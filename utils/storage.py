import json
from pathlib import Path

# Archivo seguro en Streamlit Cloud
DATA_PATH = Path("/tmp/games.json")

def load_games(user):
    if not DATA_PATH.exists():
        return []
    try:
        data = json.loads(DATA_PATH.read_text())
    except json.JSONDecodeError:
        data = {}
    return data.get(user, [])

def save_game(user, name, rules):
    if DATA_PATH.exists():
        try:
            data = json.loads(DATA_PATH.read_text())
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    data.setdefault(user, []).append({
        "name": name,
        "rules": rules
    })

    # Guardar en JSON sin mkdir, /tmp ya existe
    DATA_PATH.write_text(json.dumps(data, indent=2))
