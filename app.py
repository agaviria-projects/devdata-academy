import streamlit as st

st.set_page_config(
    page_title="DevData Academy",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.card {
    height: auto !important;
    min-height: 180px !important;
    padding: 22px 18px 32px 18px !important;
    border-radius: 12px;
    margin-bottom: 18px !important;
    font-size: 15px;
    line-height: 1.8 !important;
    box-sizing: border-box;
    overflow: visible !important;
    word-break: normal;
    white-space: normal;
}

.card h4 {
    margin-top: 0 !important;
    margin-bottom: 18px !important;
    font-size: 20px;
    line-height: 1.4 !important;
}

.card p {
    margin: 0 !important;
    padding-bottom: 12px !important;
    line-height: 1.8 !important;
    overflow: visible !important;
    white-space: normal;
}
@media (max-width: 768px) {
    .card {
        height: auto !important;
        min-height: 220px !important;
        padding-bottom: 40px !important;
        overflow: visible !important;
    }

    .card p {
        font-size: 14px !important;
        line-height: 1.9 !important;
        padding-bottom: 20px !important;
    }
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

/* Ajuste especial para celular */
@media (max-width: 768px) {
    .card {
        padding: 18px;
        margin-bottom: 16px;
        font-size: 14px;
        line-height: 1.8;
    }

    .card h4 {
        font-size: 18px;
        line-height: 1.4;
    }
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

st.markdown("## 🔎 Buscar en tu conocimiento")

busqueda = st.text_input("Escribe algo (ej: JOIN, pandas, reintegro...)")

if busqueda:
    st.info(f"Resultados para: {busqueda}")

    if "sql" in busqueda.lower() or "join" in busqueda.lower():
        st.success("🗄️ SQL → Ve a la sección SQL para practicar JOIN y consultas")

    if "python" in busqueda.lower() or "pandas" in busqueda.lower():
        st.success("🐍 Python → Revisa limpieza de datos y automatización")

    if "pdf" in busqueda.lower():
        st.success("📄 PDF → Revisa compresión de PDFs")

    if "ans" in busqueda.lower():
        st.success("⏱️ Control ANS → Revisa seguimiento de tiempos")

    if "nexus" in busqueda.lower() or "kardex" in busqueda.lower():
        st.success("📦 NEXUS → Revisa reglas de negocio e inventario")

    if "power bi" in busqueda.lower():
        st.success("📊 Power BI → Revisa DAX y dashboards")
st.divider()

st.markdown("## 🧪 Modo práctica")

modulo_practica = st.selectbox(
    "Selecciona qué quieres practicar",
    ["Seleccione...", "Python", "SQL", "Power BI", "Excel", "NEXUS / Kardex", "Streamlit", "PDF", "Control ANS"]
)

nivel = st.selectbox(
    "Selecciona el nivel",
    ["Básico", "Intermedio", "Avanzado"]
)

if modulo_practica == "SQL":
    st.success("🗄️ Práctica SQL - Nivel " + nivel)

    st.markdown("### Objetivo")
    st.write("Practicar consultas básicas para extraer información de una tabla.")

    st.markdown("### Explicación")
    st.write("SQL permite consultar datos almacenados en una base de datos. La consulta más básica es SELECT.")

    st.markdown("### Código guía")
    st.code("""
SELECT *
FROM ventas;
""", language="sql")

    st.markdown("### Reto")
    st.info("Crea una consulta que muestre solo las columnas cliente, ciudad y total_venta de la tabla ventas.")

elif modulo_practica == "Python":
    st.success("🐍 Práctica Python - Nivel " + nivel)

    st.markdown("### Objetivo")
    st.write("Leer un archivo Excel y calcular una nueva columna.")

    st.markdown("### Explicación")
    st.write("Con pandas puedes cargar archivos, limpiar datos y crear columnas calculadas.")

    st.markdown("### Código guía")
    st.code("""
import pandas as pd

df = pd.read_excel("ventas.xlsx")
df["total"] = df["cantidad"] * df["precio"]

print(df.head())
""", language="python")

    st.markdown("### Reto")
    st.info("Crea una columna llamada total_iva calculando el total más el 19% de IVA.")

elif modulo_practica == "Power BI":
    st.success("📊 Práctica Power BI - Nivel " + nivel)

    st.markdown("### Objetivo")
    st.write("Crear una medida DAX para calcular ventas totales.")

    st.markdown("### Código guía")
    st.code("""
Ventas Totales = SUM(Ventas[Total])
""", language="text")

    st.markdown("### Reto")
    st.info("Crea una medida llamada Promedio Venta usando AVERAGE.")

elif modulo_practica == "NEXUS / Kardex":
    st.success("📦 Práctica NEXUS / Kardex - Nivel " + nivel)

    st.markdown("### Objetivo")
    st.write("Recordar la regla principal del stock en NEXUS.")

    st.markdown("### Regla")
    st.warning("Solo METROPOLITANA SUR afecta el stock real. Las demás zonas son trazabilidad.")

    st.markdown("### Reto")
    st.info("Explica por qué una ENTREGA AH mal registrada debe corregirse con REINTEGRO y no con ajuste manual.")

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