# Phase 8 — Workflow Orchestration (LangGraph & CrewAI Style)

## Overview
Phase 8 implements an advanced DAG workflow orchestrator (`CrewRunner`) inspired by **LangGraph** and **CrewAI**, enabling conditional branching, parallel fanout execution, and automated feedback retry loops.

---

## State Transition Graph (DAG)

```
                     ┌──────────────────┐
                     │   [START NODE]   │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Planner Agent   │
                     └────────┬─────────┘
                              │
       ┌──────────────────────┼──────────────────────┐
       │ (Parallel Execution) │                      │
       ▼                      ▼                      ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Data Agent  │       │   ML Agent   │       │Research Agent│
└──────┬───────┘       └──────┬───────┘       └──────┬───────┘
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              │ (Synchronization Join)
                              ▼
                     ┌──────────────────┐
                     │  Reviewer Agent  │
                     └────────┬─────────┘
                              │
               ┌──────────────┴──────────────┐
               │                             │
    [Passed Validation]              [Failed / Hallucinated]
               │                             │
               ▼                             ▼
     ┌──────────────────┐          ┌──────────────────┐
     │   Report Agent   │          │  Fix Loop Retry  │ ──┐
     └────────┬─────────┘          └──────────────────┘   │
              │                                           │
              ▼                                           │
     ┌──────────────────┐                                 │
     │   [END NODE]     │ ◄───────────────────────────────┘
     └──────────────────┘
```

---

## Key Features
- **Conditional Branching**: Evaluates ReviewerAgent quality scores to determine if execution proceeds to `ReportAgent` or triggers a retry loop.
- **Parallel Fanout**: Runs `DataAgent`, `MLAgent`, and `ResearchAgent` concurrently or in sequence before merging context.
- **State Checkpointing**: Saves execution state snapshots at each node transition to enable deterministic replay and debugging.
