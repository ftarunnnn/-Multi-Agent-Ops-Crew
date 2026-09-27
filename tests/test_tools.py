import unittest
import tempfile
import os
from src.tools import PythonTool, DatabaseTool, APITool, WebSearchTool, FileSystemTool

class TestTools(unittest.TestCase):
    def test_python_tool(self):
        tool = PythonTool()
        res = tool.run(code="result = 10 * 5")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["result"], 50)

    def test_web_search_tool(self):
        tool = WebSearchTool()
        res = tool.run(query="SaaS benchmarks 2026")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertGreater(len(res["results"]), 0)

    def test_file_system_tool(self):
        tool = FileSystemTool()
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_file = os.path.join(tmp_dir, "test.txt")
            write_res = tool.run(action="write", file_path=test_file, content="Hello Crew")
            self.assertEqual(write_res["status"], "SUCCESS")
            read_res = tool.run(action="read", file_path=test_file)
            self.assertEqual(read_res["status"], "SUCCESS")
            self.assertEqual(read_res["content"], "Hello Crew")

if __name__ == "__main__":
    unittest.main()
