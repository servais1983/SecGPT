import gradio as gr
from app.core import SecGPT

sec = SecGPT()

def run_all(text):
    res = sec.analyze_alert(text)
    return res['summary'], res['response'], res['playbook'], res['yara']

iface = gr.Interface(
    fn=run_all,
    inputs=gr.Textbox(lines=15, label="Alerte brute"),
    outputs=[
        gr.Textbox(label="Résumé"),
        gr.Textbox(label="Réponse"),
        gr.Textbox(label="Playbook"),
        gr.Textbox(label="Règle YARA")
    ],
    title="SecGPT – Assistant IA Blue Team",
    description="Coller une alerte, et laissez l'IA faire le reste."
)

if __name__ == "__main__":
    iface.launch()