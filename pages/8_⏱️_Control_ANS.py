import streamlit as st

st.set_page_config(page_title="Control ANS", page_icon="⏱️", layout="wide")

st.title("⏱️ Control ANS")
st.subheader("Seguimiento de tiempos y cumplimiento")

st.markdown("""
## ¿Qué es?

Controla si una actividad se cumple dentro del tiempo definido.

## ¿Para qué sirve?

- Medir tiempos de atención
- Detectar retrasos
- Generar alertas
- Priorizar tareas

## Ejemplo real

- Fecha creación
- Fecha límite
- Fecha cierre
""")

st.divider()

st.markdown("## Lógica básica")

st.code("""
if fecha_cierre <= fecha_limite:
    estado = "Cumplido"
else:
    estado = "Vencido"
""", language="python")

st.info("💡 Práctica: crear un Excel o tabla con fechas y calcular estado ANS")