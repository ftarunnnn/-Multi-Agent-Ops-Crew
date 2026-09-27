# 🤖 Multi-Agent Ops Crew — 10-Phase Autonomous AI Data Science System

[![GitHub Repository](https://img.shields.io/badge/GitHub-ftarunnnn%2F--Multi--Agent--Ops--Crew-blue?style=for-the-badge&logo=github)](https://github.com/ftarunnnn/-Multi-Agent-Ops-Crew)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-green?style=for-the-badge&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Status](https://img.shields.io/badge/All_Phases-100%25_Complete-brightgreen?style=for-the-badge)]()

Welcome to **Multi-Agent Ops Crew**, a complete, production-grade autonomous data science crew built across **10 structured project phases**.

---

## 🎯 10 Project Phases Implementation Roadmap

| Phase | Title | Description | Primary Deliverable |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **Problem Definition** | Real-world problem definition: **AI Data Analysis Automation** | [`phase_1_problem_definition/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_1_problem_definition/PROBLEM_DEFINITION.md) |
| **Phase 2** | **System Architecture** | Agent topology design: Planner ➔ Data/ML/Research ➔ Reviewer ➔ Report | [`phase_2_system_architecture/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_2_system_architecture/ARCHITECTURE.md) |
| **Phase 3** | **Agent Creation** | Specialized agents: Planner, Data, ML, Research, Reviewer, & Report Agents | [`phase_3_agent_creation/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_3_agent_creation/AGENT_CREATION.md) |
| **Phase 4** | **LLM Integration** | Multi-LLM provider abstraction: Gemini, OpenAI, Claude, Local LLMs | [`phase_4_llm_integration/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_4_llm_integration/LLM_INTEGRATION.md) |
| **Phase 5** | **Tool Integration** | External tools: Python code executor, SQLite DB, REST API, Web Search, FS | [`phase_5_tool_integration/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_5_tool_integration/TOOL_INTEGRATION.md) |
| **Phase 6** | **Agent Communication**| Shared `ContextState` propagation and automated event message bus | [`phase_6_agent_communication/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_6_agent_communication/AGENT_COMMUNICATION.md) |
| **Phase 7** | **Memory / RAG** | Sliding conversation memory & TF-IDF VectorStore RAG retrieval engine | [`phase_7_memory_rag/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_7_memory_rag/MEMORY_RAG.md) |
| **Phase 8** | **Workflow Orchestration**| LangGraph & CrewAI style DAG execution graph with retry loops | [`phase_8_workflow_orchestration/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_8_workflow_orchestration/WORKFLOW_ORCHESTRATION.md) |
| **Phase 9** | **Testing & Evaluation**| Pytest test suite, zero-hallucination auditor & quality evaluator | [`phase_9_testing_evaluation/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_9_testing_evaluation/TESTING_EVALUATION.md) |
| **Phase 10**| **Deployment & Monitoring**| FastAPI REST API, interactive Web UI Dashboard & telemetry metrics | [`phase_10_deployment_monitoring/`](file:///c:/Users/aruni/Desktop/New%20folder/phase_10_deployment_monitoring/DEPLOYMENT_MONITORING.md) |

---

## 🏗️ Simple System Architecture

```
                                USER / REQUEST
                                      │
                                      ▼
                                PLANNER AGENT
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
          DATA AGENT              ML AGENT             RESEARCH AGENT
              └───────────────────────┼───────────────────────┘
                                      │
                                      ▼
                                REVIEWER AGENT
                                      │
                                      ▼
                                 REPORT AGENT
                                      │
                                      ▼
                                FINAL OUTPUT
```

---

## 🚀 Quick Start Guide

### 1. Run via CLI
```bash
python run_crew.py --task "AI Data Analysis Automation" --provider gemini
```

### 2. Run Test Suite (Phase 9)
```bash
python run_tests.py
```

### 3. Launch REST API (Phase 10)
```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 4. Interactive Web UI Dashboard (Phase 10)
Open [`web/index.html`](file:///c:/Users/aruni/Desktop/New%20folder/web/index.html) in any modern web browser to interact with the full DAG visualizer and execution simulator!

---

## 📊 Logical Progression for AI/DS Students
```
Basic ML / DL ➔ LLMs ➔ RAG ➔ AI Agents ➔ Multi-Agent Systems ➔ Agentic AI
```