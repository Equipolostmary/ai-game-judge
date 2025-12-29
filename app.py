import streamlit as st
from utils.storage import save_game, load_games
from judge.judge_core import explain_game, judge_move

st.set_page_config(page_title="El Juez de Juegos", layout="wide")

st.title("El Juez de Juegos")

# ---------------------------------------------
# Registro de usuario
# ---------------------------------------------
if "user" not in st.session_state or not st.session_state.user:
    user_input = st.text_input("Introduce tu nombre de usuario:")
    if user_input:
        st.session_state.user = user_input

# Continuar solo si el usuario está definido
if "user" in st.session_state and st.session_state.user:
    user = st.session_state.user
    st.subheader(f"Bienvenido, {user}!")

    # ---------------------------------------------
    # Crear juego nuevo
    # ---------------------------------------------
    st.subheader("Crear un juego nuevo")
    name = st.text_input("Nombre del juego")
    rules = st.text_area("Reglas del juego")

    if st.button("Guardar juego"):
        if not name or not rules:
            st.warning("Rellena el nombre y las reglas del juego")
        else:
            save_game(user, name, rules)
            st.success(f"Juego '{name}' guardado ✅")

    # ---------------------------------------------
    # Mostrar juegos guardados
    # ---------------------------------------------
    st.subheader("Tus juegos guardados")
    games = st.session_state.get("games", {}).get(user, load_games(user))
    for g in games:
        st.markdown(f"**{g['name']}**: {g['rules']}")
        if st.button(f"Explicar {g['name']}"):
            explanation = explain_game(g["rules"])
            st.info(explanation)

    # ---------------------------------------------
    # Probar jugada
    # ---------------------------------------------
    if games:
        selected_game = st.selectbox(
            "Selecciona un juego para probar jugada",
            [g['name'] for g in games]
        )
        move = st.text_input("Introduce la jugada")
        if st.button("Evaluar jugada"):
            rules_text = next(g["rules"] for g in games if g["name"] == selected_game)
            result = judge_move(rules_text, move)
            st.info(result)
