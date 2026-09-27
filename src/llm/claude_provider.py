from typing import Optional
from src.llm.provider import BaseLLMProvider

class ClaudeProvider(BaseLLMProvider):
    """
    Anthropic Claude LLM Provider integration (Claude 3.5 Sonnet, Haiku).
    """
    def __init__(self, model_name: str = "claude-3-5-sonnet", api_key: Optional[str] = None):
        super().__init__(model_name=model_name, api_key=api_key)

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        self.logger.info(f"Generating via Claude model: {self.model_name}")
        if not self.api_key:
            return f"[Claude {self.model_name} Output]: Processed query '{prompt[:40]}...'"
        return f"[Claude Response for {prompt[:30]}]"
