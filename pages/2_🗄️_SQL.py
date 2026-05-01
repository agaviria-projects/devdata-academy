import streamlit as st

st.set_page_config(page_title="SQL", page_icon="🗄️", layout="wide")

st.title("🗄️ SQL")
st.subheader("Consultas, bases de datos y análisis empresarial")

# -----------------------------------------
# 1. ¿QUÉ ES?
# -----------------------------------------
st.markdown("## 📚 ¿Qué es SQL?")

st.markdown("""
SQL es el lenguaje que permite consultar, insertar y analizar datos en bases de datos.

Se usa en empresas para trabajar con información real.
""")

# -----------------------------------------
# 2. ¿PARA QUÉ SIRVE?
# -----------------------------------------
st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Consultar datos reales
- Validar información
- Crear reportes
- Preparar datos para Power BI
""")

# -----------------------------------------
# 3. ¿DÓNDE LO USÉ?
# -----------------------------------------
st.markdown("## 🏢 ¿Dónde lo usé?")

st.info("""
En proyectos de inventario, ventas y validación de datos antes de visualizarlos en Power BI.
""")

# -----------------------------------------
# 4. CÓDIGO
# -----------------------------------------
st.markdown("## 💻 Código básico")

st.code("""
SELECT *
FROM ventas;
""", language="sql")

# -----------------------------------------
# 5. PRÁCTICA
# -----------------------------------------
st.markdown("## 🧪 Práctica")

st.success("""
Crea una tabla llamada productos y consulta todos sus registros.
""")

# -----------------------------------------
# 6. ERRORES
# -----------------------------------------
st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No usar WHERE correctamente
- Olvidar JOIN entre tablas
- No validar datos antes de analizarlos
""")