# Phase 3 — Agent Creation

## Overview
Phase 3 implements specialized, production-grade Python agents adhering to the architecture defined in Phase 2. Each agent inherits from `BaseAgent` and implements a deterministic execution lifecycle (`run()`).

---

## Agent Directory Structure
```
src/agents/
├── __init__.py
├── base_agent.py          # Abstract Base Agent Class
├── planner_agent.py       # Decomposes goal into DAG plan
├── data_agent.py          # Performs data cleaning & statistical analytics
├── ml_agent.py            # Trains predictive models & computes feature importances
├── research_agent.py      # Retrieves domain context & industry benchmarks
├── reviewer_agent.py      # Audits outputs for hallucinations & calculation consistency
└── report_agent.py        # Compiles executive Markdown report
```

---

## Base Agent Contract (`base_agent.py`)

Every agent conforms to the following lifecycle contract:

```python
class BaseAgent(ABC):
    def __init__(self, name: str, role: str, llm_provider=None, tools=None):
        self.name = name
        self.role = role
        self.llm_provider = llm_provider
        self.tools = tools or []

    @abstractmethod
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Core execution logic returning updated context state."""
        pass
```
