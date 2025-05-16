import os
from dotenv import load_dotenv
load_dotenv()

USE_OLLAMA = os.getenv("LLM_MODE", "ollama") == "ollama"

def query_llm(prompt):
    if USE_OLLAMA:
        import ollama
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    else:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']