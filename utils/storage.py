import json
from pathlib import Path

# Archivo de datos
DATA_PATH = Path("data/games.json")

def load_games(user):
    """
    Carga todos los juegos de un usuario.
    Devuelve lista vacía si no hay nada.
    """
    if not DATA_PATH.exists():
        return []
    try:
        data = json.loads(DATA_PATH.read_text())
    except json.JSONDecodeError:
        data = {}
    return data.get(user, [])

def save_game(user, name, rules):
    """
    Guarda un juego nuevo para un usuario.
    Crea la carpeta 'data' si no existe.
    """
    # Cargar datos existentes
    if DATA_PATH.exists():
        try:
            data = json.loads(DATA_PATH.read_text())
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    # Añadir juego
    data.setdefault(user, []).append({
        "name": name,
        "rules": rules
    })

    # Crear carpeta si no existe
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Guardar en archivo JSON
    DATA_PATH.write_text(json.dumps(data, indent=2))

