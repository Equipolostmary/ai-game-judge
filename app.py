import streamlit as st
from utils.storage import save_game, load_games
from judge.judge_core import explain_game, judge_move

st.set_page_config(page_title="El Juez de Juegos", layout="wide")
st.title("El Juez de Juegos")

# ---------------------------------------------
# Registro de usuario
# ---------------------------------------------
if "user" not in st.session_state or not st.session_state.user:
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    st.session_state.user_input = st.text_input(
        "Introduce tu nombre de usuario:",
        value=st.session_state.user_input,
        key="user_input_field"
    )
    if st.session_state.user_input:
        st.session_state.user = st.session_state.user_input

# Continuar solo si hay usuario
if "user" in st.session_state and st.session_state.user:
    user = st.session_state.user
    st.subheader(f"Bienvenido, {user}!")

    # ---------------------------------------------
    # Crear juego nuevo
    # ---------------------------------------------
    if "new_game_name" not in st.session_state:
        st.session_state.new_game_name = ""
    if "new_game_rules" not in st.session_state:
        st.session_state.new_game_rules = ""

    st.session_state.new_game_name = st.text_input(
        "Nombre del juego",
        value=st.session_state.new_game_name,
        key="new_game_name_field"
    )
    st.session_state.new_game_rules = st.text_area(
        "Reglas del juego",
        value=st.session_state.new_game_rules,
        key="new_game_rules_field"
    )

    if st.button("Guardar juego", key="save_game_button"):
        if not st.session_state.new_game_name or not st.session_state.new_game_rules:
            st.warning("Rellena el nombre y las reglas del juego")
        else:
            save_game(
                user,
                st.session_state.new_game_name,
                st.session_state.new_game_rules
            )
            st.success(f"Juego '{st.session_state.new_game_name}' guardado ✅")
            # Limpiar inputs
            st.session_state.new_game_name = ""
            st.session_state.new_game_rules = ""

    # ---------------------------------------------
    # Mostrar juegos guardados
    # ---------------------------------------------
    st.subheader("Tus juegos guardados")
    games = st.session_state.get("games", {}).get(user, load_games(user))
    for idx, g in enumerate(games):
        st.markdown(f"**{g['name']}**: {g['rules']}")
        if st.button(f"Explicar {g['name']}", key=f"explain_{idx}"):
            explanation = explain_game(g["rules"])
            st.info(explanation)

    # ---------------------------------------------
    # Probar jugada
    # ---------------------------------------------
    if games:
        game_names = [g['name'] for g in games]
        if "selected_game_idx" not in st.session_state:
            st.session_state.selected_game_idx = 0
        st.session_state.selected_game_idx = st.selectbox(
            "Selecciona un juego para probar jugada",
            range(len(game_names)),
            format_func=lambda i: game_names[i],
            index=st.session_state.selected_game_idx,
            key="select_game_box"
        )

        if "move_input" not in st.session_state:
            st.session_state.move_input = ""

        st.session_state.move_input = st.text_input(
            "Introduce la jugada",
            value=st.session_state.move_input,
            key="move_input_field"
        )

        if st.button("Evaluar jugada", key="evaluate_move_button"):
            selected_game = games[st.session_state.selected_game_idx]
            result = judge_move(selected_game["rules"], st.session_state.move_input)
            st.info(result)
            st.session_state.move_input = ""
