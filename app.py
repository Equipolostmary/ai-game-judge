import streamlit as st
from utils.storage import save_game, load_games
from judge.judge_core import explain_game

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="El Juez de Juegos",
    layout="centered"
)

st.title("🎲 El Juez de Juegos")
st.caption("Tu árbitro inteligente para juegos de mesa")

# ---------------- USUARIO ----------------
if "user" not in st.session_state:
    st.session_state.user = ""

if st.session_state.user == "":
    st.subheader("👤 Identifícate para empezar")
    username = st.text_input("Nombre de usuario")
    if st.button("Continuar"):
        if username.strip() == "":
            st.warning("Introduce un nombre de usuario")
        else:
            st.session_state.user = username.strip()
            st.rerun()
    st.stop()

user = st.session_state.user

st.success(f"Bienvenido, **{user}**")

# ---------------- CREAR JUEGO ----------------
st.divider()
st.header("➕ Añadir un juego")

game_name = st.text_input("Nombre del juego")

st.subheader("Reglas del juego")

rules_text = st.text_area(
    "Escribe las reglas aquí (opcional)",
    height=150
)

uploaded_file = st.file_uploader(
    "O sube las instrucciones del juego (TXT, PDF o DOCX)",
    type=["txt", "pdf", "docx"]
)

final_rules = ""

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        final_rules = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        import pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            final_rules = "\n".join(
                page.extract_text() or "" for page in pdf.pages
            )

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        from docx import Document
        doc = Document(uploaded_file)
        final_rules = "\n".join(p.text for p in doc.paragraphs)

else:
    final_rules = rules_text

if st.button("💾 Guardar juego"):
    if game_name.strip() == "" or final_rules.strip() == "":
        st.warning("Debes indicar el nombre del juego y sus reglas")
    else:
        save_game(user, game_name.strip(), final_rules.strip())
        st.success(f"Juego **{game_name}** guardado correctamente")
        st.rerun()

# ---------------- JUEGOS GUARDADOS ----------------
st.divider()
st.header("📚 Tus juegos")

games = load_games(user)

if not games:
    st.info("Aún no has guardado ningún juego")
else:
    for idx, game in enumerate(games):
        with st.expander(f"🎮 {game['name']}"):
            st.markdown("**Reglas:**")
            st.write(game["rules"][:500] + ("..." if len(game["rules"]) > 500 else ""))

            if st.button(
                f"🧠 Explícame cómo se juega",
                key=f"explain_{idx}"
            ):
                with st.spinner("El juez está pensando..."):
                    explanation = explain_game(game["rules"])
                st.success("📖 Explicación rápida")
                st.write(explanation)
