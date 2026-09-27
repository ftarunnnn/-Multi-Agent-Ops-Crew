import sqlite3
from typing import Dict, Any
from src.tools.base_tool import BaseTool

class DatabaseTool(BaseTool):
    """
    Database Query Tool: Connects to SQLite databases and executes SQL queries.
    """
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(
            name="DatabaseTool",
            description="Executes SQL queries against relational databases."
        )
        self.db_path = db_path

    def run(self, query: str, **kwargs) -> Dict[str, Any]:
        self.logger.info(f"Executing SQL query: {query}")
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description] if cursor.description else []
            conn.close()
            return {"status": "SUCCESS", "columns": columns, "rows": rows}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}
