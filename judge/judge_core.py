from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Eres un juez de juegos de mesa con autoridad absoluta.
No opinas, no negocias, no eres amable.
Solo aplicas las reglas aprendidas y dictas veredictos claros.

Formato obligatorio de respuesta:

⚖️ VEREDICTO
Decisión: VÁLIDO / NO VÁLIDO
Motivo: explicación breve citando las reglas
"""

def judge_event(game_name, rules, event_description):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Juego: {game_name}

Reglas del juego:
{rules}

Hecho ocurrido durante la partida:
{event_description}

Dicta veredicto.
"""
            }
        ],
        temperature=0.2
    )

    return response.output_text
