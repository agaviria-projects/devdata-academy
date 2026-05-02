import streamlit as st

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Examen SQL", layout="wide")

st.title("📝 Examen SQL - Selección Múltiple")
st.markdown("---")

# =========================================
# PREGUNTAS
# =========================================
preguntas = [
    {
        "pregunta": "¿Qué consulta muestra todos los datos de la tabla clientes?",
        "opciones": [
            "SELECT clientes",
            "SELECT * FROM clientes",
            "GET ALL clientes",
            "SHOW clientes"
        ],
        "respuesta": "SELECT * FROM clientes"
    },
    {
        "pregunta": "¿Cuál consulta filtra clientes de Medellín?",
        "opciones": [
            "SELECT * FROM clientes WHERE ciudad = Medellín",
            "SELECT * FROM clientes WHERE ciudad = 'Medellín'",
            "FILTER ciudad Medellín",
            "SELECT ciudad Medellín"
        ],
        "respuesta": "SELECT * FROM clientes WHERE ciudad = 'Medellín'"
    },
    {
        "pregunta": "¿Qué hace DELETE?",
        "opciones": [
            "Modifica datos",
            "Elimina registros",
            "Crea tablas",
            "Ordena datos"
        ],
        "respuesta": "Elimina registros"
    },
    {
        "pregunta": "¿Qué consulta ordena por edad descendente?",
        "opciones": [
            "SELECT * FROM clientes ORDER edad DESC",
            "SELECT * FROM clientes ORDER BY edad DESC",
            "SORT clientes edad",
            "ORDER edad DESC"
        ],
        "respuesta": "SELECT * FROM clientes ORDER BY edad DESC"
    },
    {
        "pregunta": "¿Qué error tiene esta consulta? SELECT nombre clientes",
        "opciones": [
            "Falta FROM",
            "Falta WHERE",
            "Falta ORDER",
            "Está correcta"
        ],
        "respuesta": "Falta FROM"
    }
]

# =========================================
# SESSION STATE
# =========================================
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# =========================================
# MOSTRAR PREGUNTAS
# =========================================
st.header("📚 Responde las siguientes preguntas")

for i, p in enumerate(preguntas):
    st.subheader(f"{i+1}. {p['pregunta']}")

    opcion = st.radio(
        "Selecciona una opción:",
        p["opciones"],
        key=f"pregunta_{i}"
    )

    st.session_state.respuestas[i] = opcion

# =========================================
# BOTÓN EVALUAR
# =========================================
if st.button("🚀 Evaluar examen"):

    puntaje = 0

    st.markdown("---")
    st.header("📊 Resultados")

    for i, p in enumerate(preguntas):
        respuesta_usuario = st.session_state.respuestas.get(i)
        respuesta_correcta = p["respuesta"]

        if respuesta_usuario == respuesta_correcta:
            st.success(f"Pregunta {i+1}: Correcto ✅")
            puntaje += 1
        else:
            st.error(f"Pregunta {i+1}: Incorrecto ❌")
            st.write(f"👉 Respuesta correcta: {respuesta_correcta}")

    st.markdown("---")
    st.subheader(f"🎯 Puntaje final: {puntaje} / {len(preguntas)}")

    # Feedback inteligente
    if puntaje == len(preguntas):
        st.success("🔥 Excelente, nivel PRO")
    elif puntaje >= 3:
        st.info("👍 Buen nivel, sigue practicando")
    else:
        st.warning("⚠️ Necesitas reforzar conceptos básicos")

# =========================================
# RESET
# =========================================
if st.button("🔄 Reiniciar examen"):
    st.session_state.respuestas = {}
    st.experimental_rerun()