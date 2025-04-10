"""LangchainCompass toolkits."""

from typing import List, Optional

from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import Field

from langchain_compass.openapi_tool_maker import make_tools


class LangchainCompassToolkit(BaseToolkit):
    # TODO: Replace all TODOs in docstring. See example docstring:
    # https://github.com/langchain-ai/langchain/blob/c123cb2b304f52ab65db4714eeec46af69a861ec/libs/community/langchain_community/agent_toolkits/sql/toolkit.py#L19
    """LangchainCompass toolkit.

    # TODO: Replace with relevant packages, env vars, etc.
    Setup:
        Install ``langchain-compass`` and set environment variable ``COMPASS_API_KEY``.

        .. code-block:: bash

            pip install -U langchain-compass
            export COMPASS_API_KEY="your-api-key"

    # TODO: Populate with relevant params.
    Key init args:
        arg 1: type
            description
        arg 2: type
            description

    # TODO: Replace with relevant init params.
    Instantiate:
        .. code-block:: python

            from langchain-compass import LangchainCompassToolkit

            toolkit = LangchainCompassToolkit(
                # ...
            )

    Tools:
        .. code-block:: python

            toolkit.get_tools()

        .. code-block:: none

            # TODO: Example output.

    Use within an agent:
        .. code-block:: python

            from langgraph.prebuilt import create_react_agent

            agent_executor = create_react_agent(llm, tools)

            example_query = "..."

            events = agent_executor.stream(
                {"messages": [("user", example_query)]},
                stream_mode="values",
            )
            for event in events:
                event["messages"][-1].pretty_print()

        .. code-block:: none

             # TODO: Example output.

    """  # noqa: E501

    api_key: Optional[str] = Field(default=None, alias="compass_api_key")

    def __init__(self, compass_api_key: Optional[str] = None) -> None:
        super().__init__()
        self.api_key = compass_api_key

    def get_tools(self) -> List[BaseTool]:
        compass_tools: List[BaseTool]
        compass_tools = make_tools(
            api_key=self.api_key,
            func_check_direct_return=lambda r: r.__name__.lower()
            in ["unsignedtransaction", "image"],
        )
        compass_tools = [
            tool for tool in compass_tools if "set_any" not in tool.get_name()
        ]
        return compass_tools
