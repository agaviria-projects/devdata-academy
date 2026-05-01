import streamlit as st

st.set_page_config(
    page_title="DevData Academy",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 DevData Academy")
st.subheader("Mi tutor personal de Python, SQL, Power BI, Excel, Streamlit y NEXUS")

st.markdown("""
Bienvenido a tu app personal de aprendizaje técnico.

Aquí vas a documentar:

- Lo que aprendiste
- Cómo lo aplicaste
- Qué errores solucionaste
- Qué código puedes reutilizar
- Qué prácticas puedes repetir
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🐍 Python\n\nLimpieza, automatización, pandas, openpyxl, scripts.")

with col2:
    st.success("🗄️ SQL\n\nConsultas, joins, agrupaciones, validaciones y bases de datos.")

with col3:
    st.warning("📊 Power BI\n\nDAX, modelo estrella, dashboards y storytelling.")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("📘 Excel\n\nPower Query, tablas, macros, fórmulas y dashboards.")

with col5:
    st.success("📦 NEXUS / Kardex\n\nReglas de negocio, seriales, reintegros, stock y trazabilidad.")

with col6:
    st.warning("🌐 Streamlit\n\nApps web, formularios, menús, tablas y despliegue.")