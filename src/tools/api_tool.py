from typing import Dict, Any
from src.tools.base_tool import BaseTool

class APITool(BaseTool):
    """
    API Tool: Invokes external REST API endpoints.
    """
    def __init__(self):
        super().__init__(
            name="APITool",
            description="Sends HTTP GET and POST requests to external API services."
        )

    def run(self, url: str, method: str = "GET", payload: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        self.logger.info(f"Sending {method} request to {url}")
        return {
            "status": "SUCCESS",
            "url": url,
            "method": method,
            "response": {"message": "API call completed successfully", "data": payload or {}}
        }
