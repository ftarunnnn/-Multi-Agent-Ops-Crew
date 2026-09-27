import os
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class BaseLLMProvider(ABC):
    """
    Abstract Base Class for LLM Providers.
    """
    def __init__(self, model_name: str, api_key: Optional[str] = None, temperature: float = 0.2):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("LLM_API_KEY", "")
        self.temperature = temperature
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generates text output for a given prompt."""
        pass
