import streamlit as st
from datetime import datetime
import uuid

from judge.judge_core import judge_event

# ================== CONFIG ==================
st.set_page_config(
    page_title="Juez de Juegos",
    page_icon="⚖️",
    layout="centered"
)

# ================== ESTADO ==================
if "games" not in st.session_state:
    st.session_state.games = {}

if "current_game" not in st.session_state:
    st.session_state.current_game = None

if "match_active" not in st.session_state:
    st.session_state.match_active = False

if "players" not in st.session_state:
    st.session_state.players = []

if "verdicts" not in st.session_state:
    st.session_state.verdicts = []

if "judge_state" not in st.session_state:
    st.session_state.judge_state = "OBSERVANDO"

# ================== CSS ==================
st.markdown("""
<style>
body { background-color:#0b0f14; color:#e6e6e6; }
hr { border-color:#1f2937; }

.judge {
    border:2px solid #f5c542;
    border-radius:16px;
    padding:22px;
    background:linear-gradient(180deg,#121821,#0b0f14);
    text-align:center;
    margin-bottom:24px;
}
.judge h1 { color:#f5c542; letter-spacing:3px; margin-bottom:6px; }
.judge .state { color:#9fb3c8; font-weight:600; }
.judge .voice {
    margin-top:10px;
    color:#c7d2fe;
    font-style:italic;
}

.card {
    background:#0f1623;
    border:1px solid #1f2937;
    border-radius:12px;
    padding:18px;
    margin-bottom:18px;
}

.terminal {
    background:#05080f;
    border:1px dashed #334155;
    border-radius:10px;
    padding:14px;
    font-family:monospace;
    color:#e5e7eb;
}

.verdict {
    border-left:4px solid #f5c542;
    background:#0b1220;
    padding:14px;
    border-radius:8px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# ================== JUEZ ==================
def judge_banner(state, message):
    st.markdown(f"""
    <div class="judge">
        <h1>⚖️ JUEZ DE JUEGOS</h1>
        <div class="state">Estado: {state}</div>
        <div class="voice">“{message}”</div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.match_active:
    judge_banner("PARTIDA ACTIVA", "Observo cada acción. Mi veredicto es definitivo.")
else:
    judge_banner("OBSERVANDO", "Estoy listo. Enseñadme el juego o iniciad la partida.")

# ================== BIBLIOTECA ==================
st.markdown("## 📚 Biblioteca de Juegos")

if st.session_state.games:
    st.session_state.current_game = st.selectbox(
        "Selecciona un juego",
        list(st.session_state.games.keys()),
        index=list(st.session_state.games.keys()).index(st.session_state.current_game)
        if st.session_state.current_game in st.session_state.games else 0
    )
else:
    st.info("El juez aún no ha aprendido ningún juego.")

# ================== ENSEÑAR JUEGO ==================
st.markdown("## 📖 Enseñar un juego al juez")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    name = st.text_input("Nombre del juego")
    rules = st.text_area(
        "Reglas del juego (texto)",
        height=180,
        placeholder="Introduce aquí las reglas completas del juego"
    )

    images = st.file_uploader(
        "Instrucciones visuales (puedes subir varias imágenes)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if images:
        st.markdown("**Previsualización:**")
        for img in images:
            st.image(img, use_container_width=True)

    if st.button("📥 Aprender este juego", use_container_width=True):
        if not name:
            st.warning("El juez exige un nombre de juego.")
        else:
            st.session_state.games[name] = {
                "id": str(uuid.uuid4()),
                "rules": rules,
                "images_count": len(images) if images else 0
            }
            st.session_state.current_game = name
            st.success(f"El juez ha aprendido **{name}**.")

    st.markdown('</div>', unsafe_allow_html=True)

# ================== CONFIG PARTIDA ==================
st.markdown("## 🎮 Configurar partida")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if not st.session_state.current_game:
        st.info("Selecciona o enseña un juego primero.")
    else:
        players_raw = st.text_input(
            "Jugadores (separados por coma)",
            placeholder="Ana, Luis, Marta"
        )

        if st.button("▶️ Iniciar partida", use_container_width=True):
            if not players_raw.strip():
                st.warning("El juez exige conocer a los jugadores.")
            else:
                st.session_state.players = [
                    p.strip() for p in players_raw.split(",") if p.strip()
                ]
                st.session_state.match_active = True
                st.session_state.verdicts = []
                st.success("Partida iniciada. El juez observa.")

    st.markdown('</div>', unsafe_allow_html=True)

# ================== PARTIDA ACTIVA ==================
if st.session_state.match_active:
    st.markdown("## 🧾 Sala del juez")

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"**Juego:** {st.session_state.current_game}")
        st.markdown(f"**Jugadores:** {', '.join(st.session_state.players)}")

        event = st.text_area(
            "Describe lo ocurrido",
            height=120,
            placeholder="Ej: Jugador 2 repite palabra fuera de turno."
        )

        if st.button("⚖️ Consultar al juez", use_container_width=True):
            if not event.strip():
                st.warning("El juez necesita hechos claros.")
            else:
                verdict_text = judge_event(
                    st.session_state.current_game,
                    st.session_state.games[st.session_state.current_game]["rules"],
                    event
                )

                verdict = {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "event": event,
                    "text": verdict_text
                }

                st.session_state.verdicts.append(verdict)

                st.markdown(f"""
                <div class="verdict">
                {verdict_text.replace(chr(10), "<br>")}
                </div>
                """, unsafe_allow_html=True)

        if st.button("⏹️ Finalizar partida", use_container_width=True):
            st.session_state.match_active = False
            st.info("Partida finalizada. El juez permanece atento.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ================== HISTORIAL ==================
    if st.session_state.verdicts:
        st.markdown("## 📜 Historial de veredictos")
        for v in reversed(st.session_state.verdicts):
            st.markdown(f"""
            <div class="terminal">
            [{v['time']}] HECHO: {v['event']}
            <br>→ {v['text']}
            </div>
            """, unsafe_allow_html=True)

# ================== PIE ==================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#6b7280;font-size:12px;'>"
    "JUEZ DE JUEGOS · AUTORIDAD FINAL · SIN DISCUSIÓN"
    "</p>",
    unsafe_allow_html=True
)
