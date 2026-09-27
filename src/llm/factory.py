from typing import Optional
from src.llm.provider import BaseLLMProvider
from src.llm.gemini_provider import GeminiProvider
from src.llm.openai_provider import OpenAIProvider
from src.llm.claude_provider import ClaudeProvider
from src.llm.local_llm_provider import LocalLLMProvider

class LLMFactory:
    """
    Factory for instantiating LLM Providers based on name.
    """
    @staticmethod
    def create(provider_name: str = "gemini", model_name: Optional[str] = None, api_key: Optional[str] = None) -> BaseLLMProvider:
        provider_key = provider_name.lower()
        
        if provider_key == "gemini":
            return GeminiProvider(model_name=model_name or "gemini-1.5-pro", api_key=api_key)
        elif provider_key in ["openai", "gpt"]:
            return OpenAIProvider(model_name=model_name or "gpt-4o", api_key=api_key)
        elif provider_key == "claude":
            return ClaudeProvider(model_name=model_name or "claude-3-5-sonnet", api_key=api_key)
        elif provider_key in ["local", "ollama", "vllm"]:
            return LocalLLMProvider(model_name=model_name or "llama3:8b")
        else:
            # Fallback default
            return GeminiProvider(model_name=model_name or "gemini-1.5-flash", api_key=api_key)
