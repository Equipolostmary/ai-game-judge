import streamlit as st

# =========================
# CONFIGURACIÓN BÁSICA
# =========================
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered"
)

# =========================
# CSS – ESTILO JUEZ TERMINAL
# =========================
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    max-width: 650px;
    padding-top: 40px;
}
h1, h2, h3 {
    color: #e6edf3;
    text-align: center;
    letter-spacing: 1px;
}
p, label {
    color: #9ba3af;
    text-align: center;
}
hr {
    border: none;
    border-top: 1px solid #30363d;
    margin: 30px 0;
}
.stButton > button {
    background-color: #161b22;
    color: #c9a227;
    border: 1px solid #30363d;
    font-size: 17px;
    padding: 14px;
    border-radius: 6px;
    width: 100%;
}
.stButton > button:hover {
    border-color: #c9a227;
}
.stTextInput input,
.stTextArea textarea {
    background-color: #161b22;
    color: #e6edf3;
    border: 1px solid #30363d;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CABECERA
# =========================
st.title("⚖️ JUEZ DE JUEGOS")
st.markdown("Árbitro neutral. Sin discusiones.")
st.markdown("---")

# =========================
# SECCIÓN: JUEGO
# =========================
st.subheader("🎲 JUEGO")

game_name = st.text_input(
    "Nombre del juego",
    placeholder="Ej: Palabras Encadenadas"
)

game_rules = st.text_area(
    "Reglas del juego",
    placeholder="Escribe aquí las reglas completas del juego...",
    height=200
)

if st.button("📘 EXPLICAR JUEGO"):
    if not game_rules.strip():
        st.warning("El juez necesita conocer las reglas.")
    else:
        st.markdown("---")
        st.subheader("📖 EXPLICACIÓN OFICIAL")
        st.markdown("""
        • **Objetivo:** Determinado por las reglas introducidas  
        • **Turnos:** Secuenciales  
        • **Prohibiciones:** Según reglas  
        • **Final:** Cuando se cumple la condición de victoria  

        *(La explicación automática se activará cuando conectemos la IA)*
        """)

# =========================
# SECCIÓN: CONSULTA AL JUEZ
# =========================
st.markdown("---")
st.subheader("🧠 CONSULTA AL JUEZ")

situation = st.text_area(
    "Describe la situación exacta",
    placeholder="Ej: El jugador dijo una palabra que empieza por la letra correcta pero es un nombre propio...",
    height=180
)

if st.button("⚖️ EMITIR VEREDICTO"):
    if not situation.strip():
        st.warning("El juez necesita hechos, no silencio.")
    else:
        st.markdown("---")
        st.subheader("⚖️ VEREDICTO")
        st.markdown("""
        **NO VÁLIDO**

        **Motivo:**  
        La situación descrita contradice las reglas del juego introducidas.

        *(El razonamiento automático se activará cuando conectemos la IA)*
        """)

# =========================
# PIE
# =========================
st.markdown("---")
st.markdown("Juez de Juegos · Prototipo")
