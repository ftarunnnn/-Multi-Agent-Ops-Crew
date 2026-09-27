from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    """
    Planner Agent: Decomposes high-level data analysis goals into a structured DAG task sequence.
    """
    def __init__(self, llm_provider=None, tools=None):
        super().__init__(
            name="PlannerAgent",
            role="System Architect & Task Planner",
            goal="Decompose user analytics tasks into actionable sub-agent DAG plans.",
            llm_provider=llm_provider,
            tools=tools
        )

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_request = state.get("user_request", "AI Data Analysis Automation")
        self.logger.info(f"Generating execution plan for: '{user_request}'")

        # Plan structure
        plan = {
            "task_id": state.get("task_id", "task_001"),
            "goal": user_request,
            "steps": [
                {
                    "step_id": 1,
                    "target_agent": "DataAgent",
                    "action": "Ingest CSV metrics and JSON feedback; calculate descriptive stats, CAC, NPS, and correlations."
                },
                {
                    "step_id": 2,
                    "target_agent": "MLAgent",
                    "action": "Train linear/ridge revenue forecast models and extract feature importances for churn."
                },
                {
                    "step_id": 3,
                    "target_agent": "ResearchAgent",
                    "action": "Retrieve SaaS 2026 growth benchmarks, CAC payback periods, and industry standards."
                },
                {
                    "step_id": 4,
                    "target_agent": "ReviewerAgent",
                    "action": "Validate mathematical consistency of Data/ML outputs and audit for numerical hallucinations."
                },
                {
                    "step_id": 5,
                    "target_agent": "ReportAgent",
                    "action": "Synthesize verified findings into publication-ready Markdown executive report."
                }
            ],
            "execution_mode": "PARALLEL_FANOUT_SYNC"
        }

        state["plan"] = plan
        return state
