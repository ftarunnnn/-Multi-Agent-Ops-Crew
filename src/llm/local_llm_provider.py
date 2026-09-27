from typing import Optional
from src.llm.provider import BaseLLMProvider

class LocalLLMProvider(BaseLLMProvider):
    """
    Local LLM Provider integration (Ollama / vLLM HTTP Endpoint).
    """
    def __init__(self, model_name: str = "llama3:8b", endpoint_url: str = "http://localhost:11434"):
        super().__init__(model_name=model_name)
        self.endpoint_url = endpoint_url

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        self.logger.info(f"Generating via Local LLM ({self.model_name}) at {self.endpoint_url}")
        return f"[Local LLM {self.model_name} Output]: Simulated response for prompt '{prompt[:40]}...'"
