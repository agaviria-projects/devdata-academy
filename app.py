import sqlite3
from pathlib import Path
import streamlit as st

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="DevData Academy",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# DETECCIÓN MÓVIL (MANUAL SIMPLE)
# =========================================
modo_movil = st.sidebar.toggle("📱 Modo celular", value=True)

# =========================================
# DB
# =========================================
DB_PATH = Path("data/conocimiento.db")

def conectar_db():
    return sqlite3.connect(DB_PATH)

def crear_tabla():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = conectar_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS conocimiento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modulo TEXT,
        titulo TEXT,
        descripcion TEXT,
        codigo TEXT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        favorito INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

crear_tabla()

# =========================================
# FUNCIONES
# =========================================
def guardar(modulo,titulo,desc,cod):
    conn=conectar_db()
    c=conn.cursor()
    c.execute("INSERT INTO conocimiento(modulo,titulo,descripcion,codigo) VALUES(?,?,?,?)",(modulo,titulo,desc,cod))
    conn.commit()
    conn.close()

def obtener():
    conn=conectar_db()
    c=conn.cursor()
    c.execute("SELECT * FROM conocimiento ORDER BY favorito DESC, id DESC")
    data=c.fetchall()
    conn.close()
    return data

def buscar(txt):
    conn=conectar_db()
    c=conn.cursor()
    c.execute("SELECT * FROM conocimiento WHERE titulo LIKE ? OR descripcion LIKE ?",(f"%{txt}%",f"%{txt}%"))
    data=c.fetchall()
    conn.close()
    return data

def favorito(id,val):
    conn=conectar_db()
    c=conn.cursor()
    c.execute("UPDATE conocimiento SET favorito=? WHERE id=?",(val,id))
    conn.commit()
    conn.close()

# =========================================
# CSS RESPONSIVE
# =========================================
st.markdown("""
<style>
html, body {
    background-color: #0f172a;
    color: #e5e7eb;
}

.header {
    background: linear-gradient(90deg,#16a34a,#065f46);
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

/* 🔥 CLAVE PARA CELULAR */
.header h2 {
    margin:0;
    font-size: clamp(16px, 5vw, 22px);
    line-height: 1.2;
    word-break: break-word;
}

.header p {
    margin:4px 0 0 0;
    font-size: clamp(11px, 3vw, 14px);
}

.card {
    background: linear-gradient(90deg, #1f2937, #111827);
    padding: 14px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: #e5e7eb;
    font-weight: 500;
    font-size: clamp(14px, 4vw, 16px);
    border: 1px solid rgba(255,255,255,0.05);
}

/* EFECTO CLICK (MUY IMPORTANTE EN CELULAR) */
.card:active {
    transform: scale(0.97);
    background: #16a34a;
}
            
h2 {
    font-size: clamp(16px,5vw,26px);
}

p {
    font-size: clamp(12px,3vw,14px);
}

.stButton>button {
    background:#16a34a;
    color:white;
    border-radius:6px;
}

/* Ajuste móvil */
@media (max-width: 768px) {
    .block-container {
        padding: 10px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER LIMPIO (100% RESPONSIVE)
# =========================================
st.markdown("""
<div style="
    font-size:22px;
    font-weight:700;
    color:#22c55e;
    text-align:center;
    margin-bottom:4px;
">
🚀 Plataforma de Entrenamiento
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:22px;'>Aprende SQL, Python y automatización</p>", unsafe_allow_html=True)


# =========================================
# TABS
# =========================================
tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs([
    "🏠 Inicio",
    "🔎 Buscar",
    "🧪 Práctica",
    "🚀 Python Guiado",
    "🧠 Guardar",
    "⭐ Favoritos",
    "📚 Biblioteca"
])

# =========================================
# INICIO
# =========================================
with tab1:
    st.markdown("## ¿Qué quieres hacer hoy?")

    if modo_movil:
        # 🔥 UNA COLUMNA (CELULAR)
        st.markdown('<div class="card">🐍 Python</div>',unsafe_allow_html=True)
        st.markdown('<div class="card">🗄️ SQL</div>',unsafe_allow_html=True)
        st.markdown('<div class="card">📊 Power BI</div>',unsafe_allow_html=True)
        st.markdown('<div class="card">📘 Excel</div>',unsafe_allow_html=True)
        st.markdown('<div class="card">📦 NEXUS</div>',unsafe_allow_html=True)
        st.markdown('<div class="card">🌐 Streamlit</div>',unsafe_allow_html=True)

    else:
        # 💻 DOS COLUMNAS (PC)
        col1,col2=st.columns(2)

        with col1:
            st.markdown('<div class="card">🐍 Python</div>',unsafe_allow_html=True)
            st.markdown('<div class="card">🗄️ SQL</div>',unsafe_allow_html=True)
            st.markdown('<div class="card">📊 Power BI</div>',unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">📘 Excel</div>',unsafe_allow_html=True)
            st.markdown('<div class="card">📦 NEXUS</div>',unsafe_allow_html=True)
            st.markdown('<div class="card">🌐 Streamlit</div>',unsafe_allow_html=True)

# =========================================
# BUSCAR
# =========================================
with tab2:
    txt=st.text_input("Buscar")

    if txt:
        res=buscar(txt)
        for r in res:
            st.write(r)

# =========================================
# PRACTICA
# =========================================
with tab3:
    mod=st.selectbox("Modulo",["SQL","Python"])

    if mod=="SQL":
        q=st.text_area("Consulta SQL")

        if st.button("Evaluar SQL"):
            if "select" in q.lower():
                st.success("Correcto")
            else:
                st.error("Error")

    if mod=="Python":
        c=st.text_area("Código Python")

        if st.button("Ejecutar"):
            try:
                exec(c)
                st.success("OK")
            except Exception as e:
                st.error(e)

# =========================================
# GUARDAR
# =========================================
with tab5:
    mod=st.selectbox("Modulo",["Python","SQL"])
    t=st.text_input("Titulo")
    d=st.text_area("Descripcion")
    c=st.text_area("Codigo")

    if st.button("Guardar"):
        guardar(mod,t,d,c)
        st.success("Guardado")

# =========================================
# PYTHON GUIADO
# =========================================
with tab4:

    st.markdown("## 🚀 Python Automatización Guiada")

    st.info("""
Aprende paso a paso cómo automatizar procesos reales:

✅ Leer archivos Excel
✅ Limpiar datos
✅ Convertir fechas
✅ Realizar cálculos
✅ Agrupar información
✅ Exportar archivos
✅ Automatizar procesos empresariales
    """)

    paso = st.selectbox(
        "Seleccione una práctica",
        [
            "1️⃣ Leer archivo Excel",
            "2️⃣ Inspeccionar DataFrame",
            "3️⃣ Limpiar texto",
            "4️⃣ Convertir fechas",
            "5️⃣ Crear cálculos",
            "6️⃣ Agrupar información",
            "7️⃣ Exportar a Excel"
        ]
    )

    # =========================================
    # PASO 1
    # =========================================
    if paso == "1️⃣ Leer archivo Excel":

        st.markdown("## 📂 Paso 1 — Lectura de Excel")

        st.warning("""
Escenario real:

Un analista recibe un archivo Excel exportado desde SAP
o desde un ERP empresarial y necesita procesarlo con Python.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
Aprender a:

✔ leer archivos Excel
✔ cargar DataFrames
✔ visualizar registros
✔ validar columnas
✔ iniciar automatización
        """)

        st.markdown("### 📦 Librería utilizada")

        st.code("""
pip install pandas openpyxl
        """, language="bash")

        st.markdown("### 🧠 Código")

        st.code("""
import pandas as pd


df = pd.read_excel("ventas.xlsx")

print(df.head())
        """, language="python")

        st.markdown("### 🔍 Explicación línea por línea")

        st.info("""
📌 import pandas as pd
Importa la librería pandas.

📌 pd.read_excel()
Lee el archivo Excel.

📌 df
Representa el DataFrame.

📌 head()
Muestra los primeros registros.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
Error:
Missing optional dependency openpyxl

Solución:
pip install openpyxl
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
Ejemplo real:

✔ ventas SAP
✔ inventarios
✔ reportes financieros
✔ entregas logísticas
✔ movimientos de almacén
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar con archivo real")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="lectura_excel"
        )

        if archivo is not None:

            import pandas as pd

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado correctamente")

            st.dataframe(df.head())

            st.markdown("### 📊 Información del DataFrame")

            st.write("Filas y columnas:")
            st.write(df.shape)

            st.markdown("### 🧾 Tipos de datos")

            st.dataframe(
                df.dtypes.astype(str)
            )

    # =========================================
    # PASO 2
    # =========================================
    elif paso == "2️⃣ Inspeccionar DataFrame":

        st.markdown("## 🔍 Paso 2 — Inspeccionar DataFrame")

        st.warning("""
Escenario real:

Después de leer un archivo Excel,
el analista debe revisar la estructura
del DataFrame antes de limpiar o calcular.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
Aprender a:

✔ revisar columnas
✔ validar tipos de datos
✔ detectar nulos
✔ inspeccionar registros
✔ entender la estructura
        """)

        st.markdown("### 🧠 Código")

        st.code("""
df.info()

df.head()

df.describe()
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
📌 df.info()
Muestra columnas y tipos de datos.

📌 df.head()
Muestra los primeros registros.

📌 df.describe()

Genera estadísticas automáticas
de columnas numéricas.

Incluye:

✔ promedio (mean)
✔ mínimo (min)
✔ máximo (max)
✔ mediana (50%)
✔ desviación estándar (std)

📌 ¿Para qué sirve?

✔ detectar errores
✔ validar datos
✔ encontrar valores anormales
✔ revisar comportamiento datos
✔ análisis rápido empresarial

📌 Ejemplo real:

Si el precio promedio es:

5000

pero aparece:

999999

puede existir un error de carga.

📌 count

Cantidad registros válidos.

📌 mean

Promedio.

📌 std

Qué tanto varían los datos.

📌 min / max

Valores mínimos y máximos.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
No revisar los tipos de datos antes
de hacer cálculos o visualizaciones.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
Ejemplo real:

✔ validar exportes SAP
✔ detectar columnas vacías
✔ revisar fechas incorrectas
✔ validar cantidades
✔ encontrar errores de carga
        """)

    # =========================================
    # PASO 3
    # =========================================
    elif paso == "3️⃣ Limpiar texto":

        st.markdown("## 🧹 Paso 3 — Limpieza de texto")

        st.warning("""
Escenario real:

Los archivos SAP o ERP suelen venir
con espacios, mayúsculas incorrectas
o textos inconsistentes.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
Aprender a:

✔ limpiar espacios
✔ convertir mayúsculas
✔ estandarizar nombres
✔ preparar datos para análisis
        """)

        st.markdown("### 🧠 Código")

        st.code("""
df["cliente"] = (
    df["cliente"]
    .str.strip()
    .str.upper()
)
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
📌 .str.strip()
Elimina espacios al inicio y final.

📌 .str.upper()
Convierte texto a MAYÚSCULAS.

📌 df["cliente"]
Selecciona la columna cliente.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
Intentar limpiar columnas numéricas
como si fueran texto.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
Ejemplo real:

✔ nombres clientes
✔ ciudades
✔ proveedores
✔ técnicos
✔ materiales SAP
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar limpieza real")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="limpieza_texto"
        )

        if archivo is not None:

            import pandas as pd

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado")

            st.dataframe(df.head())

            columna = st.selectbox(
                "Seleccione columna texto",
                df.columns
            )

            if st.button("🧹 Limpiar texto"):

                df[columna] = (
                    df[columna]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                )

                st.success("✅ Texto limpiado")

                st.dataframe(df.head())

    # =========================================
    # PASO 4
    # =========================================
    elif paso == "4️⃣ Convertir fechas":

        st.markdown("## 📅 Paso 4 — Conversión de fechas")

        st.warning("""
Escenario real:

Los archivos empresariales suelen traer
fechas en formatos inconsistentes.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
Aprender a:

✔ convertir fechas
✔ detectar errores
✔ validar formatos
✔ preparar fechas para análisis
        """)

        st.markdown("### 🧠 Código")

        st.code("""
df["fecha"] = pd.to_datetime(
    df["fecha"],
    errors="coerce"
)
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
📌 pd.to_datetime()

Convierte texto a formato fecha.

Ejemplo:

'01/02/2025'
↓
2025-01-02 00:00:00

📌 errors="coerce"

Convierte errores en NaT.

NaT significa:

Not a Time.

📌 ¿Por qué aparece 00:00:00?

Porque pandas guarda:

fecha + hora

Si no existe hora,
automáticamente coloca:

00:00:00

📌 ¿Cómo dejar solo fecha?

Usando:

.dt.date

📌 Ejemplo:

df["fecha"] = pd.to_datetime(
    df["fecha"],
    errors="coerce"
).dt.date

📌 Se usa para:

✔ Power BI
✔ dashboards
✔ filtros tiempo
✔ KPIs mensuales
✔ análisis anual
                

📌 errors="coerce"
Convierte errores en NaT.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
No validar formatos antes
de crear análisis de tiempo.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
Ejemplo real:

✔ ventas
✔ entregas
✔ facturación
✔ inventarios
✔ movimientos SAP
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar conversión real")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="fechas"
        )

        if archivo is not None:

            import pandas as pd

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado")

            st.dataframe(df.head())

            columna = st.selectbox(
                "Seleccione columna fecha",
                df.columns
            )

            if st.button("📅 Convertir fechas"):

                df[columna] = pd.to_datetime(
                    df[columna],
                    errors="coerce"
                )

                st.success("✅ Fechas convertidas")

                st.dataframe(df.head())

                st.write(df.dtypes)

    # =========================================
    # PASO 5
    # =========================================
    elif paso == "5️⃣ Crear cálculos":

        st.markdown("## 📊 Paso 5 — Crear cálculos")

        st.warning("""
Escenario real:

Los analistas necesitan generar
columnas calculadas automáticamente
para KPIs y reportes.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
Aprender a:

✔ multiplicar columnas
✔ crear métricas
✔ automatizar cálculos
✔ preparar análisis
        """)

        st.markdown("### 🧠 Código")

        st.code("""
df["total"] = (
    df["cantidad"] * df["precio"]
)
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
📌 df["total"]
Crea nueva columna.

📌 df["total"]

Crea nueva columna calculada.

📌 cantidad * precio

Multiplica ambas columnas.

📌 pd.to_numeric()

Convierte texto a número.

Ejemplo:

'5000'
↓
5000

📌 errors="coerce"

Convierte errores en NaN
sin detener el script.

📌 ¿Por qué usarlo?

Muchos archivos SAP/ERP
traen números como texto.

📌 Ejemplo real:

'5000'
'7000'
'error'

Sin pd.to_numeric()
el cálculo puede fallar.

📌 Se usa para:

✔ ventas
✔ costos
✔ inventarios
✔ KPIs
✔ facturación
                
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
Intentar multiplicar columnas texto
sin convertirlas a numérico.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
Ejemplo real:

✔ ventas
✔ costos
✔ inventarios
✔ facturación
✔ logística
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar cálculos reales")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="calculos"
        )

        if archivo is not None:

            import pandas as pd

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado")

            st.dataframe(df.head())

            columna1 = st.selectbox(
                "Seleccione primera columna",
                df.columns,
                key="col1"
            )

            columna2 = st.selectbox(
                "Seleccione segunda columna",
                df.columns,
                key="col2"
            )

            if st.button("📊 Crear cálculo"):

                df["resultado"] = (
                    pd.to_numeric(df[columna1], errors="coerce")
                    *
                    pd.to_numeric(df[columna2], errors="coerce")
                )

                st.success("✅ Cálculo realizado")

                st.dataframe(df.head())
    # =========================================
    # PASO 6
    # =========================================
    elif paso == "6️⃣ Agrupar información":

        st.markdown("## 📦 Paso 6 — Agrupar información")

        st.warning("""
    Escenario real:

    Los analistas necesitan resumir información
    para generar KPIs y reportes ejecutivos.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
    Aprender a:

    ✔ agrupar datos
    ✔ resumir información
    ✔ generar KPIs
    ✔ calcular totales
    ✔ preparar reportes
        """)

        st.markdown("### 🧠 Código")

        st.code("""
    resumen = (
        df.groupby("ciudad")["total"]
        .sum()
    )
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
    
    📌 groupby()

    Agrupa registros similares.

    Ejemplo:

    MEDELLIN
    MEDELLIN
    BOGOTA

    ↓ agrupación ↓

    MEDELLIN = total ventas
    BOGOTA = total ventas

    📌 sum()

    Suma valores numéricos.

    📌 resumen

    Variable donde se guarda
    la agrupación final.

    📌 print(resumen)

    Muestra el resultado agrupado
    en consola.

    📌 ¿Para qué sirve?

    ✔ validar KPIs
    ✔ revisar totales
    ✔ validar dashboards
    ✔ verificar agrupaciones
    ✔ análisis empresarial                        

    📌 ["ventas"]

    Selecciona columna numérica.

    ⚠️ IMPORTANTE

    La columna puede cambiar.

    Ejemplo:

    ["total"]
    ["cantidad"]
    ["costos"]

    Depende del archivo.

    📌 ¿Para qué sirve?

    ✔ KPIs
    ✔ dashboards
    ✔ Power BI
    ✔ reportes ejecutivos
    ✔ análisis ventas
    ✔ inventarios

    📌 Ejemplo empresarial:

    ventas totales por ciudad
    costos por proyecto
    facturación por cliente            

    📌 sum()
    Suma valores.

    📌 ["ventas"]
    Selecciona columna numérica.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
    Intentar agrupar columnas
    que no existen o tienen errores.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
    Ejemplo real:

    ✔ ventas por ciudad
    ✔ costos por proyecto
    ✔ inventario por almacén
    ✔ entregas por técnico
    ✔ facturación por cliente
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar agrupación real")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="groupby"
        )

        if archivo is not None:

            import pandas as pd

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado")

            st.dataframe(df.head())

            columna_grupo = st.selectbox(
                "Seleccione columna para agrupar",
                df.columns,
                key="grupo"
            )

            columna_valor = st.selectbox(
                "Seleccione columna numérica",
                df.columns,
                key="valor"
            )

            if st.button("📦 Agrupar información"):

                resumen = (
                    df.groupby(columna_grupo)[columna_valor]
                    .sum()
                    .reset_index()
                )

                st.success("✅ Agrupación realizada")

                st.dataframe(resumen)
    # =========================================
    # PASO 7
    # =========================================
    elif paso == "7️⃣ Exportar a Excel":

        st.markdown("## 📤 Paso 7 — Exportar a Excel")

        st.warning("""
    Escenario real:

    Después de limpiar y transformar datos,
    el analista necesita entregar un archivo
    Excel listo para Power BI o reportes.
        """)

        st.markdown("### ✅ Objetivo")

        st.success("""
    Aprender a:

    ✔ exportar DataFrames
    ✔ generar archivos Excel
    ✔ automatizar entregables
    ✔ preparar archivos finales
        """)

        st.markdown("### 🧠 Código")

        st.code("""
    df.to_excel(
        "archivo_limpio.xlsx",
        index=False
    )
        """, language="python")

        st.markdown("### 🔍 Explicación")

        st.info("""
    📌 to_excel()
    Exporta DataFrame a Excel.

    📌 index=False
    Evita exportar índices.
        """)

        st.markdown("### ⚠️ Error común")

        st.error("""
    No instalar openpyxl
    antes de exportar archivos.
        """)

        st.markdown("### 💼 Caso empresarial")

        st.success("""
    Ejemplo real:

    ✔ archivos SAP limpios
    ✔ reportes financieros
    ✔ entregas Power BI
    ✔ consolidaciones
    ✔ inventarios finales
        """)

        # =========================================
        # PRÁCTICA REAL
        # =========================================
        st.markdown("### 📤 Probar exportación real")

        archivo = st.file_uploader(
            "Suba un archivo Excel",
            type=["xlsx"],
            key="exportar_excel"
        )

        if archivo is not None:

            import pandas as pd
            from io import BytesIO

            df = pd.read_excel(archivo)

            st.success("✅ Archivo cargado")

            st.dataframe(df.head())

            output = BytesIO()

            df.to_excel(
                output,
                index=False,
                engine="openpyxl"
            )

            output.seek(0)

            st.success("✅ Archivo preparado para descarga")

            st.download_button(
                label="📥 Descargar Excel",
                data=output,
                file_name="archivo_limpio.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )