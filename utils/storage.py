import json
from pathlib import Path

DATA_PATH = Path("data/games.json")

def load_games(user):
    if not DATA_PATH.exists():
        return []
    data = json.loads(DATA_PATH.read_text())
    return data.get(user, [])

def save_game(user, name, rules):
    if DATA_PATH.exists():
        data = json.loads(DATA_PATH.read_text())
    else:
        data = {}

    data.setdefault(user, []).append({
        "name": name,
        "rules": rules
    })

    DATA_PATH.parent.mkdir(exist_ok=True)
    DATA_PATH.write_text(json.dumps(data, indent=2))

