import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Analítica Avanzada", layout="wide")

st.title("📈 Analítica Avanzada de Aprendizaje")
st.markdown("---")

# =========================================
# DB
# =========================================
def get_conn():
    return sqlite3.connect("data/entrenamiento.db")

conn = get_conn()
c = conn.cursor()

# =========================================
# CREAR TABLA HISTORIAL
# =========================================
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

conn.commit()

# =========================================
# CARGAR DATOS
# =========================================
df = pd.read_sql("SELECT * FROM historial", conn)

if df.empty:
    st.warning("Aún no hay historial registrado")
    st.stop()

# =========================================
# FILTRO USUARIO
# =========================================
usuario = st.selectbox("Selecciona usuario", df["usuario"].unique())

df_user = df[df["usuario"] == usuario].copy()

# =========================================
# ORDENAR POR FECHA
# =========================================
df_user["fecha"] = pd.to_datetime(df_user["fecha"])
df_user = df_user.sort_values(by="fecha")

# =========================================
# KPIs
# =========================================
st.header("📊 Indicadores")

col1, col2, col3 = st.columns(3)

col1.metric("Intentos", len(df_user))
col2.metric("Nivel Máximo", df_user["nivel"].max())
col3.metric("Puntos Totales", df_user["puntos"].sum())

# =========================================
# GRÁFICO EVOLUCIÓN
# =========================================
st.header("📈 Evolución de Puntos")

st.line_chart(df_user.set_index("fecha")["puntos"])

# =========================================
# PROGRESO POR NIVEL
# =========================================
st.header("📚 Avance por Nivel")

nivel_counts = df_user["nivel"].value_counts().sort_index()

st.bar_chart(nivel_counts)

# =========================================
# TIPO DE ACTIVIDAD
# =========================================
st.header("⚙️ Tipo de Entrenamiento")

tipo_counts = df_user["tipo"].value_counts()

st.bar_chart(tipo_counts)

# =========================================
# TABLA DETALLE
# =========================================
st.header("📋 Historial detallado")

st.dataframe(df_user, use_container_width=True)

# =========================================
# INSIGHT AUTOMÁTICO
# =========================================
st.header("🧠 Insight automático")

ultimo_nivel = df_user["nivel"].iloc[-1]

if ultimo_nivel >= 4:
    st.success("🔥 Usuario en nivel avanzado")
elif ultimo_nivel >= 2:
    st.info("👍 Usuario en progreso")
else:
    st.warning("⚠️ Usuario en nivel inicial")

conn.close()