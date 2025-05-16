PROMPTS = {
    "summary": """Tu es un analyste sécurité. Résume cette alerte de façon claire :
{{INPUT}}""",
    "response": """Tu es membre Blue Team. Quelle serait la réponse appropriée à :
{{INPUT}}""",
    "playbook": """Rédige un mini-playbook de réponse SOC basé sur l'alerte suivante :
{{INPUT}}""",
    "yara": """Génère une règle YARA basique pour détecter ce type de menace :
{{INPUT}}"""
}