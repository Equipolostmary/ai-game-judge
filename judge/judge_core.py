import streamlit as st
import openai

# --- CARGA SEGURA DE LA API KEY DESDE STREAMLIT SECRETS ---
if "openai" not in st.secrets or "api_key" not in st.secrets["openai"]:
    raise RuntimeError("❌ No se ha encontrado la API Key de OpenAI en Secrets")

openai.api_key = st.secrets["openai"]["api_key"]


# --- EXPLICAR JUEGO EN VERSIÓN CORTA ---
def explain_game(rules_text: str) -> str:
    """
    Devuelve una explicación breve y clara del juego
    """
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un experto explicando juegos de mesa. "
                    "Explica las reglas de forma muy clara, breve y fácil "
                    "para empezar a jugar en menos de 1 minuto."
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


# --- JUZGAR UNA JUGADA ---
def judge_move(rules_text: str, move_text: str) -> str:
    """
    Evalúa si una jugada es válida según las reglas del juego
    """
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un juez imparcial de juegos. "
                    "Decide si una jugada es válida según las reglas. "
                    "Si no es válida, explica por qué de forma clara."
                )
            },
            {
                "role": "user",
                "content": (
                    f"REGLAS DEL JUEGO:\n{rules_text}\n\n"
                    f"JUGADA PROPUESTA:\n{move_text}\n\n"
                    "¿Es válida esta jugada?"
                )
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
