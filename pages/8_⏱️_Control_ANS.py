import streamlit as st

st.set_page_config(page_title="Control ANS", page_icon="⏱️", layout="wide")

st.title("⏱️ Control ANS")
st.subheader("Sistema de control técnico, tiempos y validación operativa")

# ============================================================
# 📘 DESCRIPCIÓN
# ============================================================

st.markdown("## 📘 ¿Qué es Control ANS?")

st.markdown("""
Control ANS es un sistema que permite:

- Validar cumplimiento de tiempos (ANS)
- Cruzar información entre FÉNIX y Excel
- Detectar inconsistencias
- Generar reportes operativos
- Preparar datos para Power BI

Tecnologías usadas:

- Python (procesamiento)
- Excel (salidas)
- Flask (formulario técnico)
- Power BI (visualización)
""")

st.divider()

# ============================================================
# 🧩 ESTRUCTURA DEL PROYECTO
# ============================================================

st.markdown("## 🧩 Estructura del sistema")

st.code("""
Control_ANS/
├── data_raw/            # Archivos originales (TXT, XLSX)
├── data_clean/          # Archivos procesados
├── dashboard/           # Archivos para Power BI
├── formularios_tecnicos/ # Web Flask
├── scripts/             # Lógica principal
├── requirements.txt
├── README.md
""")

st.divider()

# ============================================================
# 🔥 SCRIPTS PRINCIPALES
# ============================================================

st.markdown("## 🔥 Scripts clave (lo más importante)")

st.markdown("### 1. calculos_ans.py")

st.markdown("""
Procesa datos y calcula ANS:

- FECHA_LIMITE_ANS
- DIAS_TRANSCURRIDOS
- DIAS_RESTANTES
- ESTADO (VENCIDO / ALERTA / A TIEMPO)

Incluye:

- Exclusión de sábados, domingos y festivos
- Formato condicional en Excel
- Preparación para Power BI
""")

st.markdown("### 2. validar_export_almacen.py")

st.markdown("""
Cruza datos entre:

- FÉNIX
- Planilla Excel (Elite)

Hace:

- Limpieza de datos
- Estandarización columnas
- Merge (outer join)
- Cálculo diferencias

Genera:

- CONTROL_ALMACEN.xlsx
- RESUMEN
- NO_COINCIDEN
""")

st.markdown("### 3. limpieza_fenix.py")

st.markdown("""
Limpia datos de FÉNIX:

- Elimina duplicados
- Corrige tipos de datos
- Normaliza columnas
- Prepara base para cálculos ANS
""")

st.markdown("### 4. diagnostico_control.py")

st.markdown("""
Detecta problemas:

- Columnas vacías
- Datos mal tipados
- Inconsistencias
- Errores en archivos
""")

st.divider()

# ============================================================
# ⚙️ FLUJO REAL DEL SISTEMA
# ============================================================

st.markdown("## ⚙️ Flujo operativo real")

st.code("""
1. Descargar archivo FÉNIX
2. Ejecutar limpieza_fenix.py
3. Ejecutar validar_export_almacen.py
4. Ejecutar calculos_ans.py
5. Revisar Excel generado
6. Subir a Power BI
""")

st.divider()

# ============================================================
# 🧠 CONCEPTOS CLAVE
# ============================================================

st.markdown("## 🧠 Conceptos que debes dominar")

st.markdown("""
### 📅 ANS

Tiempo máximo para cumplir una actividad.

---

### 🚦 Estados

- 🔴 VENCIDO
- 🟠 ALERTA
- 🟢 A TIEMPO

---

### 📊 Diferencias

- OK
- FALTANTE EN ELITE
- EXCESO EN ELITE
""")

st.divider()

# ============================================================
# 💻 COMANDOS CLAVE
# ============================================================

st.markdown("## 💻 Comandos esenciales")

st.code("""
# Activar entorno
venv\\Scripts\\activate

# Ejecutar script
python calculos_ans.py

# Ejecutar validación
python validar_export_almacen.py

# Ver paquetes
pip freeze

# Actualizar requirements
pip freeze > requirements.txt
""")

st.divider()

# ============================================================
# ⚠️ ERRORES COMUNES
# ============================================================

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- Columnas mal nombradas
- Tipos de datos incorrectos
- Archivos mal exportados de FÉNIX
- Cruces mal hechos (merge incorrecto)
- Datos duplicados
""")

st.divider()

# ============================================================
# 🔧 DIAGNÓSTICO RÁPIDO
# ============================================================

st.markdown("## 🔧 Diagnóstico rápido")

st.markdown("""
Si algo falla:

1. Revisar archivo origen
2. Validar columnas
3. Ejecutar diagnóstico
4. Revisar diferencias
5. Validar cálculos ANS
""")

st.divider()

# ============================================================
# 🚀 INSTALACIÓN
# ============================================================

st.markdown("## 🚀 Instalación")

st.code("""
python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python calculos_ans.py
""")

st.divider()

# ============================================================
# 📌 BUENAS PRÁCTICAS
# ============================================================

st.markdown("## 📌 Buenas prácticas")

st.success("""
- No modificar archivos originales
- Trabajar siempre sobre copias
- Validar antes de entregar
- Documentar errores
- Usar nombres claros de archivos
- Versionar con Git
""")

st.divider()

# ============================================================
# 🧠 CÓMO USAR ESTE MÓDULO
# ============================================================

st.info("""
Cuando te pidan algo en Control ANS:

1. Identifica el script
2. Revisa el flujo
3. Ejecuta diagnóstico
4. Valida Excel
5. Corrige y documenta
""")