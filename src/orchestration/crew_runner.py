import logging
from src.communication import ContextState
from src.orchestration.dag_orchestrator import DAGOrchestrator
from src.llm import LLMFactory

class CrewRunner:
    """
    CrewRunner: High-level CrewAI style facade to initiate and manage Multi-Agent Ops Crew runs.
    """
    def __init__(self, provider_name: str = "gemini", model_name: str = None):
        self.llm_provider = LLMFactory.create(provider_name=provider_name, model_name=model_name)
        self.orchestrator = DAGOrchestrator(llm_provider=self.llm_provider)
        self.logger = logging.getLogger("CrewRunner")

    def kickoff(self, user_request: str = "AI Data Analysis Automation") -> ContextState:
        self.logger.info(f"🚀 Kicking off Multi-Agent Ops Crew for task: '{user_request}'")
        initial_state = ContextState(user_request=user_request)
        final_state = self.orchestrator.run(initial_state)
        return final_state
