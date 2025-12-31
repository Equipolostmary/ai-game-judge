import streamlit as st
from judge.judge_core import judge_game
from PIL import Image
import base64

# ---------- CONFIG ----------
st.set_page_config(
    page_title="AI Game Judge",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e0e0e;
    color: #eaeaea;
}
h1, h2, h3 {
    text-align: center;
}
.judge-box {
    border: 2px solid #444;
    padding: 20px;
    border-radius: 10px;
    background-color: #141414;
}
.verdict {
    font-size: 18px;
    font-weight: bold;
    color: #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# ---------- JUEZ ----------
st.markdown("<h1>⚖️ AI GAME JUDGE</h1>", unsafe_allow_html=True)
st.markdown("<h3>El juez decide. No discute.</h3>", unsafe_allow_html=True)

try:
    judge_img = Image.open("assets/judge.png")
    st.image(judge_img, width=250)
except:
    st.warning("Imagen del juez no encontrada")

st.divider()

# ---------- ESTADO ----------
if "rules_text" not in st.session_state:
    st.session_state.rules_text = ""

if "game_name" not in st.session_state:
    st.session_state.game_name = ""

# ---------- SUBIR INSTRUCCIONES ----------
st.markdown("## 📜 Instrucciones del juego")

st.session_state.game_name = st.text_input(
    "Nombre del juego",
    placeholder="Ej: Monopoly, Poker, Uno..."
)

uploaded_files = st.file_uploader(
    "Sube una o varias fotos de las instrucciones",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    st.session_state.rules_text = "Instrucciones proporcionadas por imágenes."
    st.success(f"{len(uploaded_files)} imagen(es) cargadas correctamente")

# ---------- ZONA JUGAR ----------
st.divider()
st.markdown("## 🎮 JUGAR")

player_action = st.text_area(
    "Describe la jugada / situación",
    height=150,
    placeholder="Ej: El jugador A roba dos cartas cuando no le tocaba..."
)

# ---------- VEREDICTO ----------
if st.button("⚖️ DICTAR VEREDICTO"):
    if not st.session_state.game_name or not player_action:
        st.error("Falta el nombre del juego o la acción.")
    else:
        with st.spinner("El juez está deliberando..."):
            verdict = judge_game(
                st.session_state.game_name,
                st.session_state.rules_text,
                player_action
            )

        st.markdown("""
        <div class="judge-box">
        <p class="verdict">VEREDICTO</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(verdict)
