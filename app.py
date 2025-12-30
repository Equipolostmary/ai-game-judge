import streamlit as st
from PIL import Image

# -------------------------
# CONFIGURACIÓN DE PÁGINA
# -------------------------
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------
# CSS PERSONALIZADO
# -------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0b0f14;
    color: #e6e6e6;
}

.main {
    background-color: #0b0f14;
}

.judge-box {
    border: 2px solid #f5c542;
    border-radius: 14px;
    padding: 25px;
    text-align: center;
    margin-bottom: 40px;
    background: radial-gradient(circle at top, #121821, #0b0f14);
}

.judge-title {
    font-size: 28px;
    font-weight: 700;
    color: #f5c542;
    letter-spacing: 2px;
}

.judge-sub {
    font-size: 14px;
    color: #9fb3c8;
    margin-top: 10px;
}

.section {
    margin-top: 40px;
}

textarea {
    background-color: #0f1623 !important;
    color: #ffffff !important;
    border: 1px solid #2a3446 !important;
}

.stButton>button {
    background-color: transparent;
    color: #f5c542;
    border: 2px solid #f5c542;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #f5c542;
    color: #000;
}

hr {
    border: 1px solid #1f2937;
}

.footer {
    text-align: center;
    font-size: 12px;
    color: #6b7280;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# CABECERA - EL JUEZ
# -------------------------
st.markdown("""
<div class="judge-box">
    <div class="judge-title">⚖️ JUEZ DE JUEGOS</div>
    <div class="judge-sub">
        SISTEMA DE ARBITRAJE NEUTRAL<br>
        ESTADO: ESPERANDO INSTRUCCIONES
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# INSTRUCCIONES DEL JUEGO
# -------------------------
st.markdown("## 📜 INSTRUCCIONES DEL JUEGO")

game_name = st.text_input("Nombre del juego")

rules_text = st.text_area(
    "Escribe o pega aquí las reglas del juego",
    height=220,
    placeholder="Ejemplo:\nCada jugador lanza un dado...\nEl juez decide empates..."
)

# -------------------------
# SUBIDA DE IMAGEN (SOLO VISUAL)
# -------------------------
st.markdown("### 📷 Imagen con las instrucciones (opcional)")
uploaded_image = st.file_uploader(
    "PNG, JPG o JPEG (solo referencia visual)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Imagen cargada (no se analiza automáticamente)", use_container_width=True)

# -------------------------
# ACCIÓN DEL JUEZ
# -------------------------
st.markdown("---")

if st.button("⚖️ DICTAR VEREDICTO"):
    if not game_name:
        st.warning("El juez necesita el nombre del juego.")
    elif not rules_text:
        st.warning("El juez necesita reglas para poder arbitrar.")
    else:
        st.info("""
        ⚠️ **Modo juez en espera**
        
        La lógica de IA está desactivada temporalmente  
        (saldo / API pendiente de configurar).
        
        La interfaz está lista.
        """)

        st.markdown("""
        **Resumen recibido por el juez:**
        - Juego: `{}`  
        - Reglas: {} caracteres
        """.format(game_name, len(rules_text)))

# -------------------------
# PIE
# -------------------------
st.markdown("""
<div class="footer">
    JUEZ DE JUEGOS · SISTEMA EXPERIMENTAL · SIN DISCUSIONES
</div>
""", unsafe_allow_html=True)
