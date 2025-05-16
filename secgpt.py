#!/usr/bin/env python3

from app.core import SecGPT
import argparse

def main():
    parser = argparse.ArgumentParser(description="SecGPT - Assistant IA SOC")
    parser.add_argument("--input", required=True, help="Chemin d'une alerte brute (texte)")
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        alert_text = f.read()

    gpt = SecGPT()
    result = gpt.analyze_alert(alert_text)

    print("\n[Résumé 📄]")
    print(result['summary'])

    print("\n[Réponse 🔧]")
    print(result['response'])

    print("\n[Playbook ⚙️]")
    print(result['playbook'])

    print("\n[YARA 🧬]")
    print(result['yara'])

if __name__ == "__main__":
    main()