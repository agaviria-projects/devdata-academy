import streamlit as st
import sqlite3
import pandas as pd

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Evaluador SQL PRO", layout="wide")

st.title("🧠 Evaluador SQL PRO (Teoría + Práctica)")
st.markdown("---")

# =========================================
# DB DE PRÁCTICA
# =========================================
def get_connection():
    return sqlite3.connect("data/sql_eval.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ciudad TEXT,
        edad INTEGER
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM clientes")
    if cursor.fetchone()[0] == 0:
        datos = [
            ("Juan", "Medellín", 30),
            ("Ana", "Bogotá", 25),
            ("Carlos", "Cali", 40),
            ("Luisa", "Medellín", 35)
        ]
        cursor.executemany(
            "INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)", datos
        )

    conn.commit()
    conn.close()

init_db()

# =========================================
# PARTE 1: TEST
# =========================================
st.header("📚 Parte 1 - Teoría")

pregunta = "¿Cuál consulta filtra clientes de Medellín?"

opciones = [
    "SELECT * FROM clientes WHERE ciudad = Medellín",
    "SELECT * FROM clientes WHERE ciudad = 'Medellín'",
    "SELECT Medellín FROM clientes"
]

respuesta_usuario = st.radio("Selecciona una opción:", opciones)

respuesta_correcta = "SELECT * FROM clientes WHERE ciudad = 'Medellín'"

puntaje_test = 0

if respuesta_usuario == respuesta_correcta:
    st.success("Correcto ✅")
    puntaje_test = 1
else:
    st.error("Incorrecto ❌")

st.markdown("---")

# =========================================
# PARTE 2: PRÁCTICA SQL
# =========================================
st.header("💻 Parte 2 - Práctica SQL")

st.markdown("""
🎯 Reto:

👉 Escribe una consulta que muestre SOLO los clientes de Medellín
""")

query = st.text_area("Escribe tu SQL aquí:")

# Resultado esperado
query_correcta = "SELECT * FROM clientes WHERE ciudad = 'Medellín'"

conn = get_connection()

puntaje_sql = 0

if st.button("🚀 Evaluar SQL"):

    try:
        # Ejecutar query usuario
        df_user = pd.read_sql(query, conn)

        # Ejecutar query correcta
        df_correcto = pd.read_sql(query_correcta, conn)

        # Comparar resultados
        if df_user.equals(df_correcto):
            st.success("✅ Consulta correcta")
            puntaje_sql = 1
        else:
            st.warning("⚠️ La consulta ejecuta pero no es correcta")
            st.write("👉 Resultado esperado:")
            st.dataframe(df_correcto)

        st.subheader("📊 Tu resultado:")
        st.dataframe(df_user)

    except Exception as e:
        st.error("❌ Error en la consulta")
        st.code(str(e))

    conn.close()

# =========================================
# RESULTADO FINAL
# =========================================
st.markdown("---")
st.header("🎯 Resultado final")

total = puntaje_test + puntaje_sql

st.write(f"Puntaje total: {total} / 2")

if total == 2:
    st.success("🔥 Nivel PRO")
elif total == 1:
    st.info("👍 Buen trabajo, pero puedes mejorar")
else:
    st.warning("⚠️ Reforzar conceptos")