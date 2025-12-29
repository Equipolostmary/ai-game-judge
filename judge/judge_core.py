import streamlit as st
from openai import OpenAI

# --- CLIENTE OPENAI ---
if "openai" not in st.secrets or "api_key" not in st.secrets["openai"]:
    raise RuntimeError("❌ Falta la API Key de OpenAI en Secrets")

client = OpenAI(api_key=st.secrets["openai"]["api_key"])


def explain_game(rules_text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Explica este juego de mesa de forma muy breve y clara."
            },
            {
                "role": "user",
                "content": rules_text
            }
        ],
    )

    return response.output_text.strip()


def judge_move(rules_text: str, move_text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
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
    )

    return response.output_text.strip()
