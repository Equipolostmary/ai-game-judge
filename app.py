import streamlit as st
from utils.storage import save_game, load_games
from judge.judge_core import explain_game, judge_move

st.title("El Juez de Juegos")

# Usuario (simulado para pruebas)
if "user" not in st.session_state:
    st.session_state.user = st.text_input("Nombre de usuario:")

user = st.session_state.user

st.subheader("Crear un juego nuevo")
name = st.text_input("Nombre del juego")
rules = st.text_area("Reglas del juego")

if st.button("Guardar juego"):
    if not name or not rules:
        st.warning("Rellena el nombre y las reglas del juego")
    else:
        save_game(user, name, rules)
        st.success(f"Juego '{name}' guardado ✅")
        st.experimental_rerun()  # fuerza recarga para actualizar la lista

st.subheader("Tus juegos guardados")
games = st.session_state.get("games", {}).get(user, [])
for g in games:
    st.markdown(f"**{g['name']}**: {g['rules']}")
    if st.button(f"Explicar {g['name']}"):
        explanation = explain_game(g["rules"])
        st.info(explanation)
