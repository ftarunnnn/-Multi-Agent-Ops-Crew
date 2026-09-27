import os
from typing import Dict, Any
from src.tools.base_tool import BaseTool

class FileSystemTool(BaseTool):
    """
    File System Tool: Manages reading and writing project files.
    """
    def __init__(self):
        super().__init__(
            name="FileSystemTool",
            description="Reads and writes files in the project workspace."
        )

    def run(self, action: str, file_path: str, content: str = "", **kwargs) -> Dict[str, Any]:
        self.logger.info(f"FileSystemTool action: {action} on {file_path}")
        try:
            if action.lower() == "read":
                if not os.path.exists(file_path):
                    return {"status": "ERROR", "error": f"File not found: {file_path}"}
                with open(file_path, "r", encoding="utf-8") as f:
                    data = f.read()
                return {"status": "SUCCESS", "content": data}
            
            elif action.lower() == "write":
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return {"status": "SUCCESS", "message": f"Successfully wrote file to {file_path}"}
            
            else:
                return {"status": "ERROR", "error": f"Unsupported action: {action}"}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}
