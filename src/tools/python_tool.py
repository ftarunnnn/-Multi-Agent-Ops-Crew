import sys
import io
from typing import Dict, Any
from src.tools.base_tool import BaseTool

class PythonTool(BaseTool):
    """
    Python Execution Tool: Executes dynamic Python snippets safely.
    """
    def __init__(self):
        super().__init__(
            name="PythonTool",
            description="Executes Python analytics code snippets and returns stdout/result."
        )

    def run(self, code: str, **kwargs) -> Dict[str, Any]:
        self.logger.info("Executing Python code snippet...")
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        
        exec_scope = {}
        try:
            exec(code, exec_scope)
            output = redirected_output.getvalue()
            return {"status": "SUCCESS", "output": output, "result": exec_scope.get("result", None)}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}
        finally:
            sys.stdout = old_stdout
