import streamlit as st

st.markdown("## 🧠 Mentalidad de Analista / Desarrollador")

st.info("""
Un buen analista o desarrollador no se define por memorizar código,
sino por entender cómo funciona el sistema.

Lo importante no es la sintaxis, es la lógica.
""")

st.markdown("""
### 🎯 Lo que realmente importa

✔ Qué problema resuelve el sistema  
✔ Cómo fluye la información  
✔ Qué reglas de negocio hay detrás  
✔ Qué impacto tiene cada acción  

---

### 🔍 En términos simples

No necesitas entender cada línea de código,  
pero sí debes entender:

- Qué hace cada módulo
- De dónde vienen los datos
- Cómo se transforman
- Qué resultado generan

---

### ⚠️ Error común

❌ “Funciona pero no sé qué hace”  

✔ “No memorizo el código, pero entiendo su lógica”

---

### 🏆 Nivel profesional

Un analista de datos o desarrollador realmente útil es aquel que puede:

- Explicar el sistema sin mostrar código  
- Detectar errores en lógica de negocio  
- Validar datos contra la realidad  
- Proponer mejoras funcionales  

---

### 💡 Regla clave

No necesitas saber cómo está escrito todo,  
pero sí debes entender qué hace cada parte del sistema.
""")

# =========================================
# CONFIGURACIÓN
# =========================================
st.set_page_config(page_title="Arquitectura Pro", layout="wide")

st.title("🏗️ Arquitectura de Proyectos - Nivel Profesional")
st.markdown("---")

# =========================================
# ¿QUÉ ES?
# =========================================
st.header("🧠 ¿Qué es la arquitectura de un proyecto?")

st.markdown("""
Es la forma en que organizas tu código para que:

- No se rompa fácilmente
- Sea escalable
- Sea entendible
- Se pueda mantener en el tiempo

🔥 No es solo carpetas… es cómo piensas el sistema
""")

# =========================================
# ¿POR QUÉ ES CLAVE?
# =========================================
st.header("🎯 ¿Por qué es tan importante?")

st.markdown("""
Sin arquitectura:
- Rompes cosas al cambiar otras
- No sabes dónde está la lógica
- Se vuelve inmantenible

Con arquitectura:
- Puedes crecer el sistema
- Sabes dónde tocar
- Evitas errores en producción

👉 Esto es lo que te pasó varias veces en NEXUS
""")

# =========================================
# MODELO BASE (EL QUE DEBES USAR)
# =========================================
st.header("🔥 Modelo profesional recomendado")

st.code("""
project/
│
├── app.py
│
├── modules/
│   ├── database.py
│   ├── logic_movimientos.py
│   ├── logic_seriales.py
│   └── utils.py
│
├── ui/
│   ├── formularios.py
│   ├── tablas.py
│   └── dashboards.py
│
├── data/
│   └── base.db
│
└── pages/
    ├── 1_kardex.py
    ├── 2_seriales.py
    └── ...
""")

st.markdown("""
👉 Regla de oro:
- modules = lógica
- ui = interfaz
- pages = pantallas
""")

# =========================================
# SEPARACIÓN DE CAPAS
# =========================================
st.header("🧩 Separación de capas")

st.markdown("""
🔥 CAPA 1 → Base de datos  
🔥 CAPA 2 → Lógica  
🔥 CAPA 3 → Interfaz  

NUNCA mezclar todo en el mismo archivo
""")

st.code("""
# ❌ MAL
def guardar():
    # SQL + lógica + UI mezclado

# ✅ BIEN
# database.py → conexión
# logic.py → reglas
# ui.py → interfaz
""")

# =========================================
# FLUJO REAL
# =========================================
st.header("🔄 Flujo real de un sistema")

st.code("""
UI (Streamlit)
   ↓
Logic (reglas negocio)
   ↓
Database (SQLite)
""")

st.markdown("""
👉 Ejemplo real NEXUS:

Formulario → Validación → Inserción → Recalcular Kardex
""")

# =========================================
# ERRORES COMUNES
# =========================================
st.header("❌ Errores comunes")

st.markdown("""
🔴 Código gigante en un solo archivo  
🔴 Mezclar SQL con UI  
🔴 Repetir funciones  
🔴 No reutilizar lógica  
🔴 No modularizar  

👉 Resultado:
Sistema frágil
""")

# =========================================
# PRINCIPIOS CLAVE
# =========================================
st.header("📐 Principios clave")

st.markdown("""
🔥 1. Responsabilidad única  
Cada archivo hace UNA cosa  

🔥 2. Reutilización  
No copies código  

🔥 3. Claridad  
Código entendible  

🔥 4. Escalabilidad  
Pensar en crecimiento  
""")

# =========================================
# CHECKLIST
# =========================================
st.header("✅ Checklist profesional")

st.markdown("""
✔ Separé lógica y UI  
✔ Tengo módulos reutilizables  
✔ No repito código  
✔ Mi app está organizada  
✔ Puedo escalar sin romper  
""")

# =========================================
# CÓDIGO REAL EJEMPLO
# =========================================
st.header("💻 Ejemplo real")

st.markdown("🔹 database.py")

st.code("""
import sqlite3

def get_connection():
    return sqlite3.connect("data/base.db")
""")

st.markdown("🔹 logic.py")

st.code("""
def calcular_stock(stock, cantidad, afecta):
    return stock + (cantidad * afecta)
""")

st.markdown("🔹 ui.py")

st.code("""
import streamlit as st
from modules.logic import calcular_stock

st.write(calcular_stock(10, 5, -1))
""")

# =========================================
# CÓMO PRACTICAR
# =========================================
st.header("🧪 Cómo practicar")

st.markdown("""
Ejercicio:

1. Toma un script que tengas
2. Sepáralo en:
   - database
   - logic
   - ui
3. Elimina duplicados

👉 Objetivo:
Pensar como arquitecto, no como script
""")

# =========================================
# TIPS REALES
# =========================================
st.header("💡 Tips de trabajo real")

st.markdown("""
🔥 No toques lógica sin entender flujo  
🔥 Haz cambios pequeños  
🔥 Usa Git siempre  
🔥 Documenta  
🔥 Piensa antes de programar  

👉 El error más caro:
"arreglar algo y dañar otra cosa"
""")

# =========================================
# BONUS
# =========================================
st.header("🚀 BONUS")

st.markdown("""
Siguiente nivel:

- Arquitectura por capas tipo backend (MVC)
- APIs (FastAPI)
- Microservicios
- Deploy profesional

🔥 Ya es nivel empresa real
""")