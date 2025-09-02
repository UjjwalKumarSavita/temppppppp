import os
from typing import Optional

class LLM:
    def ask(self, system: str, user: str) -> str:
        return ""

class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4o-mini", api_key: Optional[str] = None):
        try:
            from openai import OpenAI
            key = api_key or os.getenv("OPENAI_API_KEY")
            self.client = OpenAI(api_key=key) if key else None
            self.model = model
        except Exception:
            self.client = None
            self.model = model
    def ask(self, system: str, user: str) -> str:
        if not self.client:
            return ""
        try:
            r = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role":"system","content":system},{"role":"user","content":user}],
                temperature=0
            )
            return r.choices[0].message.content.strip()
        except Exception:
            return ""

class NullLLM(LLM):
    def ask(self, system: str, user: str) -> str:
        return ""

def build_llm() -> LLM:
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return OpenAILLM()
    return NullLLM()
