import streamlit as st
import sqlite3
import pandas as pd

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Dashboard Progreso", layout="wide")

st.title("📊 Dashboard de Progreso y Ranking")
st.markdown("---")

# =========================================
# CONEXIÓN DB
# =========================================
def get_conn():
    return sqlite3.connect("data/entrenamiento.db")

conn = get_conn()

# =========================================
# CARGAR DATOS
# =========================================
df = pd.read_sql("SELECT * FROM progreso", conn)

if df.empty:
    st.warning("Aún no hay datos de usuarios")
    st.stop()

# =========================================
# LIMPIEZA Y ORDEN
# =========================================
df = df.sort_values(by="puntos", ascending=False)

# =========================================
# RANKING
# =========================================
st.header("🏆 Ranking de Usuarios")

df["ranking"] = range(1, len(df) + 1)

st.dataframe(df[["ranking", "usuario", "nivel", "puntos"]], use_container_width=True)

# =========================================
# TOP 3
# =========================================
st.header("🥇 Top 3")

top3 = df.head(3)

col1, col2, col3 = st.columns(3)

if len(top3) > 0:
    col1.metric("🥇 1er lugar", top3.iloc[0]["usuario"], top3.iloc[0]["puntos"])

if len(top3) > 1:
    col2.metric("🥈 2do lugar", top3.iloc[1]["usuario"], top3.iloc[1]["puntos"])

if len(top3) > 2:
    col3.metric("🥉 3er lugar", top3.iloc[2]["usuario"], top3.iloc[2]["puntos"])

# =========================================
# GRÁFICO DE PROGRESO
# =========================================
st.header("📈 Progreso por Usuario")

usuario_select = st.selectbox("Selecciona usuario", df["usuario"].unique())

df_user = df[df["usuario"] == usuario_select]

st.line_chart(df_user[["puntos"]])

# =========================================
# DETALLE USUARIO
# =========================================
st.header("👤 Detalle del Usuario")

st.write(df_user)

# =========================================
# INSIGHT AUTOMÁTICO
# =========================================
st.header("🧠 Insight automático")

top_user = df.iloc[0]["usuario"]

st.success(f"🔥 El usuario con mejor rendimiento es: {top_user}")

# =========================================
# REFRESH
# =========================================
if st.button("🔄 Actualizar datos"):
    st.experimental_rerun()

conn.close()