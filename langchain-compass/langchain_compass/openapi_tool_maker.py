import json
from typing import Any, Callable, List, Optional, Type

import requests
from compass.api_client import api_client  # type: ignore
from langchain_core.callbacks import (
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass
from requests import get

from langchain_compass.params_converter import generate_pydantic_model


class EmptySchema(BaseModel):
    pass


class PostRequestTool(BaseTool):
    name: str = "This is the tool name."
    description: str = "A description of what your tools is doing"
    url: str = "https://api.compasslabs.ai"
    args_schema: Type[BaseModel] = EmptySchema
    return_direct: bool = False
    verbose: bool = False
    response_type: Any = None
    example_args: Optional[dict] = None
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
        tool_name = path.replace("/v0/", "").replace("/", "_") + "_"  # TODO

        if "post" in openapi_data["paths"][path]:
            endpoint = openapi_data["paths"][path]["post"]

            schema_name = endpoint["requestBody"]["content"]["application/json"][
                "schema"
            ]["$ref"].split("/")[-1]

            # TODO: The SDK itself is inconsistent here.
            #  Maybe we should just run datamodel-codegen in CI.
            args_schema = (
                getattr(api_client.compass.api_client, schema_name)
                if hasattr(api_client.compass.api_client, schema_name)
                else getattr(
                    api_client.compass.api_client, schema_name.rstrip("Request")
                )
            )

            description: str = (
                endpoint["description"]
                if "description" in endpoint
                else endpoint["summary"]
            )
            response_schema_name = get_response_schema_name(endpoint)

            response_type = getattr(api_client.compass.api_client, response_schema_name)

            example_args = (
                openapi_data["components"]["schemas"][schema_name]["example"]
                if "example" in openapi_data["components"]["schemas"][schema_name]
                else None
            )

            return_direct: bool = (
                False
                if func_check_direct_return is None
                else func_check_direct_return(response_type)
            )

            post_tool = PostRequestTool(
                name=tool_name,
                description=description,
                url=url,
                args_schema=args_schema,
                return_direct=return_direct,
                verbose=False,
                response_type=response_type,
                example_args=example_args,
                api_key="123",
            )

            post_tool.__name__ = tool_name  # type: ignore
            tools.append(post_tool)

        if "get" in openapi_data["paths"][path]:
            endpoint = openapi_data["paths"][path]["get"]

            response_schema_name = get_response_schema_name(endpoint)
            response_type = getattr(api_client.compass.api_client, response_schema_name)

            if "parameters" in endpoint:
                Params = generate_pydantic_model(
                    model_name="Params", parameters=endpoint["parameters"]
                )
            else:
                Params = None

            get_tool = GetRequestTool(
                name=tool_name,
                description=endpoint["description"],
                url=url,
                return_direct=False,
                args_schema=Params,
                response_type=response_type,
                api_key="123",
            )

            get_tool.__name__ = tool_name  # type: ignore
            tools.append(get_tool)

    return tools  # type: ignore


if __name__ == "__main__":
    make_tools(
        api_key=None,
        func_check_direct_return=lambda x: True,
    )
