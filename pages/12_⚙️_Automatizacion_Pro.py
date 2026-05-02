import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import os

# =========================================
# CONFIGURACIÓN
# =========================================
st.set_page_config(page_title="Automatización Pro", layout="wide")

st.title("⚙️ Automatización - Nivel Profesional")
st.markdown("---")

# =========================================
# ¿QUÉ ES?
# =========================================
st.header("🧠 ¿Qué es Automatización?")

st.markdown("""
Automatizar es hacer que un proceso se ejecute solo, sin intervención manual.

👉 En tu contexto:
- Procesar archivos
- Actualizar base de datos
- Generar reportes
- Validar información

🔥 Pasas de:
"yo hago tareas"
👉 a:
"el sistema trabaja por mí"
""")

# =========================================
# ¿PARA QUÉ SIRVE?
# =========================================
st.header("🎯 ¿Para qué sirve en la vida real?")

st.markdown("""
- Eliminar tareas repetitivas
- Reducir errores humanos
- Aumentar velocidad
- Crear procesos tipo empresa

💼 Ejemplo real:
Subir archivo → limpiar → guardar → reportar → listo
""")

# =========================================
# DÓNDE LO USASTE
# =========================================
st.header("📍 ¿Dónde lo usaste tú?")

st.markdown("""
✔ Compresor PDF automático  
✔ Scripts de limpieza  
✔ Exportaciones a Excel  
✔ Flujo NEXUS (movimientos + cálculo)  

👉 Ya automatizas… ahora lo estructuramos PRO
""")

# =========================================
# FLUJO PROFESIONAL
# =========================================
st.header("🔥 Flujo profesional de automatización")

st.code("""
INPUT (archivo / DB / API)
    ↓
LIMPIEZA (Python / Pandas)
    ↓
VALIDACIÓN (QA)
    ↓
PROCESAMIENTO (reglas negocio)
    ↓
OUTPUT (Excel / DB / Dashboard)
""")

# =========================================
# EJEMPLO REAL COMPLETO
# =========================================
st.header("💻 Ejemplo real (flujo completo)")

# Crear conexión SQLite local
def get_connection():
    return sqlite3.connect("data/demo_automatizacion.db")

# Crear tabla si no existe
def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT,
            cantidad INTEGER,
            fecha TEXT
        )
    """)
    conn.commit()
    conn.close()

crear_tabla()

# Simulación de archivo de entrada
df_input = pd.DataFrame({
    "producto": ["A", "B", "C"],
    "cantidad": ["10", "20", "error"],
    "fecha": ["2025-01-01", "2025-01-02", "2025-01-03"]
})

st.subheader("📥 Datos de entrada")
st.dataframe(df_input)

# Limpieza
def limpiar_datos(df):
    df = df.copy()
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
    df = df.dropna()
    return df

df_limpio = limpiar_datos(df_input)

st.subheader("🧹 Datos limpios")
st.dataframe(df_limpio)

# Validación
errores = df_input[pd.to_numeric(df_input["cantidad"], errors="coerce").isna()]

if not errores.empty:
    st.error("❌ Registros inválidos detectados")
    st.dataframe(errores)

# Carga a DB
def guardar_db(df):
    conn = get_connection()
    df.to_sql("ventas", conn, if_exists="append", index=False)
    conn.close()

if st.button("🚀 Ejecutar automatización"):
    guardar_db(df_limpio)
    st.success("Proceso completado y guardado en base de datos")

# =========================================
# CHECKLIST
# =========================================
st.header("✅ Checklist profesional")

st.markdown("""
✔ Tengo input claro  
✔ Limpio datos  
✔ Valido errores  
✔ Aplico reglas negocio  
✔ Genero output  
✔ Registro resultados  
""")

# =========================================
# ERRORES COMUNES
# =========================================
st.header("❌ Errores comunes")

st.markdown("""
🔴 No validar datos  
🔴 Automatizar sin entender proceso  
🔴 No manejar errores  
🔴 No guardar logs  
🔴 Procesos manuales repetidos  

👉 Resultado:
Automatización frágil
""")

# =========================================
# PRÁCTICA
# =========================================
st.header("🧪 Cómo practicar")

st.markdown("""
Ejercicio PRO:

1. Crear carpeta "input"
2. Leer archivo Excel
3. Limpiar datos
4. Guardar en SQLite
5. Generar reporte

👉 Objetivo:
Simular flujo empresarial
""")

# =========================================
# TIPS REALES
# =========================================
st.header("💡 Tips de trabajo real")

st.markdown("""
🔥 Automatiza lo repetitivo  
🔥 Siempre valida datos  
🔥 Guarda historial  
🔥 Usa logs  
🔥 Diseña procesos claros  

👉 Automatización = eficiencia real
""")

# =========================================
# BONUS
# =========================================
st.header("🚀 BONUS")

st.markdown("""
Siguiente nivel:

- Jobs programados (Task Scheduler / cron)
- Integración APIs
- Automatización en la nube
- ETL profesional

🔥 Nivel empresa real
""")