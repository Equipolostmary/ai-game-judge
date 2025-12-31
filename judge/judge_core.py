import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def judge_game(game_name, rules_text, player_action):
    prompt = f"""
Eres un juez supremo, serio y con autoridad absoluta.
Conoces perfectamente el juego: {game_name}.

REGLAS DEL JUEGO:
{rules_text}

ACCIÓN DEL JUGADOR:
{player_action}

Dicta un veredicto claro:
- ¿Es válida o no?
- Explica brevemente
- Usa tono de juez, firme y serio
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
