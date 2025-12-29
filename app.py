import streamlit as st
from judge.judge_core import judge_move, explain_game
from utils.storage import save_game, load_games

st.set_page_config(page_title="AI Game Judge", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None
if "current_game" not in st.session_state:
    st.session_state.current_game = None

if not st.session_state.user:
    st.title("🎲 AI Game Judge")
    username = st.text_input("Nombre de usuario")
    if st.button("Entrar"):
        st.session_state.user = username
        st.rerun()
    st.stop()

st.title("🎤 AI Game Judge")
st.write(f"Hola, **{st.session_state.user}**")

games = load_games(st.session_state.user)

st.subheader("🎮 Tus juegos")
game_names = [g["name"] for g in games]

selected = st.selectbox("Selecciona un juego", ["Crear nuevo"] + game_names)

if selected == "Crear nuevo":
    name = st.text_input("Nombre del juego")
    rules = st.text_area("Instrucciones del juego")
    if st.button("Guardar juego"):
        save_game(st.session_state.user, name, rules)
        st.success("Juego guardado")
        st.rerun()
else:
    st.session_state.current_game = selected

if st.session_state.current_game:
    game = next(g for g in games if g["name"] == st.session_state.current_game)

    st.subheader(f"📜 {game['name']}")

    if st.button("📖 Explícanos cómo se juega"):
        explanation = explain_game(game["rules"])
        st.info(explanation)

    st.divider()

    st.subheader("⚖️ Juez en acción")
    move = st.text_input("Introduce la jugada del jugador")

    if st.button("Evaluar"):
        verdict = judge_move(game["rules"], move)
        st.write(verdict)

