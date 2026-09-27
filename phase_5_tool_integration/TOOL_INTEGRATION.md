# Phase 5 — Tool Integration

## Overview
Phase 5 equips agents with secure, standardized external tools (`BaseTool`) to interact with the environment, execute Python code, query databases, invoke REST APIs, perform web searches, and manage file artifacts.

---

## Tool Taxonomy

```
                       ┌──────────────────────┐
                       │       BaseTool       │
                       └──────────┬───────────┘
                                  │
      ┌───────────┬───────────────┼───────────────┬───────────┐
      ▼           ▼               ▼               ▼           ▼
┌──────────┐┌───────────┐  ┌─────────────┐  ┌───────────┐┌───────────┐
│PythonTool││DatabaseTool│ │ WebSearchTool│ │  APITool  ││FileSystem Tool│
└──────────┘└───────────┘  └─────────────┘  └───────────┘└───────────┘
```

---

## Integrated Tools List

| Tool Name | Class | Primary Function |
| :--- | :--- | :--- |
| **Python Execution Tool** | `PythonTool` | Safely evaluates Python expressions and Pandas analytics code. |
| **Database Tool** | `DatabaseTool` | Connects to SQLite databases and executes SQL queries. |
| **API Tool** | `APITool` | Sends HTTP GET/POST requests to external REST APIs. |
| **Web Search Tool** | `WebSearchTool` | Performs domain search queries for current market benchmarks. |
| **File System Tool** | `FileSystemTool` | Reads and writes files to the local workspace safely. |
