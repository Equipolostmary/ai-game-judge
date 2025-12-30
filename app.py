import streamlit as st
from PIL import Image
import uuid

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered"
)

# ---------------- ESTADO ----------------
if "games" not in st.session_state:
    st.session_state.games = {}

if "current_game" not in st.session_state:
    st.session_state.current_game = None

# ---------------- CSS ----------------
st.markdown("""
<style>
body { background-color: #0b0f14; color: #e6e6e6; }

.judge {
    border: 2px solid #f5c542;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    background: linear-gradient(180deg,#121821,#0b0f14);
    margin-bottom: 40px;
}

.judge h1 {
    color: #f5c542;
    letter-spacing: 3px;
}

.judge p {
    color: #9fb3c8;
}

.card {
    background-color: #0f1623;
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- JUEZ ----------------
st.markdown("""
<div class="judge">
    <h1>⚖️ JUEZ DE JUEGOS</h1>
    <p>Sistema de arbitraje imparcial</p>
    <p><b>Estado:</b> observando y aprendiendo</p>
</div>
""", unsafe_allow_html=True)

# ---------------- BIBLIOTECA ----------------
st.markdown("## 📚 Biblioteca de Juegos")

if st.session_state.games:
    selected = st.selectbox(
        "Selecciona un juego aprendido",
        list(st.session_state.games.keys())
    )
    st.session_state.current_game = selected
else:
    st.info("El juez aún no ha aprendido ningún juego.")

# ---------------- NUEVO JUEGO ----------------
st.markdown("## ➕ Enseñar un nuevo juego al juez")

name = st.text_input("Nombre del juego")

rules = st.text_area(
    "Reglas del juego",
    height=200,
    placeholder="Escribe las reglas o añade imágenes abajo"
)

images = st.file_uploader(
    "Sube una o varias imágenes con las instrucciones",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if images:
    st.markdown("### 📷 Instrucciones visuales")
    for img in images:
        st.image(Image.open(img), use_container_width=True)

if st.button("📖 Enseñar este juego al juez"):
    if not name:
        st.warning("El juez necesita el nombre del juego.")
    else:
        st.session_state.games[name] = {
            "rules": rules,
            "images": images,
            "id": str(uuid.uuid4())
        }
        st.session_state.current_game = name
        st.success(f"El juez ha aprendido el juego: {name}")

# ---------------- JUEGO ACTIVO ----------------
if st.session_state.current_game:
    game = st.session_state.games[st.session_state.current_game]

    st.markdown("## 🎮 Juego activo")
    st.markdown(f"**{st.session_state.current_game}**")

    if st.button("🧠 Explícale el juego al juez"):
        st.info("El juez ha comprendido las reglas y está listo para arbitrar.")

    if st.button("▶️ Empezar partida"):
        st.success("La partida ha comenzado. El juez está atento a cualquier disputa.")

    if st.button("⚖️ Solicitar veredicto"):
        st.warning("El juez emitirá un veredicto cuando la IA esté activada.")

# ---------------- PIE ----------------
st.markdown("""
<hr>
<p style="text-align:center;color:#6b7280;font-size:12px;">
JUEZ DE JUEGOS · AUTORIDAD FINAL · SIN DISCUSIÓN
</p>
""", unsafe_allow_html=True)
