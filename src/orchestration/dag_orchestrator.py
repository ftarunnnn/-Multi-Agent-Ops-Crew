import logging
from typing import Dict, Any, List
from src.agents import PlannerAgent, DataAgent, MLAgent, ResearchAgent, ReviewerAgent, ReportAgent
from src.communication import ContextState
from src.orchestration.state_machine import StateMachine

class DAGOrchestrator:
    """
    DAG Orchestrator: Graph execution engine with conditional branching & review validation loops.
    """
    def __init__(self, llm_provider=None):
        self.planner = PlannerAgent(llm_provider=llm_provider)
        self.data_agent = DataAgent(llm_provider=llm_provider)
        self.ml_agent = MLAgent(llm_provider=llm_provider)
        self.research_agent = ResearchAgent(llm_provider=llm_provider)
        self.reviewer = ReviewerAgent(llm_provider=llm_provider)
        self.report_agent = ReportAgent(llm_provider=llm_provider)
        self.state_machine = StateMachine()
        self.logger = logging.getLogger("DAGOrchestrator")

    def run(self, initial_state: ContextState) -> ContextState:
        state_dict = initial_state.to_dict()
        self.logger.info("⚡ Executing Multi-Agent Crew DAG Pipeline...")

        # Step 1: Planner Node
        self.logger.info("Executing Node: Planner")
        state_dict = self.planner.run(state_dict)
        self.state_machine.checkpoint("Planner", state_dict)

        # Step 2: Parallel Fanout (Data, ML, Research)
        self.logger.info("Executing Node: Data Agent")
        state_dict = self.data_agent.run(state_dict)
        self.state_machine.checkpoint("DataAgent", state_dict)

        self.logger.info("Executing Node: ML Agent")
        state_dict = self.ml_agent.run(state_dict)
        self.state_machine.checkpoint("MLAgent", state_dict)

        self.logger.info("Executing Node: Research Agent")
        state_dict = self.research_agent.run(state_dict)
        self.state_machine.checkpoint("ResearchAgent", state_dict)

        # Step 3: Reviewer Node (Audit & Validation)
        self.logger.info("Executing Node: Reviewer Agent")
        state_dict = self.reviewer.run(state_dict)
        self.state_machine.checkpoint("ReviewerAgent", state_dict)

        # Conditional Branching on Audit Result
        review_status = state_dict.get("review_results", {}).get("status", "APPROVED")
        if review_status != "APPROVED":
            self.logger.warning("⚠️ Reviewer flagged issues! Retrying DataAgent execution...")
            state_dict = self.data_agent.run(state_dict)
            state_dict = self.reviewer.run(state_dict)

        # Step 4: Report Agent Node
        self.logger.info("Executing Node: Report Agent")
        state_dict = self.report_agent.run(state_dict)
        self.state_machine.checkpoint("ReportAgent", state_dict)

        self.logger.info("🎉 DAG Execution Completed Successfully!")
        return ContextState.from_dict(state_dict)
