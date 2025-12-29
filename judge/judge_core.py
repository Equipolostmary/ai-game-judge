import streamlit as st
from openai import OpenAI

# --- CREAR CLIENTE OPENAI DESDE STREAMLIT SECRETS ---
if "openai" not in st.secrets or "api_key" not in st.secrets["openai"]:
    raise RuntimeError("❌ Falta la API Key de OpenAI en Secrets")

client = OpenAI(api_key=st.secrets["openai"]["api_key"])


# --- EXPLICAR JUEGO ---
def explain_game(rules_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un experto en juegos de mesa. "
                    "Explica las reglas de forma MUY breve, clara y práctica "
                    "para empezar a jugar inmediatamente."
                )
            },
            {
                "role": "user",
                "content": rules_text
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()


# --- JUZGAR JUGADA ---
def judge_move(rules_text: str, move_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un juez imparcial de juegos."
            },
            {
                "role": "user",
                "content": (
                    f"REGLAS:\n{rules_text}\n\n"
                    f"JUGADA:\n{move_text}\n\n"
                    "¿Es válida?"
                )
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
