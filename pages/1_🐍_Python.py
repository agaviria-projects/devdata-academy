import streamlit as st

st.set_page_config(page_title="Python", page_icon="🐍", layout="wide")

st.title("🐍 Python")
st.subheader("Automatización, limpieza de datos y desarrollo de soluciones")

st.markdown("## 📚 ¿Qué es Python?")

st.markdown("""
Python es un lenguaje de programación usado para automatizar tareas, limpiar datos,
crear scripts, procesar archivos y construir aplicaciones.

Es muy usado en análisis de datos, inteligencia artificial, automatización y desarrollo web.
""")

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Automatizar tareas repetitivas
- Limpiar archivos Excel, CSV o TXT
- Conectar con bases de datos
- Crear reportes
- Generar gráficos
- Crear apps con Streamlit
""")

st.markdown("## 🏢 ¿Dónde lo usé?")

st.info("""
Lo he usado en procesos de limpieza de datos, automatización de archivos,
compresión de PDF, exportación a Excel y desarrollo de herramientas como NEXUS.
""")

st.markdown("## 📦 Librerías importantes")

st.markdown("""
- `pandas`: análisis y limpieza de datos
- `openpyxl`: trabajar con archivos Excel
- `matplotlib`: crear gráficos
- `streamlit`: crear aplicaciones web
- `sqlite3`: conectar con bases de datos SQLite
- `os`: trabajar con carpetas y archivos
""")

st.markdown("## 💻 Ejemplo básico")

st.code("""
import pandas as pd

df = pd.read_excel("ventas.xlsx")
df["total"] = df["cantidad"] * df["precio"]
print(df.head())
""", language="python")

st.markdown("## 🧪 Práctica")

st.success("""
Crea un archivo Excel con ventas, cárgalo con pandas y calcula una columna total.
""")

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No activar el entorno virtual
- No instalar librerías necesarias
- Confundir rutas de archivos
- No validar columnas antes de usarlas
- Guardar archivos con nombres diferentes a los esperados
""")