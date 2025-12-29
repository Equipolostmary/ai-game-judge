import streamlit as st
from utils.storage import save_game, load_games, check_global_game
from judge.judge_core import explain_game, judge_move
import io
from docx import Document

st.set_page_config(page_title="El Juez de Juegos", layout="wide")
st.title("El Juez de Juegos")

# --------------------------
# Registro de usuario
# --------------------------
if "user" not in st.session_state:
    st.session_state.user = ""
    st.session_state.user_set = False

if not st.session_state.user_set:
    st.session_state.user = st.text_input("Introduce tu nombre de usuario:")
    if st.button("Continuar"):
        if st.session_state.user.strip() == "":
            st.warning("Debes introducir un nombre de usuario")
        else:
            st.session_state.user_set = True
    st.stop()

user = st.session_state.user
st.subheader(f"Bienvenido, {user}!")

# --------------------------
# Crear juego nuevo
# --------------------------
if "new_game_name" not in st.session_state:
    st.session_state.new_game_name = ""
if "new_game_rules" not in st.session_state:
    st.session_state.new_game_rules = ""

st.session_state.new_game_name = st.text_input(
    "Nombre del juego",
    value=st.session_state.new_game_name,
    key="new_game_name_field"
)

# Subida de archivo opcional
uploaded_file = st.file_uploader("Sube un archivo con las reglas (TXT o DOCX)", type=["txt", "docx"])

rules_text = ""
if uploaded_file:
    if uploaded_file.type == "text/plain":
        rules_text = uploaded_file.getvalue().decode("utf-8")
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(io.BytesIO(uploaded_file.read()))
        rules_text = "\n".join([p.text for p in doc.paragraphs])
else:
    st.session_state.new_game_rules = st.text_area(
        "Escribe las reglas del juego (si no subes archivo)",
        value=st.session_state.new_game_rules,
        key="new_game_rules_field"
    )
    rules_text = st.session_state.new_game_rules

if st.button("Guardar juego", key="save_game_button"):
    if not st.session_state.new_game_name.strip() or not rules_text.strip():
        st.warning("Debes indicar nombre y reglas del juego (archivo o manual)")
    else:
        global_game = check_global_game(st.session_state.new_game_name)
        if global_game:
            st.info(f"Este juego ya existe globalmente. Puedes usarlo para jugar como juez")
        else:
            save_game(user, st.session_state.new_game_name, rules_text)
            st.success(f"Juego '{st.session_state.new_game_name}' guardado ✅")
        st.session_state.new_game_name = ""
        st.session_state.new_game_rules = ""

# --------------------------
# Mostrar juegos guardados
# --------------------------
st.subheader("Tus juegos guardados")
games = st.session_state.get("games", {}).get(user, load_games(user))
for idx, g in enumerate(games):
    st.markdown(f"**{g['name']}**:")
    if st.button(f"Explicar {g['name']}", key=f"explain_{idx}"):
        explanation = explain_game(g["rules"])
        st.info(explanation)

# --------------------------
# Probar jugada
# --------------------------
if games:
    game_names = [g['name'] for g in games]
    if "selected_game_idx" not in st.session_state:
        st.session_state.selected_game_idx = 0
    st.session_state.selected_game_idx = st.selectbox(
        "Selecciona un juego para probar jugada",
        range(len(game_names)),
        format_func=lambda i: game_names[i],
        index=st.session_state.selected_game_idx,
        key="select_game_box"
    )

    if "move_input" not in st.session_state:
        st.session_state.move_input = ""

    st.session_state.move_input = st.text_input(
        "Introduce la jugada",
        value=st.session_state.move_input,
        key="move_input_field"
    )

    if st.button("Evaluar jugada", key="evaluate_move_button"):
        selected_game = games[st.session_state.selected_game_idx]
        result = judge_move(selected_game["rules"], st.session_state.move_input)
        st.info(result)
        st.session_state.move_input = ""

# --------------------------
# Contador de partidas jugadas (simple)
# --------------------------
if "play_count" not in st.session_state:
    st.session_state.play_count = 0

st.session_state.play_count += 0  # solo para inicializar
st.sidebar.subheader("Partidas jugadas")
st.sidebar.write(st.session_state.play_count)
