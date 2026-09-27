# Phase 4 — LLM Integration

## Overview
Phase 4 implements a flexible, multi-provider LLM abstraction layer (`LLMProvider`) enabling the Multi-Agent Ops Crew to seamlessly switch between OpenAI, Gemini, Claude, Local LLMs (Ollama/vLLM), and offline fallback mock engines.

---

## Provider Architecture

```
                       ┌──────────────────────┐
                       │     BaseLLMProvider  │
                       └──────────┬───────────┘
                                  │
       ┌──────────────────┬───────┴──────────┬──────────────────┐
       ▼                  ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│GeminiProvider│   │OpenAIProvider│   │ClaudeProvider│   │LocalLLMProv. │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

---

## Supported Providers & Models

| Provider Key | Provider Name | Default Model | Fallback Supported |
| :--- | :--- | :--- | :--- |
| `gemini` | Google Gemini | `gemini-1.5-pro` | Yes |
| `openai` | OpenAI | `gpt-4o` | Yes |
| `claude` | Anthropic Claude | `claude-3-5-sonnet` | Yes |
| `local` | Ollama / vLLM | `llama3:8b` | Yes |
| `mock` | Mock Provider | `mock-engine-v1` | Yes (Default Offline) |

---

## Configuration & Usage
```python
from src.llm import LLMFactory

# Get a Gemini provider instance
llm = LLMFactory.create(provider_name="gemini", model_name="gemini-1.5-pro")
response = llm.generate(prompt="Analyze revenue metrics for Q1.")
```
