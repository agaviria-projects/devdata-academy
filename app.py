import sqlite3
from pathlib import Path
import streamlit as st

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="Plataforma de Entrenamiento en Datos y Desarrollo",
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
    font-size:18px;
    font-weight:600;
    color:#22c55e;
    text-align:center;
    margin-bottom:2px;
">
🚀 Plataforma de Entrenamiento
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:12px;'>Aprende SQL, Python y automatización</p>", unsafe_allow_html=True)


# =========================================
# TABS
# =========================================
tab1,tab2,tab3,tab4,tab5,tab6=st.tabs([
"🏠 Inicio","🔎 Buscar","🧪 Práctica","🧠 Guardar","⭐ Favoritos","📚 Biblioteca"
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
with tab4:
    mod=st.selectbox("Modulo",["Python","SQL"])
    t=st.text_input("Titulo")
    d=st.text_area("Descripcion")
    c=st.text_area("Codigo")

    if st.button("Guardar"):
        guardar(mod,t,d,c)
        st.success("Guardado")

# =========================================
# FAVORITOS
# =========================================
with tab5:
    data=obtener()

    for r in data:
        if r[6]==1:
            st.write(r)

# =========================================
# BIBLIOTECA
# =========================================
with tab6:
    data=obtener()

    for r in data:
        if modo_movil:
            st.write(r[2])
            if st.button("⭐",key=f"m{r[0]}"):
                favorito(r[0],1)
        else:
            col1,col2=st.columns([6,1])
            with col1:
                st.write(r[2])
            with col2:
                if st.button("⭐",key=r[0]):
                    favorito(r[0],1)