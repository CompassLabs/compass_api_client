import importlib
import json
import sys
from typing import Any, Callable, List, Optional, Type

import requests
from langchain_core.callbacks import (
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass
from requests import get

from langchain_compass.model_generator import models_from_openapi

from langchain_compass.params_converter import generate_pydantic_model


class EmptySchema(BaseModel):
    pass


class PostRequestTool(BaseTool):
    name: str = "This is the tool name."
    description: str = "A description of what your tools is doing"
    url: str = "https://api.compasslabs.ai"
    args_schema: Type[BaseModel] = EmptySchema
    return_direct: bool = False
    verbose: bool = True
    response_type: Any = None
    example_args: dict = {}
    api_key: Optional[str] = None

    def _run(
        self,
        run_manager: CallbackManagerForToolRun | None = None,
        **kwargs: Any,
    ) -> dict:  # type: ignore
        """Use the tool."""

        headers = {"accept": "application/json", "Content-Type": "application/json"}
        if self.api_key is not None:
            headers["x-api-key"] = self.api_key

        response = requests.post(
            self.url,
            json=self.args_schema(**kwargs).model_dump(mode="json"),
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        if self.return_direct:  # TODO
            if "image" in response.json():
                return {"type": "image", "content": response.json()["image"]}
            return {"type": "unsigned_transaction", "content": response.json()}
        return self.response_type(**response.json())


class GetRequestTool(BaseTool):
    name: str
    description: str
    url: str
    return_direct: bool
    args_schema: Any
    verbose: bool = True
    response_type: Any
    api_key: Optional[str] = None

    def _run(
        self, run_manager: CallbackManagerForToolRun | None = None, **kwargs: Any
    ) -> dict:  # type: ignore
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        if self.api_key is not None:
            headers["x-api-key"] = self.api_key
        params = {
            key: value
            for key, value in kwargs.items()
            if "{" + key + "}" not in self.url
        }

        response = requests.get(
            self.url.format(**kwargs), params=params, headers=headers
        )
        if response.status_code != 200:
            raise Exception(response.text)
        data = response.json()
        if isinstance(data, list):
            try:
                result = self.response_type(response.json())
            except:  # noqa: E722
                result = [self.response_type(**i) for i in data][0]  # strange hack
        else:
            result = self.response_type(**response.json())

        return result


def make_tools(
    func_check_direct_return: Callable[[ModelMetaclass], bool],
    api_key: Optional[str] = None,
) -> List[BaseTool]:
    response = get("https://api.compasslabs.ai/openapi.json")
    if response.status_code != 200:
        raise Exception("Could not fetch https://api.compasslabs.ai/openapi.json!")
    openapi_data = json.loads(response.text)

    import tempfile
    from pathlib import Path

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
    tmp_file_path = Path(tmp_file.name)

    models_from_openapi(response.text, tmp_file_path)

    ###

    module_name = "temp_schemas"
    spec = importlib.util.spec_from_file_location(module_name, tmp_file_path.as_posix())
    if not spec:
        raise Exception("Unable to generate openapi model spec.")
    schemas = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = schemas
    spec.loader.exec_module(schemas)  # type: ignore
    ###

    def get_response_schema_name(endpoint: dict) -> str:
        return endpoint["responses"]["200"]["content"]["application/json"]["schema"][
            "$ref"
        ].split("/")[-1]

    tools: list[BaseTool] = []
    for path in openapi_data["paths"].keys():
        if "patch" in openapi_data["paths"][path]:
            raise ValueError("We don't support patch requests yet.")
        if "update" in openapi_data["paths"][path]:
            raise ValueError("We don't support update requests yet.")

        url: str = (
            openapi_data["servers"][0]["url"].rstrip("/") + "/" + path.lstrip("/")
        )

        if "post" in openapi_data["paths"][path]:
            endpoint = openapi_data["paths"][path]["post"]

            schema_name = endpoint["requestBody"]["content"]["application/json"][
                "schema"
            ]["$ref"].split("/")[-1]

            # TODO: The SDK itself is inconsistent here.
            #  Maybe we should just run datamodel-codegen in CI.
            # args_schema = test.get(schema_name)
            # args_schema = globals()[schema_name]
            args_schema = getattr(schemas, schema_name)

            description: str = (
                endpoint["description"]
                if "description" in endpoint
                else endpoint["summary"]
            )
            response_schema_name = get_response_schema_name(endpoint)

            # response_type = test.get(response_schema_name)
            response_type = getattr(schemas, response_schema_name)

            if "default" not in openapi_data["components"]["schemas"][schema_name]:
                raise ValueError(
                    "Unable to build tools."
                    "Pls message contact@compasslabs.ai to resolve this."
                )
            example_args = openapi_data["components"]["schemas"][schema_name]["default"]

            return_direct: bool = (
                False
                if func_check_direct_return is None
                else func_check_direct_return(response_type)
            )

            post_tool = PostRequestTool(
                name=endpoint['operationId'],
                description=description,
                url=url,
                args_schema=args_schema,
                return_direct=return_direct,
                verbose=False,
                response_type=response_type,
                example_args=example_args,
                api_key="123",
            )

            post_tool.__name__ = endpoint['operationId']  # type: ignore
            tools.append(post_tool)

        if "get" in openapi_data["paths"][path]:
            # raise ValueError("Not yet fully implemented.")
            endpoint = openapi_data["paths"][path]["get"]
            description: str = (
                endpoint["description"]
                if "description" in endpoint
                else endpoint["summary"]
            )
            response_schema_name = get_response_schema_name(endpoint)
            response_type = getattr(schemas, response_schema_name)

            if "parameters" in endpoint:
                Params = generate_pydantic_model(
                    model_name="Params", parameters=endpoint["parameters"]
                )
            else:
                Params = None
            #
            get_tool = GetRequestTool(
                name=endpoint['operationId'],
                description=description,
                url=url,
                return_direct=False,
                args_schema=Params,
                response_type=response_type,
                api_key="123",
            )

            get_tool.__name__ = endpoint['operationId']  # type: ignore
            tools.append(get_tool)

    return tools  # [:3]  # type: ignore


if __name__ == "__main__":
    tools = make_tools(
        api_key=None,
        func_check_direct_return=lambda x: True,
    )
