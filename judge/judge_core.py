import openai
import streamlit as st

# Inicializa la API Key desde los secretos
openai.api_key = st.secrets["openai"]["api_key"]

def explain_game(rules_text):
    """Devuelve un resumen breve de las reglas usando IA"""
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en juegos de mesa y explicas las reglas de manera breve y clara."},
            {"role": "user", "content": f"Explica de forma breve estas reglas:\n{rules_text}"}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content

def judge_move(rules_text, move_text):
    """Evalúa si la jugada es válida según las reglas"""
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres un juez imparcial de juegos."},
            {"role": "user", "content": f"Estas son las reglas:\n{rules_text}\n¿Es válida esta jugada?\n{move_text}"}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content
