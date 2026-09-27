from typing import Optional
from src.llm.provider import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI LLM Provider integration (GPT-4o, GPT-3.5-turbo).
    """
    def __init__(self, model_name: str = "gpt-4o", api_key: Optional[str] = None):
        super().__init__(model_name=model_name, api_key=api_key)

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        self.logger.info(f"Generating via OpenAI model: {self.model_name}")
        if not self.api_key:
            return f"[OpenAI {self.model_name} Output]: Processed query '{prompt[:40]}...'"
        return f"[OpenAI Response for {prompt[:30]}]"
