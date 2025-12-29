import json
from pathlib import Path
import streamlit as st

# Archivo seguro en Streamlit Cloud
DATA_PATH = Path("/tmp/games.json")

def load_games(user):
    """Carga todos los juegos de un usuario. Devuelve lista vacía si no hay nada."""
    if not DATA_PATH.exists():
        return []
    try:
        data = json.loads(DATA_PATH.read_text())
    except json.JSONDecodeError:
        data = {}
    return data.get(user, [])

def save_game(user, name, rules):
    """Guarda un juego nuevo para un usuario y actualiza session_state para refrescar la UI."""
    # Cargar datos existentes
    if DATA_PATH.exists():
        try:
            data = json.loads(DATA_PATH.read_text())
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    # Añadir juego
    data.setdefault(user, []).append({"name": name, "rules": rules})

    # Guardar en JSON
    DATA_PATH.write_text(json.dumps(data, indent=2))

    # Actualizar session_state para refrescar la lista de juegos
    if "games" not in st.session_state:
        st.session_state["games"] = {}
    st.session_state["games"][user] = data[user]
