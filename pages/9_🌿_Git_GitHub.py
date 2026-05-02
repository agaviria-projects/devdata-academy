import streamlit as st

st.set_page_config(page_title="Git / GitHub", page_icon="🌿", layout="wide")

st.title("🌿 Git / GitHub")
st.subheader("Control de versiones y trabajo profesional")

# ---------------------------------------------------
# ¿QUÉ ES?
# ---------------------------------------------------
st.markdown("## 📘 ¿Qué es Git / GitHub?")

st.markdown("""
Git es un sistema de control de versiones que permite guardar cambios en tu código.

GitHub es una plataforma en la nube donde puedes almacenar tus proyectos.
""")

# ---------------------------------------------------
# ¿PARA QUÉ SIRVE?
# ---------------------------------------------------
st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Guardar versiones de tu código
- Recuperar cambios
- Trabajar en equipo
- Subir proyectos a la nube
- Crear portafolio profesional
""")

# ---------------------------------------------------
# COMANDOS CLAVE
# ---------------------------------------------------
st.markdown("## 💻 Comandos básicos")

st.code("""
git status
git add .
git commit -m "mensaje"
git push
""", language="bash")

# ---------------------------------------------------
# DONDE LO USÉ
# ---------------------------------------------------
st.markdown("## 🧠 ¿Dónde lo usé?")

st.info("""
- DevData Academy
- Sistema NEXUS
- Control ANS
- Compresor PDF
""")

# ---------------------------------------------------
# PRÁCTICA
# ---------------------------------------------------
st.markdown("## 🧪 Práctica")

st.success("""
1. Haz un cambio en tu app
2. Ejecuta git status
3. Ejecuta git add .
4. Ejecuta git commit -m "Mi cambio"
5. Ejecuta git push
""")

# ---------------------------------------------------
# ERRORES COMUNES
# ---------------------------------------------------
st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No hacer commit antes de push
- No agregar archivos (git add)
- Confundir ramas
- No tener conexión a internet
""")