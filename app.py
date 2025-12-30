import streamlit as st
from PIL import Image
import io

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered"
)

# =========================
# CSS – JUEZ TERMINAL
# =========================
st.markdown("""
<style>
body { background-color: #0e1117; }
.block-container { max-width: 650px; padding-top: 30px; }
h1, h2, h3 { color: #e6edf3; text-align: center; letter-spacing: 1px; }
p, label { color: #9ba3af; text-align: center; }
hr { border: none; border-top: 1px solid #30363d; margin: 30px 0; }
.stButton > button {
    background-color: #161b22;
    color: #c9a227;
    border: 1px solid #30363d;
    font-size: 16px;
    padding: 14px;
    border-radius: 6px;
    width: 100%;
}
.stTextInput input, .stTextArea textarea {
    background-color: #161b22;
    color: #e6edf3;
    border: 1px solid #30363d;
}
.judge-box {
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    margin-bottom: 25px;
}
.judge-title { color: #c9a227; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# =========================
# CABECERA JUEZ
# =========================
st.title("⚖️ JUEZ DE JUEGOS")

st.markdown("""
<div class="judge-box">
<span class="judge-title">ESTADO DEL JUEZ</span><br>
El juez está atento. Esperando instrucciones.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# SECCIÓN JUEGO
# =========================
st.subheader("📜 INSTRUCCIONES DEL JUEGO")

game_name = st.text_input("Nombre del juego")

rules_text = st.text_area(
    "Escribe las reglas (opcional)",
    height=160,
    placeholder="Puedes escribirlas o subir un archivo debajo"
)

uploaded_file = st.file_uploader(
    "O sube las instrucciones",
    type=["jpg", "jpeg", "png", "pdf", "docx"]
)

if uploaded_file:
    st.success("📂 El juez ha recibido las instrucciones.")
    if uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Instrucciones recibidas", use_container_width=True)
    else:
        st.info("Archivo cargado. El juez lo analizará cuando active la IA.")

if st.button("📘 ANALIZAR INSTRUCCIONES"):
    if not rules_text and not uploaded_file:
        st.warning("El juez necesita reglas. Escríbelas o súbelas.")
    else:
        st.markdown("""
        <div class="judge-box">
        <span class="judge-title">JUEZ</span><br>
        He leído las instrucciones.  
        Estoy preparado para explicar el juego o juzgar situaciones.
        </div>
        """, unsafe_allow_html=True)

# =========================
# CONSULTA
# =========================
st.markdown("---")
st.subheader("🧠 CONSULTA AL JUEZ")

situation = st.text_area(
    "Describe exactamente lo ocurrido",
    height=160,
    placeholder="Ej: El jugador dijo una palabra que..."
)

if st.button("⚖️ EMITIR VEREDICTO"):
    if not situation:
        st.warning("Describe la situación con precisión.")
    else:
        st.markdown("""
        <div class="judge-box">
        <span class="judge-title">VEREDICTO</span><br><br>
        <b>NO VÁLIDO</b><br><br>
        Según las reglas proporcionadas, la acción no es aceptable.
        </div>
        """, unsafe_allow_html=True)

# =========================
# PIE
# =========================
st.markdown("---")
st.markdown("Juez de Juegos · Prototipo conceptual")
