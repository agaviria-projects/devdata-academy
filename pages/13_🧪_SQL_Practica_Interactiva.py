import streamlit as st
import sqlite3
import pandas as pd

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="SQL Práctica", layout="wide")

st.title("🧪 Práctica SQL Interactiva (Modo Celular)")
st.markdown("---")

# =========================================
# CONEXIÓN
# =========================================
def get_connection():
    return sqlite3.connect("data/sql_practica.db")

# =========================================
# CREAR TABLA DEMO
# =========================================
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # 🔥 BORRAR TABLA SI EXISTE
    cursor.execute("DROP TABLE IF EXISTS clientes")

    # 🔥 CREAR NUEVA
    cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        ciudad TEXT,
        edad INTEGER
    )
    """)

    # 🔥 INSERTAR SIN TILDES
    datos = [
        ("Juan", "medellin", 30),
        ("Ana", "bogota", 25),
        ("Carlos", "cali", 40),
        ("Luisa", "medellin", 35)
    ]

    cursor.executemany(
        "INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)", datos
    )

    conn.commit()
    conn.close()

init_db()

# =========================================
# MOSTRAR TABLA
# =========================================
st.subheader("📊 Tabla de práctica")

conn = get_connection()
df = pd.read_sql("SELECT * FROM clientes", conn)
conn.close()

st.dataframe(df)

# =========================================
# INPUT SQL
# =========================================
st.subheader("✍️ Escribe tu consulta SQL")

query = st.text_area("Ejemplo: SELECT * FROM clientes", height=150)

# =========================================
# EJECUCIÓN
# =========================================
if st.button("🚀 Ejecutar consulta"):

    conn = get_connection()

    try:
        resultado = pd.read_sql(query, conn)

        st.success("✅ Consulta ejecutada correctamente")
        st.dataframe(resultado)

    except Exception as e:
        st.error("❌ Error en la consulta")
        st.code(str(e))

    finally:
        conn.close()

# =========================================
# RETOS
# =========================================
st.markdown("---")
st.header("🎯 Retos")

st.markdown("""
Prueba estas consultas:

1. Ver todos los datos  
👉 SELECT * FROM clientes  

2. Filtrar por ciudad  
👉 SELECT * FROM clientes WHERE ciudad = 'Medellin'  

3. Ordenar por edad  
👉 SELECT * FROM clientes ORDER BY edad DESC  

4. Eliminar un registro  
👉 DELETE FROM clientes WHERE nombre = 'Ana'  
""")

# =========================================
# VALIDACIÓN BÁSICA
# =========================================
st.markdown("---")
st.header("🧠 Tip automático")

if "select" in query.lower() and "from" not in query.lower():
    st.warning("⚠️ Te falta FROM en la consulta")

if "delete" in query.lower() and "where" not in query.lower():
    st.warning("⚠️ DELETE sin WHERE puede borrar todo")