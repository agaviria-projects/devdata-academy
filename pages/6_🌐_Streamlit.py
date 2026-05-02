import streamlit as st
import pandas as pd
import time

# =========================================
# CONFIGURACIÓN
# =========================================
st.set_page_config(page_title="Streamlit Pro", layout="wide")

st.title("🧠 Streamlit PRO - Nivel Profesional")
st.markdown("---")

# =========================================
# ¿QUÉ ES?
# =========================================
st.header("🧠 ¿Qué es Streamlit PRO?")

st.markdown("""
Streamlit es una herramienta para crear aplicaciones web con Python.

👉 Nivel PRO significa:
- Controlar el estado (session_state)
- Evitar recargas innecesarias
- Diseñar UI profesional
- Manejar formularios correctamente
- Optimizar rendimiento

🔥 Esto es lo que convierte tu app en algo tipo:
NEXUS / ERP / Dashboard real
""")

# =========================================
# DÓNDE LO USASTE
# =========================================
st.header("📍 ¿Dónde lo usaste?")

st.markdown("""
✔ NEXUS (Kardex completo)  
✔ DevData Academy  
✔ Dashboards internos  
✔ Scripts con interfaz  

👉 Ya lo usas… ahora lo vas a dominar
""")

# =========================================
# SESSION STATE (CLAVE)
# =========================================
st.header("🔥 session_state (EL CEREBRO)")

st.markdown("""
Streamlit se recarga en cada interacción.

👉 session_state permite:
- Guardar variables
- Mantener filtros
- Controlar botones
- Evitar que todo se reinicie

🔥 Sin esto → app inestable
🔥 Con esto → app profesional
""")

# Inicialización segura
if "contador" not in st.session_state:
    st.session_state.contador = 0

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Incrementar"):
        st.session_state.contador += 1

with col2:
    st.write("Valor actual:")
    st.success(st.session_state.contador)

# =========================================
# FORMULARIOS (PRO)
# =========================================
st.header("📋 Formularios PRO")

st.markdown("""
🔥 PROBLEMA COMÚN:
Los inputs ejecutan todo el script

🔥 SOLUCIÓN:
Usar st.form()
""")

with st.form("formulario_demo"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0)

    enviar = st.form_submit_button("Guardar")

    if enviar:
        st.success(f"Guardado: {nombre} - {edad}")

# =========================================
# CACHE (RENDIMIENTO)
# =========================================
st.header("⚡ Cache (rendimiento)")

st.markdown("""
Evita recalcular funciones pesadas.

🔥 Ideal para:
- SQL
- Pandas
- APIs
""")

@st.cache_data
def cargar_datos():
    time.sleep(2)
    df = pd.DataFrame({
        "Producto": ["A", "B", "C"],
        "Stock": [10, 20, 30]
    })
    return df

if st.button("Cargar datos (cache)"):
    df = cargar_datos()
    st.dataframe(df)

# =========================================
# CONTROL DE FLUJO
# =========================================
st.header("🧭 Control de flujo")

st.markdown("""
🔥 Clave para apps grandes

Evita ejecutar todo siempre
""")

opcion = st.selectbox("Selecciona vista", ["Inicio", "Análisis"])

if opcion == "Inicio":
    st.info("Vista inicial")

elif opcion == "Análisis":
    st.success("Vista de análisis cargada")

# =========================================
# UI PROFESIONAL
# =========================================
st.header("🎨 UI Profesional")

st.markdown("""
Tips reales:
- Usa columnas
- Usa contenedores
- Usa colores
- Usa títulos claros
""")

col1, col2, col3 = st.columns(3)

col1.metric("Ventas", "100", "+10")
col2.metric("Stock", "50", "-5")
col3.metric("Clientes", "20", "+2")

# =========================================
# ERRORES COMUNES
# =========================================
st.header("❌ Errores comunes")

st.markdown("""
🔴 No usar session_state  
🔴 Recargar todo sin control  
🔴 No usar formularios  
🔴 Código desordenado  
🔴 Mezclar lógica con UI  

👉 Resultado:
App lenta o inestable
""")

# =========================================
# CHECKLIST
# =========================================
st.header("✅ Checklist PRO")

st.markdown("""
✔ Uso session_state  
✔ Uso formularios  
✔ Uso cache  
✔ Separo lógica y UI  
✔ Evito recargas innecesarias  
✔ Diseño limpio  
""")

# =========================================
# CÓDIGO REAL (ESTRUCTURA)
# =========================================
st.header("💻 Estructura real (tipo NEXUS)")

st.code("""
modules/
    database.py
    logic.py

ui/
    forms.py
    tables.py

app.py
""")

# =========================================
# PRÁCTICA
# =========================================
st.header("🧪 Cómo practicar")

st.markdown("""
Ejercicio PRO:

1. Crear formulario
2. Guardar datos en session_state
3. Mostrar tabla
4. Filtrar datos sin recargar

👉 Objetivo:
Pensar como sistema
""")

# =========================================
# TIPS REALES
# =========================================
st.header("💡 Tips de trabajo real")

st.markdown("""
🔥 Usa session_state para TODO lo dinámico  
🔥 Nunca dependas solo de inputs  
🔥 Controla cuándo ejecutar consultas  
🔥 Divide archivos (no todo en app.py)  
🔥 Piensa en usuario final  

👉 Streamlit simple → demo  
👉 Streamlit PRO → sistema real
""")

# =========================================
# BONUS
# =========================================
st.header("🚀 BONUS")

st.markdown("""
Siguiente nivel:

- AgGrid
- Autenticación
- Multiusuario
- Logs
- Deploy avanzado

🔥 Eso ya es nivel empresa
""")