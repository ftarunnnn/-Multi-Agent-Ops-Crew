# Phase 6 — Agent Communication & Automated Workflow Pipeline

## Overview
Phase 6 implements automated message passing and shared state context propagation across the agent DAG.

---

## Agent Communication Data Flow

```
┌─────────────────┐
│  Planner Agent  │ (Generates Execution Plan DAG)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Data Agent    │ ───► Emits `data_artifacts`
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    ML Agent     │ ───► Emits `ml_artifacts`
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Research Agent  │ ───► Emits `research_artifacts`
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Reviewer Agent  │ ───► Audits all artifacts ───► Emits `review_results`
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Report Agent   │ ───► Compiles `final_report`
└─────────────────┘
```

---

## Shared Context State Schema (`ContextState`)

The shared workflow context state accumulates structured output objects from each agent step:

```json
{
  "task_id": "task_2026_001",
  "user_request": "AI Data Analysis Automation",
  "plan": { ... },
  "data_artifacts": { ... },
  "ml_artifacts": { ... },
  "research_artifacts": { ... },
  "review_results": { ... },
  "final_report": "# Executive Report...",
  "execution_logs": [ ... ]
}
```
