import sqlite3
from pathlib import Path

import streamlit as st

DB_PATH = Path("data/conocimiento.db")


def conectar_db():
    return sqlite3.connect(DB_PATH)


def crear_tabla_si_no_existe():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conocimiento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modulo TEXT,
        titulo TEXT,
        descripcion TEXT,
        codigo TEXT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    try:
        cursor.execute("ALTER TABLE conocimiento ADD COLUMN favorito INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


def guardar_conocimiento(modulo, titulo, descripcion, codigo):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO conocimiento (modulo, titulo, descripcion, codigo)
    VALUES (?, ?, ?, ?)
    """, (modulo, titulo, descripcion, codigo))

    conn.commit()
    conn.close()


def buscar_conocimiento(busqueda):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT modulo, titulo, descripcion, codigo, fecha
    FROM conocimiento
    WHERE titulo LIKE ?
       OR descripcion LIKE ?
       OR codigo LIKE ?
       OR modulo LIKE ?
    ORDER BY id DESC
    """, (
        f"%{busqueda}%",
        f"%{busqueda}%",
        f"%{busqueda}%",
        f"%{busqueda}%"
    ))

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def obtener_conocimiento():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, modulo, titulo, descripcion, codigo, fecha, favorito
    FROM conocimiento
    ORDER BY favorito DESC, id DESC
    """)

    datos = cursor.fetchall()
    conn.close()
    return datos

def eliminar_conocimiento(id):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM conocimiento WHERE id = ?", (id,))

    conn.commit()
    conn.close()


def actualizar_conocimiento(id, titulo, descripcion, codigo):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE conocimiento
    SET titulo = ?, descripcion = ?, codigo = ?
    WHERE id = ?
    """, (titulo, descripcion, codigo, id))

    conn.commit()
    conn.close()

def cambiar_favorito(id_, favorito):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE conocimiento
    SET favorito = ?
    WHERE id = ?
    """, (favorito, id_))

    conn.commit()
    conn.close()


def obtener_favoritos():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, modulo, titulo, descripcion, codigo, fecha, favorito
    FROM conocimiento
    WHERE favorito = 1
    ORDER BY id DESC
    """)

    datos = cursor.fetchall()
    conn.close()
    return datos

st.set_page_config(
    page_title="DevData Academy",
    page_icon="🧠",
    layout="wide"
)

crear_tabla_si_no_existe()

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

@media (max-width: 768px) {
    .card {
        height: auto !important;
        min-height: 220px !important;
        padding: 18px 18px 40px 18px !important;
        margin-bottom: 16px !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
        overflow: visible !important;
    }

    .card h4 {
        font-size: 18px !important;
        line-height: 1.4 !important;
    }

    .card p {
        font-size: 14px !important;
        line-height: 1.9 !important;
        padding-bottom: 20px !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
    font-size: clamp(26px, 7vw, 42px);
    white-space: nowrap;
    margin-bottom: 0;
">
🧠 DevData Academy
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-size: clamp(15px, 4vw, 22px);
    line-height: 1.4;
">
Mi tutor personal de Python, SQL, Power BI, Excel, Streamlit ,NEXUS,Control ANS,Compresor inteligente PDF, Git / GitHub
</p>
""", unsafe_allow_html=True)

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

tab_inicio, tab_buscar, tab_practica, tab_guardar, tab_favoritos, tab_biblioteca = st.tabs([
    "🏠 Inicio",
    "🔎 Buscar",
    "🧪 Práctica",
    "🧠 Guardar",
    "⭐ Favoritos",
    "📚 Biblioteca"
])

# ============================================================
# TAB INICIO
# ============================================================

with tab_inicio:
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
    col10, col11, col12 = st.columns(3)

    with col10:
        st.markdown("""
        <div class="card card-green">
            <h4>🌿 Git / GitHub</h4>
            <p>Versionamiento, commits, ramas, push, pull, merge y despliegue desde repositorio.</p>
        </div>
        """, unsafe_allow_html=True)

    with col11:
        st.markdown("""
        <div class="card card-blue">
            <h4>🧪 Prácticas guiadas</h4>
            <p>Ejercicios paso a paso para reforzar SQL, Python, Power BI, Excel y Streamlit.</p>
        </div>
        """, unsafe_allow_html=True)

    with col12:
        st.markdown("""
        <div class="card card-yellow">
            <h4>⭐ Favoritos</h4>
            <p>Apuntes importantes para repasar rápido desde el celular.</p>
        </div>
        """, unsafe_allow_html=True)
# ============================================================
# TAB BUSCAR
# ============================================================

with tab_buscar:
    st.markdown("## 🔎 Buscar en tu conocimiento")

    busqueda = st.text_input("Escribe algo (ej: JOIN, pandas, reintegro...)")

    if busqueda:
        resultados = buscar_conocimiento(busqueda)

        if resultados:
            st.success(f"Resultados encontrados: {len(resultados)}")

            for modulo, titulo, descripcion, codigo, fecha in resultados:
                with st.expander(f"📌 {titulo} | {modulo}"):
                    st.markdown(f"**Módulo:** {modulo}")
                    st.markdown(f"**Fecha:** {fecha}")
                    st.markdown(descripcion)

                    if codigo:
                        st.code(codigo)
        else:
            st.warning("No se encontraron resultados en tu base de conocimiento.")

# ============================================================
# TAB PRÁCTICA
# ============================================================

with tab_practica:
    st.markdown("## 🧪 Modo práctica")

    modulo_practica = st.selectbox(
        "Selecciona qué quieres practicar",
        ["Seleccione...", "Python", "SQL", "Power BI", "Excel", "NEXUS / Kardex", "Streamlit", "PDF", "Control ANS","Git / GitHub"]
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

    elif modulo_practica == "Excel":
        st.success("📘 Práctica Excel - Nivel " + nivel)

        st.markdown("### Objetivo")
        st.write("Practicar limpieza y organización de datos en Excel.")

        st.markdown("### Explicación")
        st.write("Excel permite estructurar información, aplicar fórmulas, limpiar datos y preparar reportes.")

        st.markdown("### Ejemplo")
        st.code("""
=SI(A2="";"Sin dato";A2)
""", language="text")

        st.markdown("### Reto")
        st.info("Crea una tabla con productos, cantidades y precios. Calcula el total por producto.")

    elif modulo_practica == "Streamlit":
        st.success("🌐 Práctica Streamlit - Nivel " + nivel)

        st.markdown("### Objetivo")
        st.write("Crear una mini app con título, texto y botón.")

        st.markdown("### Código guía")
        st.code("""
import streamlit as st

st.title("Mi primera app")
st.write("Hola, estoy aprendiendo Streamlit")

if st.button("Saludar"):
    st.success("¡Hola!")
""", language="python")

        st.markdown("### Reto")
        st.info("Agrega un input de texto para que el usuario escriba su nombre.")

    elif modulo_practica == "PDF":
        st.success("📄 Práctica PDF - Nivel " + nivel)

        st.markdown("### Objetivo")
        st.write("Recordar cómo automatizar la compresión de archivos PDF con Python.")

        st.markdown("### Código guía")
        st.code("""
from pathlib import Path

carpeta_origen = Path("PDF")
carpeta_destino = Path("PDF_COMPRIMIDOS")

carpeta_destino.mkdir(exist_ok=True)
""", language="python")

        st.markdown("### Reto")
        st.info("Crea una carpeta origen y una carpeta destino para guardar PDFs comprimidos.")

    elif modulo_practica == "Control ANS":
        st.success("⏱️ Práctica Control ANS - Nivel " + nivel)

        st.markdown("### Objetivo")
        st.write("Calcular si una solicitud cumple o incumple el tiempo acordado.")

        st.markdown("### Código guía")
        st.code("""
if fecha_cierre <= fecha_limite:
    estado = "Cumplido"
else:
    estado = "Vencido"
""", language="python")

        st.markdown("### Reto")
        st.info("Crea una tabla con fecha_creacion, fecha_limite y fecha_cierre. Calcula el estado ANS.")

    elif modulo_practica == "Git / GitHub":
        st.success("🌿 Práctica Git / GitHub - Nivel " + nivel)

        st.markdown("### Objetivo")
        st.write("Practicar el flujo básico para guardar cambios y subirlos a GitHub.")

        st.markdown("### Explicación")
        st.write("Git permite controlar versiones del proyecto. GitHub permite guardar el repositorio en la nube.")

        st.markdown("### Código guía")
        st.code("""
    git status
    git add .
    git commit -m "Descripcion del cambio"
    git push
    """, language="bash")

        st.markdown("### Reto")
        st.info("Haz un cambio pequeño en la app, revisa el estado con git status, crea un commit y súbelo a GitHub.")

# ============================================================
# TAB GUARDAR
# ============================================================

with tab_guardar:
    st.markdown("## 🧠 Guardar nuevo conocimiento")

    modulo = st.selectbox(
        "Módulo",
        ["Python", "SQL", "Power BI", "Excel", "NEXUS", "PDF", "ANS"]
    )

    titulo = st.text_input("Título")
    descripcion = st.text_area("Descripción")
    codigo = st.text_area("Código (opcional)")

    if st.button("Guardar conocimiento"):
        if not titulo.strip() or not descripcion.strip():
            st.error("Debes escribir al menos título y descripción.")
        else:
            guardar_conocimiento(modulo, titulo, descripcion, codigo)
            st.success("Conocimiento guardado correctamente.")

with tab_favoritos:
    st.markdown("## ⭐ Favoritos")

    favoritos = obtener_favoritos()

    if favoritos:
        for id_, modulo, titulo, descripcion, codigo, fecha, favorito in favoritos:
            with st.expander(f"⭐ {titulo} | {modulo}"):
                st.markdown(f"**Módulo:** {modulo}")
                st.markdown(f"**Fecha:** {fecha}")
                st.markdown(descripcion)

                if codigo:
                    st.code(codigo)
    else:
        st.info("Aún no tienes favoritos guardados.")

# ============================================================
# TAB BIBLIOTECA
# ============================================================

with tab_biblioteca:
    st.markdown("## 📚 Conocimiento guardado")

    filtro_modulo = st.selectbox(
        "Filtrar por módulo",
        ["Todos", "Python", "SQL", "Power BI", "Excel", "NEXUS", "PDF", "ANS", "Git / GitHub"],
        key="filtro_biblioteca"
    )

    datos = obtener_conocimiento()

    if filtro_modulo != "Todos":
        datos = [d for d in datos if d[1] == filtro_modulo]

    if datos:
        for id_, modulo, titulo, descripcion, codigo, fecha, favorito in datos:

            icono = "⭐" if favorito else "📌"

            with st.expander(f"{icono} {titulo} | {modulo}"):

                st.markdown(f"**Módulo:** {modulo}")
                st.markdown(f"**Fecha:** {fecha}")

                es_favorito = st.checkbox(
                    "⭐ Marcar como favorito",
                    value=bool(favorito),
                    key=f"fav_{id_}"
                )

                if es_favorito != bool(favorito):
                    cambiar_favorito(id_, 1 if es_favorito else 0)
                    st.rerun()

                nuevo_titulo = st.text_input("Título", value=titulo, key=f"t_{id_}")
                nueva_desc = st.text_area("Descripción", value=descripcion, key=f"d_{id_}")
                nuevo_codigo = st.text_area("Código", value=codigo or "", key=f"c_{id_}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button("💾 Guardar cambios", key=f"g_{id_}"):
                        actualizar_conocimiento(id_, nuevo_titulo, nueva_desc, nuevo_codigo)
                        st.success("Actualizado correctamente")
                        st.rerun()

                with col2:
                    if st.button("🗑️ Eliminar", key=f"e_{id_}"):
                        eliminar_conocimiento(id_)
                        st.warning("Eliminado correctamente")
                        st.rerun()
    else:
        st.info("Aún no hay conocimiento guardado para este filtro.")