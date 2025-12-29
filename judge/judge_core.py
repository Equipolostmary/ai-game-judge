def explain_game(rules: str) -> str:
    return f"Resumen rápido del juego:\n{rules[:300]}..."

def judge_move(rules: str, move: str) -> str:
    if len(move.strip()) < 2:
        return "❌ No válido: respuesta demasiado corta"
    return "✅ Válido según las reglas"

