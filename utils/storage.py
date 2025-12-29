import json
from pathlib import Path
import streamlit as st

DATA_PATH = Path("/tmp/games.json")  # almacenamiento temporal seguro en Streamlit Cloud

def load_all_games():
    """Cargar todos los juegos globales"""
    if not DATA_PATH.exists():
        return {}
    try:
        data = json.loads(DATA_PATH.read_text())
    except json.JSONDecodeError:
        data = {}
    return data

def load_games(user):
    """Cargar juegos de un usuario"""
    data = load_all_games()
    return data.get(user, [])

def save_game(user, name, rules):
    """Guardar juego para usuario y global"""
    data = load_all_games()
    data.setdefault(user, [])
    
    # Evitar duplicados exactos
    if any(g["name"].lower() == name.lower() for g in data[user]):
        st.warning(f"El juego '{name}' ya existe para tu usuario")
        return

    # Guardar juego
    data[user].append({"name": name, "rules": rules})
    DATA_PATH.write_text(json.dumps(data, indent=2))

    # Actualizar session_state
    if "games" not in st.session_state:
        st.session_state["games"] = {}
    st.session_state["games"][user] = data[user]

def check_global_game(name):
    """Comprobar si existe un juego global"""
    data = load_all_games()
    for u_games in data.values():
        for g in u_games:
            if g["name"].lower() == name.lower():
                return g
    return None
