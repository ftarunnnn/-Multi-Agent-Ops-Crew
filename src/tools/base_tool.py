import logging
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseTool(ABC):
    """
    Abstract Base Class for external tools usable by agents.
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.logger = logging.getLogger(self.name)

    @abstractmethod
    def run(self, **kwargs) -> Dict[str, Any]:
        """Executes the tool logic with given arguments."""
        pass
