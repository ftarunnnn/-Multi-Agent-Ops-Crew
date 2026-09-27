import logging
from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.communication.context_state import ContextState

class SequentialWorkflowPipeline:
    """
    Automated sequential workflow execution engine that passes output from agent to agent.
    """
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.logger = logging.getLogger("WorkflowPipeline")

    def run(self, initial_state: ContextState) -> ContextState:
        self.logger.info(f"Starting Multi-Agent Workflow Pipeline with {len(self.agents)} agents...")
        
        state_dict = initial_state.to_dict()
        for agent in self.agents:
            self.logger.info(f"▶ Step: Handing off context state to {agent.name}...")
            state_dict = agent.run(state_dict)

        updated_context = ContextState.from_dict(state_dict)
        self.logger.info("🎉 Multi-Agent Workflow Pipeline execution completed successfully!")
        return updated_context
