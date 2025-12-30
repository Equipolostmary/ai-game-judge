import streamlit as st
from PIL import Image

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered"
)

# =========================
# CSS FUERTE (WRAPPER)
# =========================
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0e1117 !important;
}

.judge-terminal {
    background-color: #0e1117;
    color: #e6edf3;
    max-width: 650px;
    margin: auto;
    padding: 30px 10px;
}

.judge-box {
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    margin-bottom: 25px;
}

.judge-title {
    color: #c9a227;
    font-weight: bold;
    letter-spacing: 1px;
}

hr {
    border: none;
    border-top: 1px solid #30363d;
    margin: 30px 0;
}

input, textarea {
    background-color: #161b22 !important;
    color: #e6edf3 !important;
    border: 1px solid #30363d !important;
}

button {
    background-color: #161b22 !important;
    color: #c9a227 !important;
    border: 1px solid #30363d !important;
    width: 100%;
    padding: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# WRAPPER INICIO
# =========================
st.markdown('<div class="judge-terminal">', unsafe_allow_html=True)

# =========================
# JUEZ PRESENTE
# =========================
st.markdown("""
<div class="judge-box">
<span class="judge-title">⚖️ EL JUEZ</span><br><br>
Estoy presente.  
Esperando instrucciones.
</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>JUEZ DE JUEGOS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#9ba3af;'>Árbitro neutral · Sin discusiones</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# INSTRUCCIONES
# =========================
st.markdown("<h3>📜 INSTRUCCIONES DEL JUEGO</h3>", unsafe_allow_html=True)

game_name = st.text_input("Nombre del juego")

rules_text = st.text_area(
    "Reglas (opcional)",
    height=150,
    placeholder="Escribe o sube las reglas"
)

uploaded = st.file_uploader(
    "Sube instrucciones (foto, PDF, Word)",
    type=["jpg", "png", "pdf", "docx"]
)

if uploaded:
    st.markdown("""
    <div class="judge-box">
    El juez ha recibido las instrucciones.
    </div>
    """, unsafe_allow_html=True)

    if uploaded.type.startswith("image"):
        image = Image.open(uploaded)
        st.image(image, use_container_width=True)

if st.button("📘 ANALIZAR INSTRUCCIONES"):
    st.markdown("""
    <div class="judge-box">
    <span class="judge-title">JUEZ</span><br><br>
    Instrucciones analizadas.  
    Estoy preparado para juzgar.
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONSULTA
# =========================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3>🧠 CONSULTA AL JUEZ</h3>", unsafe_allow_html=True)

situation = st.text_area(
    "Describe exactamente lo ocurrido",
    height=160
)

if st.button("⚖️ EMITIR VEREDICTO"):
    st.markdown("""
    <div class="judge-box">
    <span class="judge-title">VEREDICTO</span><br><br>
    <b>NO VÁLIDO</b><br><br>
    La acción contradice las reglas proporcionadas.
    </div>
    """, unsafe_allow_html=True)

# =========================
# WRAPPER FIN
# =========================
st.markdown("</div>", unsafe_allow_html=True)
