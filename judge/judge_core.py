import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "Eres un juez neutral de juegos de mesa y juegos sociales. "
    "Interpretas reglas, explicas cómo se juega de forma clara "
    "y decides si una jugada es válida, dudosa o no válida, "
    "siempre con una explicación breve."
)

def explain_game(rules: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Estas son las reglas del juego:\n\n"
                    f"{rules}\n\n"
                    "Explícalo de forma corta y clara para jugadores antes de empezar."
                ),
            },
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content


def judge_move(rules: str, move: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Reglas del juego:\n"
                    f"{rules}\n\n"
                    "Jugada del jugador:\n"
                    f"{move}\n\n"
                    "Decide si la jugada es VÁLIDA, DUDOSA o NO VÁLIDA "
                    "y explica brevemente el motivo."
                ),
            },
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
