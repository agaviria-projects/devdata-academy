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
# PASOS COMPLETOS (CLONAR UN REPOSITORIO)
# =========================================
st.header("⚙️ Luego de clonar....")

st.code("""
# 1️⃣ Crear entorno virtual
python -m venv venv

# 2️⃣ Activarlo
En Git Bash:
source venv/Scripts/activate
        
# 3️⃣ Instalar dependencias
pip install -r requirements.txt
        
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
# ERROR 403 - PERMISOS GITHUB
# =========================================
st.header("🚫 Error 403 en GitHub - Permission denied")

st.markdown("""
Este error aparece cuando intento hacer:

    git push origin main

y Git responde algo parecido a:

    remote: Permission to elite-sst/sistema-capacitaciones.git denied to agaviria-projects.
    fatal: unable to access 'https://github.com/elite-sst/sistema-capacitaciones.git/': The requested URL returned error: 403

O también puede aparecer al revés:

    remote: Permission to agaviria-projects/devdata-academy.git denied to elite-sst.
    fatal: unable to access 'https://github.com/agaviria-projects/devdata-academy.git/': The requested URL returned error: 403

---

## Qué significa

El error 403 significa que GitHub está rechazando el push porque la cuenta autenticada no tiene permisos sobre ese repositorio.

No necesariamente significa que el código esté mal.

Normalmente el problema es:

- Estoy en el repositorio correcto
- Pero Git está autenticado con la cuenta equivocada
- GitHub no permite subir cambios con esa cuenta

---

## Regla principal

Cada proyecto debe subirse con su cuenta correcta.

| Proyecto | Repositorio | Cuenta correcta |
|---|---|---|
| DevData Academy | agaviria-projects/devdata-academy | agaviria-projects |
| Sistema Capacitaciones | elite-sst/sistema-capacitaciones | elite-sst |

---

## Cómo identificar el problema

Primero revisar a qué repositorio estoy apuntando:

    git remote -v

Ejemplo correcto para DevData Academy:

    origin  https://github.com/agaviria-projects/devdata-academy.git

Ejemplo correcto para Sistema Capacitaciones:

    origin  https://github.com/elite-sst/sistema-capacitaciones.git

Si el repositorio es de elite-sst, debo estar autenticado como elite-sst.

Si el repositorio es de agaviria-projects, debo estar autenticado como agaviria-projects.

---

## Solución 1: cerrar sesión en GitHub del navegador

1. Abrir GitHub en el navegador
2. Cerrar sesión de la cuenta incorrecta
3. Iniciar sesión con la cuenta correcta
4. Volver a intentar:

    git push origin main

---

## Solución 2: limpiar credenciales desde Windows

Ruta:

    Panel de control
        ↓
    Administrador de credenciales
        ↓
    Credenciales de Windows

Buscar y eliminar entradas relacionadas con:

    github.com
    git:https://github.com
    GitHub
    Git Credential Manager

Después:

1. Cerrar Chrome
2. Cerrar Edge
3. Cerrar GitHub Desktop si está abierto
4. Abrir Git Bash
5. Ejecutar nuevamente:

    git push origin main

Git debería pedir login otra vez.

---

## Solución 3: limpiar credenciales desde Git Bash

Ejecutar:

    git config --global --unset credential.helper

Luego:

    printf "protocol=https\\nhost=github.com\\n" | git credential reject

Después volver a activar el administrador de credenciales:

    git config --global credential.helper manager-core

Verificar:

    git config --global credential.helper

Debe mostrar:

    manager-core

Luego intentar nuevamente:

    git push origin main

---

## Solución 4: usar el login correcto cuando Git abra navegador

Cuando Git abre la ventana de autenticación o el navegador, debo revisar qué cuenta aparece arriba a la derecha.

Si estoy subiendo a:

    elite-sst/sistema-capacitaciones

debe aparecer:

    elite-sst

Si estoy subiendo a:

    agaviria-projects/devdata-academy

debe aparecer:

    agaviria-projects

Si aparece la cuenta incorrecta, cerrar sesión antes de autorizar.

---

## Solución 5: revisar que el remote esté correcto

Ver remote:

    git remote -v

Si el remote está mal, corregirlo.

Para DevData Academy:

    git remote set-url origin https://github.com/agaviria-projects/devdata-academy.git

Para Sistema Capacitaciones:

    git remote set-url origin https://github.com/elite-sst/sistema-capacitaciones.git

Luego:

    git push origin main

---

## Solución 6: usar navegadores separados

Recomendación para evitar errores:

| Cuenta | Navegador recomendado |
|---|---|
| agaviria-projects | Chrome |
| elite-sst | Edge |

O usar perfiles separados de Chrome:

- Perfil 1: agaviria-projects
- Perfil 2: elite-sst

Esto evita que GitHub mezcle sesiones.

---

## Checklist rápido cuando aparece 403

1. Revisar repo:

    git remote -v

2. Identificar cuenta correcta del repo
3. Cerrar sesión de la cuenta incorrecta en GitHub
4. Borrar credenciales Windows si sigue fallando
5. Volver a hacer push
6. Autorizar con la cuenta correcta
7. Confirmar que el push subió

---

## Ejemplo real 1

Error:

    Permission to elite-sst/sistema-capacitaciones.git denied to agaviria-projects

Significa:

Estoy intentando subir al repo de elite-sst, pero Git está usando agaviria-projects.

Solución:

Autenticar Git con:

    elite-sst

---

## Ejemplo real 2

Error:

    Permission to agaviria-projects/devdata-academy.git denied to elite-sst

Significa:

Estoy intentando subir al repo de agaviria-projects, pero Git está usando elite-sst.

Solución:

Autenticar Git con:

    agaviria-projects

---

## Frase para recordar

El repositorio manda.

Si el repo es de elite-sst, debo usar elite-sst.

Si el repo es de agaviria-projects, debo usar agaviria-projects.

El error 403 casi siempre es cuenta equivocada o falta de permisos.
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