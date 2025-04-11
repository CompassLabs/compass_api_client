from typing import Any

from langchain_tests.integration_tests import ToolsIntegrationTests

from langchain_compass.toolkits import LangchainCompassToolkit

tools = LangchainCompassToolkit(compass_api_key=None).get_tools()


for tool in tools:
    class_name = f"Test_{tool.name.capitalize()}Tool"

    def make_class(tool: Any) -> type[ToolsIntegrationTests]:
        class TestTool(ToolsIntegrationTests):
            @property
            def tool_constructor(self) -> Any:
                # self.tool_invoke_params_example = {"a": 2}
                return tool

            @property
            def tool_constructor_params(self) -> dict:
                return {}

            @property
            def tool_invoke_params_example(self) -> dict:
                return tool.example_args

        return TestTool

    # Dynamically add it to the module so pytest can discover it
    globals()[class_name] = make_class(tool)
