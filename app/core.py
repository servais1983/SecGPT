from app.models import query_llm
from app.templates import PROMPTS

class SecGPT:
    def __init__(self):
        pass

    def analyze_alert(self, raw_text):
        out = {}
        for k, prompt in PROMPTS.items():
            out[k] = query_llm(prompt.replace("{{INPUT}}", raw_text.strip()))
        return out