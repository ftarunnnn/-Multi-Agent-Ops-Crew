import time
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

class BaseAgent(ABC):
    """
    Abstract Base Class for all Multi-Agent Ops Crew agents.
    """
    def __init__(
        self,
        name: str,
        role: str,
        goal: str,
        llm_provider: Optional[Any] = None,
        tools: Optional[List[Any]] = None
    ):
        self.name = name
        self.role = role
        self.goal = goal
        self.llm_provider = llm_provider
        self.tools = tools or []
        self.logger = logging.getLogger(self.name)

    @abstractmethod
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the agent's task and updates the workflow state.
        
        Args:
            state (Dict[str, Any]): Current shared workflow context state.
            
        Returns:
            Dict[str, Any]: Updated shared workflow context state.
        """
        pass

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info(f"🚀 Running agent: {self.name} ({self.role})")
        start_time = time.time()
        
        try:
            updated_state = self.execute(state)
            duration = round(time.time() - start_time, 3)
            
            # Log step execution event
            if "execution_logs" not in updated_state:
                updated_state["execution_logs"] = []
                
            updated_state["execution_logs"].append({
                "agent": self.name,
                "status": "SUCCESS",
                "duration_seconds": duration,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            
            self.logger.info(f"✅ Completed agent: {self.name} in {duration}s")
            return updated_state
        except Exception as e:
            self.logger.error(f"❌ Error in agent {self.name}: {str(e)}", exc_info=True)
            if "execution_logs" not in state:
                state["execution_logs"] = []
            state["execution_logs"].append({
                "agent": self.name,
                "status": "FAILED",
                "error": str(e),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            raise e
