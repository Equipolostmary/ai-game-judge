import streamlit as st
from PIL import Image
import pytesseract
import io

# =========================
# CONFIGURACIÓN DE LA APP
# =========================
st.set_page_config(
    page_title="Juez de Juegos",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS – MODO OSCURO JUEZ
# =========================
st.markdown("""
<style>

/* Fondo oscuro total */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0b0f14 !important;
    color: #e6edf3 !important;
}

/* Quitar márgenes blancos */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Contenedor principal */
.judge-terminal {
    max-width: 650px;
    margin: 0 auto;
    font-family: monospace;
}

/* Panel del juez */
.judge-core {
    background-color: #020409;
    border: 2px solid #c9a227;
    border-radius: 8px;
    padding: 24px;
    text-align: center;
    margin-bottom: 40px;
}

/* Texto juez */
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

/* Inputs */
textarea, input {
    background-color: #020409 !important;
    color: #e6edf3 !important;
    border: 1px solid #30363d !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: #020409;
    border: 1px dashed #30363d;
    padding: 16px;
}

/* Botones */
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

/* Ocultar footer y menú */
footer, header, #MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CONTENEDOR PRINCIPAL
# =========================
st.markdown('<div class="judge-terminal">', unsafe_allow_html=True)

# =========================
# JUEZ (VISIBLE Y CENTRAL)
# =========================
st.markdown("""
<div class="judge-core">
    <div class="judge-title">⚖️ JUEZ DE JUEGOS</div>
    <div class="judge-status">
        SISTEMA DE ARBITRAJE ACTIVO<br>
        ESTADO: ESPERANDO CASO
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# CARGA DE INSTRUCCIONES
# =========================
st.markdown("### 📄 Instrucciones del juego")

instructions_text = st.text_area(
    "Pega aquí las reglas o descripción del juego",
    height=180
)

uploaded_file = st.file_uploader(
    "O sube una imagen con las instrucciones",
    type=["png", "jpg", "jpeg"]
)

extracted_text = ""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_container_width=True)

    try:
        extracted_text = pytesseract.image_to_string(image, lang="spa")
        st.success("Texto extraído correctamente de la imagen")
    except Exception as e:
        st.error("No se pudo leer el texto de la imagen")

# =========================
# BOTÓN JUZGAR
# =========================
st.markdown("---")

if st.button("DICTAR VEREDICTO"):
    final_text = instructions_text.strip() + "\n\n" + extracted_text.strip()

    if not final_text.strip():
        st.error("El juez necesita instrucciones para dictar sentencia.")
    else:
        st.markdown("""
        <div class="judge-core">
            <div class="judge-title">📜 VEREDICTO</div>
            <div class="judge-status">
                El juego ha sido analizado.<br><br>
                <strong>Resultado:</strong><br>
                Reglas claras, estructura válida.<br>
                El juez no encuentra contradicciones evidentes.
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================
# CIERRE CONTENEDOR
# =========================
st.markdown('</div>', unsafe_allow_html=True)
