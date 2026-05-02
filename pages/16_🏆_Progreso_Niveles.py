import streamlit as st
import sqlite3
import pandas as pd

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Progreso y Niveles", layout="wide")

st.title("🏆 Sistema de Niveles (SQL + Python)")
st.markdown("---")

# =========================================
# DB
# =========================================
def get_connection():
    return sqlite3.connect("data/progreso.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progreso (
        usuario TEXT PRIMARY KEY,
        puntos INTEGER,
        nivel INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()

# =========================================
# USUARIO
# =========================================
usuario = st.text_input("👤 Ingresa tu nombre:")

if not usuario:
    st.stop()

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM progreso WHERE usuario = ?", (usuario,))
data = cursor.fetchone()

if data is None:
    cursor.execute("INSERT INTO progreso VALUES (?, ?, ?)", (usuario, 0, 1))
    conn.commit()
    puntos, nivel = 0, 1
else:
    puntos, nivel = data[1], data[2]

st.subheader(f"📊 Nivel: {nivel} | Puntos: {puntos}")

st.markdown("---")

# =========================================
# NIVEL 1 (SQL)
# =========================================
if nivel == 1:
    st.header("🔥 Nivel 1 - SQL Básico")

    query = st.text_area("Escribe: Mostrar todos los clientes")

    if st.button("Evaluar Nivel 1"):

        if "select" in query.lower() and "*" in query:
            st.success("✅ Correcto")
            puntos += 10
            nivel = 2

            cursor.execute(
                "UPDATE progreso SET puntos=?, nivel=? WHERE usuario=?",
                (puntos, nivel, usuario)
            )
            conn.commit()
        else:
            st.error("❌ Incorrecto")

# =========================================
# NIVEL 2 (SQL)
# =========================================
elif nivel == 2:
    st.header("🔥 Nivel 2 - SQL Filtro")

    query = st.text_area("Filtra clientes de Medellín")

    if st.button("Evaluar Nivel 2"):

        if "where" in query.lower() and "medell" in query.lower():
            st.success("✅ Correcto")
            puntos += 10
            nivel = 3

            cursor.execute(
                "UPDATE progreso SET puntos=?, nivel=? WHERE usuario=?",
                (puntos, nivel, usuario)
            )
            conn.commit()
        else:
            st.error("❌ Incorrecto")

# =========================================
# NIVEL 3 (PYTHON)
# =========================================
elif nivel == 3:
    st.header("🔥 Nivel 3 - Python Básico")

    codigo = st.text_area("Escribe una función que sume 2 números")

    if st.button("Evaluar Nivel 3"):

        if "def" in codigo and "+" in codigo:
            st.success("✅ Correcto")
            puntos += 10
            nivel = 4

            cursor.execute(
                "UPDATE progreso SET puntos=?, nivel=? WHERE usuario=?",
                (puntos, nivel, usuario)
            )
            conn.commit()
        else:
            st.error("❌ Incorrecto")

# =========================================
# NIVEL 4 (PYTHON + PANDAS)
# =========================================
elif nivel == 4:
    st.header("🔥 Nivel 4 - Python Pandas")

    codigo = st.text_area("Filtra un DataFrame por una columna")

    if st.button("Evaluar Nivel 4"):

        if "df" in codigo and "[" in codigo:
            st.success("✅ Correcto")
            puntos += 10
            nivel = 5

            cursor.execute(
                "UPDATE progreso SET puntos=?, nivel=? WHERE usuario=?",
                (puntos, nivel, usuario)
            )
            conn.commit()
        else:
            st.error("❌ Incorrecto")

# =========================================
# FINAL
# =========================================
elif nivel >= 5:
    st.success("🏆 Has completado todos los niveles")
    st.write("Sigue creando nuevos retos 🔥")

conn.close()