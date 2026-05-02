import streamlit as st

# =========================================
# CONFIGURACIÓN
# =========================================
st.set_page_config(page_title="Git & GitHub", layout="wide")

st.title("📦 Git & GitHub - Nivel Profesional")
st.markdown("---")

# =========================================
# ¿QUÉ ES?
# =========================================
st.header("🧠 ¿Qué es Git & GitHub?")

st.markdown("""
**Git** es un sistema de control de versiones que permite:
- Guardar cambios de código
- Volver a versiones anteriores
- Trabajar por ramas sin dañar el proyecto

**GitHub** es la nube donde subes tu código:
- Portafolio profesional
- Trabajo en equipo
- Backup de proyectos

👉 En tu caso:
Es la base para guardar y mostrar proyectos como:
- NEXUS
- Scripts Python
- Dashboards Power BI
""")

# =========================================
# ¿PARA QUÉ SIRVE?
# =========================================
st.header("🎯 ¿Para qué sirve en la vida real?")

st.markdown("""
- Guardar versiones de tus proyectos
- Evitar perder código
- Mostrar portafolio profesional
- Trabajar en equipo
- Hacer pruebas sin dañar producción

💼 En trabajo real:
- Todo proyecto serio usa Git
- Te pueden pedir:
  - Hacer commit
  - Crear ramas
  - Resolver conflictos
""")

# =========================================
# DÓNDE LO USASTE
# =========================================
st.header("📍 ¿Dónde lo usaste tú?")

st.markdown("""
✔ Proyecto NEXUS (dev / main)  
✔ Script compresor PDF  
✔ DevData Academy (esta app)  
✔ Proyectos de SQL y Python  

👉 Ya lo usas… ahora lo vamos a profesionalizar
""")

# =========================================
# COMANDOS ESENCIALES
# =========================================
st.header("⚙️ Comandos esenciales")

st.code("""
# Inicializar repositorio
git init

# Ver estado
git status

# Agregar archivos
git add .

# Guardar cambios
git commit -m "mensaje"

# Ver historial
git log

# Conectar a GitHub
git remote add origin URL

# Subir código
git push -u origin main
""")

# =========================================
# FLUJO PROFESIONAL (CLAVE)
# =========================================
st.header("🔥 Flujo profesional (IMPORTANTE)")

st.markdown("""
Este es el flujo que debes usar SIEMPRE:

1. Trabajas en DEV
2. Haces commit en DEV
3. Pruebas
4. Merge a MAIN cuando esté estable

👉 Ejemplo:
""")

st.code("""
git checkout dev
# haces cambios

git add .
git commit -m "Corrección validación seriales"

git checkout main
git merge dev

git push origin main
""")

# =========================================
# RAMAS (CLAVE)
# =========================================
st.header("🌿 Ramas (Branches)")

st.markdown("""
- main → producción
- dev → desarrollo
- feature → pruebas

👉 Nunca trabajes directo en main
""")

st.code("""
# Crear rama
git checkout -b nueva_rama

# Cambiar de rama
git checkout dev

# Ver ramas
git branch
""")

# =========================================
# ERRORES COMUNES
# =========================================
st.header("❌ Errores comunes")

st.markdown("""
🔴 No hacer commit frecuente  
🔴 Trabajar en main directamente  
🔴 No hacer pull antes de push  
🔴 Subir archivos innecesarios  
🔴 Romper código sin backup  

👉 TU CASO:
Ya te pasó:
- Romper scripts sin control
- No saber qué cambió

Git soluciona eso.
""")

# =========================================
# CHECKLIST
# =========================================
st.header("✅ Checklist profesional")

st.markdown("""
✔ Estoy trabajando en rama dev  
✔ Hago commit con mensajes claros  
✔ No subo archivos basura  
✔ Tengo .gitignore  
✔ Hago merge solo cuando está probado  
✔ Tengo repositorio en GitHub  
""")

# =========================================
# CÓDIGO ÚTIL
# =========================================
st.header("💻 Código útil (real)")

st.markdown("🔹 Ver diferencias:")

st.code("""
git diff
""")

st.markdown("🔹 Deshacer cambios:")

st.code("""
git checkout -- archivo.py
""")

st.markdown("🔹 Guardar temporal (stash):")

st.code("""
git stash
git stash pop
""")

# =========================================
# PRÁCTICA
# =========================================
st.header("🧪 Cómo practicar")

st.markdown("""
Ejercicio:

1. Crea un proyecto nuevo
2. Inicializa Git
3. Crea rama dev
4. Haz 3 cambios
5. Haz commits separados
6. Haz merge a main

👉 Objetivo:
Sentir control total del proyecto
""")

# =========================================
# TIPS REALES
# =========================================
st.header("💡 Tips de trabajo real")

st.markdown("""
🔥 Usa mensajes claros:
❌ "cambios"
✔ "fix: validación seriales en salida"

🔥 Haz commit pequeño:
No guardes 100 cambios en uno solo

🔥 Siempre prueba antes de merge

🔥 Ten repositorio limpio:
- README.md
- estructura clara

🔥 Git es tu seguro:
Si algo se daña → puedes volver atrás
""")

# =========================================
# BONUS
# =========================================
st.header("🚀 BONUS (Nivel Pro)")

st.markdown("""
Cuando avances:

- GitHub Actions (automatización)
- Deploy automático
- Versionado semántico
- Pull Requests

👉 Eso ya es nivel empresa
""")