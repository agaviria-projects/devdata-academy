import streamlit as st
import sqlite3
import pandas as pd
import io
import contextlib

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Modo Entrenamiento", layout="wide")

st.title("🎓 Modo Entrenamiento Completo")
st.markdown("---")

# =========================================
# DB PROGRESO
# =========================================
def get_conn():
    return sqlite3.connect("data/entrenamiento.db")

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS progreso (
        usuario TEXT PRIMARY KEY,
        nivel INTEGER,
        puntos INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()

from datetime import datetime

def guardar_historial(usuario, nivel, puntos, tipo):
    conn = sqlite3.connect("data/entrenamiento.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS historial (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        fecha TEXT,
        nivel INTEGER,
        puntos INTEGER,
        tipo TEXT
    )
    """)

    c.execute("""
    INSERT INTO historial (usuario, fecha, nivel, puntos, tipo)
    VALUES (?, ?, ?, ?, ?)
    """, (
        usuario,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        nivel,
        puntos,
        tipo
    ))

    conn.commit()
    conn.close()
# =========================================
# USUARIO
# =========================================
usuario = st.text_input("👤 Ingresa tu nombre")

if not usuario:
    st.stop()

conn = get_conn()
c = conn.cursor()

c.execute("SELECT * FROM progreso WHERE usuario=?", (usuario,))
data = c.fetchone()

if not data:
    c.execute("INSERT INTO progreso VALUES (?, ?, ?)", (usuario, 1, 0))
    conn.commit()
    nivel, puntos = 1, 0
else:
    nivel, puntos = data[1], data[2]

st.success(f"Nivel: {nivel} | Puntos: {puntos}")

st.markdown("---")

# =========================================
# DB SQL PRACTICA
# =========================================
def init_sql():
    conn = sqlite3.connect("data/sql_train.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ciudad TEXT,
        edad INTEGER
    )
    """)

    cur.execute("SELECT COUNT(*) FROM clientes")
    if cur.fetchone()[0] == 0:
        datos = [
            ("Juan", "Medellín", 30),
            ("Ana", "Bogotá", 25),
            ("Carlos", "Cali", 40),
            ("Luisa", "Medellín", 35)
        ]
        cur.executemany(
            "INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)", datos
        )

    conn.commit()
    conn.close()

init_sql()

# =========================================
# NIVEL 1 - SQL BÁSICO
# =========================================
if nivel == 1:
    st.header("🔥 Nivel 1 - SQL Básico")

    query = st.text_area("Mostrar todos los clientes")

    if st.button("Evaluar Nivel 1"):

        if "select" in query.lower() and "*" in query:
            
            st.success("✅ Correcto")

            nivel += 1
            puntos += 10

            guardar_historial(usuario, nivel, puntos, "SQL_BASICO")

            c.execute("UPDATE progreso SET nivel=?, puntos=? WHERE usuario=?",
                      (nivel, puntos, usuario))
            conn.commit()
        else:
            st.error("❌ Incorrecto")

# =========================================
# NIVEL 2 - SQL REAL
# =========================================
elif nivel == 2:
    st.header("🔥 Nivel 2 - SQL REAL")

    st.markdown("👉 Filtra clientes de Medellín")

    query = st.text_area("Escribe tu SQL")

    if st.button("Evaluar Nivel 2"):

        conn_sql = sqlite3.connect("data/sql_train.db")

        try:
            df_user = pd.read_sql(query, conn_sql)
            df_correct = pd.read_sql(
                "SELECT * FROM clientes WHERE ciudad='Medellín'", conn_sql
            )

            if df_user.equals(df_correct):
                
                st.success("✅ Correcto")

                nivel += 1
                puntos += 20

                guardar_historial(usuario, nivel, puntos, "SQL_REAL")   

                c.execute("UPDATE progreso SET nivel=?, puntos=? WHERE usuario=?",
                          (nivel, puntos, usuario))
                conn.commit()
            else:
                st.warning("⚠️ Resultado incorrecto")
                st.dataframe(df_correct)

            st.dataframe(df_user)

        except Exception as e:
            st.error("❌ Error en SQL")
            st.code(str(e))

        conn_sql.close()

# =========================================
# NIVEL 3 - PYTHON
# =========================================
elif nivel == 3:
    st.header("🔥 Nivel 3 - Python")

    codigo = st.text_area("Imprime 10 usando Python")

    if st.button("Evaluar Nivel 3"):

        salida = io.StringIO()

        try:
            with contextlib.redirect_stdout(salida):
                exec(codigo, {"__builtins__": {}})

            resultado = salida.getvalue()

            if "10" in resultado:
                
                st.success("✅ Correcto")

                nivel += 1
                puntos += 20

                guardar_historial(usuario, nivel, puntos, "PYTHON")

                c.execute("UPDATE progreso SET nivel=?, puntos=? WHERE usuario=?",
                          (nivel, puntos, usuario))
                conn.commit()
            else:
                st.warning("⚠️ Resultado incorrecto")

        except Exception as e:
            st.error("❌ Error en Python")
            st.code(str(e))

# =========================================
# FINAL
# =========================================
elif nivel >= 4:
    st.success("🏆 Has completado el entrenamiento inicial")

    st.markdown("""
    🔥 Ya sabes:
    - SQL práctico
    - Validación real
    - Python ejecutable
    
    👉 Nivel siguiente: PROYECTOS REALES
    """)

conn.close()