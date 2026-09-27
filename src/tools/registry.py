from typing import Dict, List
from src.tools.base_tool import BaseTool
from src.tools.python_tool import PythonTool
from src.tools.database_tool import DatabaseTool
from src.tools.api_tool import APITool
from src.tools.web_search_tool import WebSearchTool
from src.tools.file_system_tool import FileSystemTool

class ToolRegistry:
    """
    Central Registry for managing and retrieving agent tools.
    """
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        # Register default tools
        self.register(PythonTool())
        self.register(DatabaseTool())
        self.register(APITool())
        self.register(WebSearchTool())
        self.register(FileSystemTool())

    def register(self, tool: BaseTool):
        self._tools[tool.name.lower()] = tool

    def get(self, name: str) -> BaseTool:
        return self._tools.get(name.lower())

    def list_tools(self) -> List[str]:
        return list(self._tools.keys())
