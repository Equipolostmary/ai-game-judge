import streamlit as st
from PIL import Image

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="Juez de Juegos",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS — JUEZ OSCURO
# =========================
st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0b0f14 !important;
    color: #e6edf3 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.judge-terminal {
    max-width: 650px;
    margin: auto;
    font-family: monospace;
}

.judge-core {
    background-color: #020409;
    border: 2px solid #c9a227;
    border-radius: 8px;
    padding: 24px;
    text-align: center;
    margin-bottom: 40px;
}

.judge-title {
    color: #c9a227;
    font-weight: bold;
    letter-spacing: 3px;
    font-size: 18px;
}

.judge-status {
    color: #9ba3af;
    margin-top: 12px;
    font-size: 14px;
}

textarea, input {
    background-color: #020409 !important;
    color: #e6edf3 !important;
    border: 1px solid #30363d !important;
}

[data-testid="stFileUploader"] {
    background-color: #020409;
    border: 1px dashed #30363d;
    padding: 16px;
}

button {
    background-color: #020409 !important;
    color: #c9a227 !important;
    border: 1px solid #c9a227 !important;
    padding: 14px !important;
    width: 100% !important;
    font-weight: bold;
    letter-spacing: 1px;
}

button:hover {
    background-color: #c9a227 !important;
    color: #020409 !important;
}

footer, header, #MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CONTENEDOR
# =========================
st.markdown('<div class="judge-terminal">', unsafe_allow_html=True)

# =========================
# JUEZ VISIBLE
# =========================
st.markdown("""
<div class="judge-core">
    <div class="judge-title">⚖️ JUEZ DE JUEGOS</div>
    <div class="judge-status">
        SISTEMA DE ARBITRAJE ACTIVO<br>
        ESTADO: ESPERANDO INSTRUCCIONES
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# INSTRUCCIONES
# =========================
st.markdown("### 📄 INSTRUCCIONES DEL JUEGO")

instructions = st.text_area(
    "Escribe o pega aquí las reglas del juego",
    height=180
)

uploaded_image = st.file_uploader(
    "O sube una imagen con las instrucciones (solo visual)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Imagen aportada al juez", use_container_width=True)

# =========================
# VEREDICTO
# =========================
st.markdown("---")

if st.button("DICTAR VEREDICTO"):
    if not instructions.strip() and not uploaded_image:
        st.error("El juez no puede dictar sentencia sin pruebas.")
    else:
        st.markdown("""
        <div class="judge-core">
            <div class="judge-title">📜 VEREDICTO</div>
            <div class="judge-status">
                Caso recibido.<br><br>
                El juez ha analizado las instrucciones.<br>
                <strong>No se detectan incoherencias evidentes.</strong><br><br>
                Sentencia provisional emitida.
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
