import streamlit as st

st.set_page_config(
    page_title="DevData Academy",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.card {
    height: 125px;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 14px;
    font-size: 15px;
    box-sizing: border-box;
}
.card h4 {
    margin-top: 0;
    margin-bottom: 14px;
}
.card-blue {
    background-color: #e8f2ff;
    color: #004b93;
}
.card-green {
    background-color: #e6f7ec;
    color: #006b2f;
}
.card-yellow {
    background-color: #fffbe6;
    color: #8a6500;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 DevData Academy")
st.subheader("Mi tutor personal de Python, SQL, Power BI, Excel, Streamlit y NEXUS")

st.markdown("""
Bienvenido a tu sistema personal de aprendizaje técnico.

Aquí vas a:

- 📚 Documentar lo que aprendes
- 🧠 Recordar cómo lo hiciste
- 💻 Guardar código reutilizable
- 🧪 Practicar conceptos reales
- ⚠️ Registrar errores y soluciones
""")

st.divider()

st.markdown("## 🔍 ¿Qué quieres hacer hoy?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card card-blue">
        <h4>🐍 Aprender Python</h4>
        <p>Automatización, limpieza de datos, pandas, scripts y desarrollo de soluciones.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card card-green">
        <h4>🗄️ Practicar SQL</h4>
        <p>Consultas, JOIN, filtros, agrupaciones, validaciones y bases de datos.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card card-yellow">
        <h4>📊 Revisar Power BI</h4>
        <p>DAX, modelo estrella, dashboards, KPIs y storytelling.</p>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card card-blue">
        <h4>📘 Estudiar Excel</h4>
        <p>Power Query, tablas, fórmulas, macros, validaciones y dashboards.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card card-green">
        <h4>📦 Revisar NEXUS / Kardex</h4>
        <p>Reglas de negocio, stock, seriales, reintegros y trazabilidad.</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card card-yellow">
        <h4>🌐 Crear apps con Streamlit</h4>
        <p>Apps web, formularios, menús, tablas, despliegue y acceso desde celular.</p>
    </div>
    """, unsafe_allow_html=True)

col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("""
    <div class="card card-blue">
        <h4>📄 Compresor PDF Inteligente</h4>
        <p>Comprimir PDFs, optimizar peso y automatizar carpetas.</p>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown("""
    <div class="card card-green">
        <h4>⏱️ Control ANS v5</h4>
        <p>Alertas, tiempos, geolocalización y cumplimiento empresarial.</p>
    </div>
    """, unsafe_allow_html=True)

with col9:
    st.markdown("""
    <div class="card card-yellow">
        <h4>🧠 Errores y soluciones</h4>
        <p>Casos reales, fallas corregidas y aprendizajes técnicos.</p>
    </div>
    """, unsafe_allow_html=True)