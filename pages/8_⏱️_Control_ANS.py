import streamlit as st

st.set_page_config(page_title="Control ANS", page_icon="⏱️", layout="wide")

st.title("⏱️ Control ANS")
st.subheader("Sistema de control técnico, tiempos y validación operativa")

# ============================================================
# 📘 DESCRIPCIÓN GENERAL
# ============================================================

st.markdown("## 📘 ¿Qué es Control ANS?")

st.markdown("""
Control ANS es una plataforma desarrollada para automatizar y centralizar el seguimiento operativo de pedidos y actividades.

El sistema permite organizar información proveniente de diferentes zonas operativas, validar registros, calcular tiempos ANS y generar indicadores para facilitar el control y análisis de la operación.

Toda la información procesada es presentada en reportes y tableros que ayudan al usuario a realizar seguimiento operativo.
""")

# ============================================================
# 1️⃣ GENERAR INFORME ANS
# ============================================================

st.markdown("## 1️⃣ Generar Informe ANS")

st.markdown("""
Este módulo se encarga de procesar los archivos operativos provenientes de las diferentes zonas y generar el informe principal de seguimiento ANS.

Durante el proceso el sistema:

- Consolida información
- Limpia registros
- Valida fechas y estados
- Calcula tiempos ANS

Posteriormente cada pedido es clasificado automáticamente en estados como:

- 🟢 A Tiempo
- 🟠 Alerta a 0 días
- 🔴 Vencido

Finalmente se generan reportes e indicadores que permiten realizar seguimiento operativo y análisis general de la información.
""")

st.divider()
# ============================================================
# 2️⃣ VALIDACIÓN MO VS MATERIALES
# ============================================================

st.markdown("## 2️⃣ Validación MO vs Materiales")

st.markdown("""
MO significa Mano de Obra vs Materiales.

            
Este módulo igual incia desde un exporte del archivos en Fenxi, valida automáticamente que los materiales registrados correspondan correctamente a la mano de obra ejecutada en cada pedido.

El sistema realiza cruces entre pedidos, materiales y actividades para identificar posibles inconsistencias.

Finalmente, se generan reportes que permiten validar si los materiales están correctos, si sobran registros o si existe información inconsistente.
""")

st.divider()
# ============================================================
# 3️⃣ DESCARGAR EVIDENCIAS DRIVE
# ============================================================

st.markdown("## 3️⃣ Descargar Evidencias Drive")

st.markdown("""
Este módulo fue reemplazado por un proceso automatizado mediante el script `PDF_ZIP`.

Su función principal es organizar y comprimir automáticamente las evidencias PDF generadas durante la operación.

El sistema toma los archivos PDF, los agrupa y genera carpetas comprimidas (.zip) para facilitar:

- Organización de evidencias
- Reducción de espacio
- Envío de información
- cargue de pdf's al sistema Enter

Todo el proceso se realiza automáticamente para optimizar el manejo de evidencias operativas.
""")

st.divider()

# ============================================================
# 4️⃣ FORMULARIO TÉCNICO - REPORTE DE EVIDENCIAS
# ============================================================

st.markdown("## 4️⃣ Formulario Técnico - Reporte de Evidencias")

st.markdown("""
Se desarrolló un formulario en Google Forms para que los técnicos en campo puedan registrar y cargar las evidencias de las actividades ejecutadas durante la operación.

El formulario permite registrar información como:

- Nombre del técnico
- Número del pedido
- Actividad
- Estado del Pdido
- Municipio
- Rural/Urbano
- Observacion
- Evidencias en PDF

El objetivo principal es centralizar las evidencias operativas, facilitar el seguimiento de actividades.

Toda la información cargada queda almacenada automáticamente para su posterior validación y control operativo.
""")
st.divider()

# ============================================================
# 5️⃣ MOVER A PAPELERA API
# ============================================================

st.markdown("## 5️⃣ Mover a Papelera API")

st.markdown("""
Este módulo permite liberar espacio automáticamente en Google Drive después de procesar las evidencias operativas.

Su función principal es mover a la papelera los archivos que ya fueron procesados previamente mediante el sistema `PDF_ZIP`, evitando acumulación innecesaria de información.

El objetivo es optimizar el almacenamiento disponible en Google Drive, teniendo en cuenta el límite de espacio de 15 GB.

Beneficios principales:

- Liberación automática de espacio
- Mejor organización documental
- Evita acumulación de archivos
- Reduce reprocesos
- Mantiene el Drive más limpio y controlado
""")
st.divider()

# ============================================================
# 6️⃣ VISOR GEOGRÁFICO ANS
# ============================================================

st.markdown("## 6️⃣ Visor Geográfico ANS")

st.markdown("""
Este módulo permite visualizar geográficamente los pedidos y actividades operativas registradas en el sistema.

La información es presentada sobre un mapa interactivo donde cada punto representa un pedido operativo clasificado según su estado ANS.

El usuario puede realizar búsquedas, aplicar filtros y visualizar zonas con mayor cantidad de novedades o pedidos pendientes.

Estados visualizados:

- 🟢 A Tiempo
- 🟡 Alerta
- 🟠 Alerta a 0 días
- 🔴 Vencido

El objetivo principal es facilitar el seguimiento operativo y tener una visión más clara de la distribución de pedidos en campo.

Posteriormente, toda esta información es consolidada y presentada en dashboards e indicadores finales para análisis y seguimiento por parte del usuario.
""")

# ============================================================
# 📊 DASHBOARDS Y HERRAMIENTAS OPERATIVAS
# ============================================================

st.markdown("## 📊 Dashboards y herramientas operativas")

# ------------------------------------------------------------
# 1️⃣ DASHBOARD ANS OPERATIVO
# ------------------------------------------------------------

st.markdown("### 1️⃣ Dashboard ANS")

st.markdown("""
Este dashboard es el reporte principal compartido con el usuario final.

Aquí se consolida toda la información procesada por el sistema Control ANS, permitiendo visualizar indicadores, estados operativos, cantidad de pedidos y seguimiento general de la operación.

El objetivo es facilitar el análisis operativo y la toma de decisiones mediante información organizada y actualizada.
""")

# ------------------------------------------------------------
# 2️⃣ DASHBOARD ANS INTERNO
# ------------------------------------------------------------

st.markdown("### 2️⃣ Dashboard ANS EPM")

st.markdown("""
Este dashboard es utilizado de manera interna como apoyo operativo para el seguimiento de pedidos.

A diferencia del dashboard final entregado al cliente, este maneja un colchón operativo adicional que permite a los técnicos y coordinadores anticiparse a posibles vencimientos.

El objetivo es evitar esperar hasta el último día contractual para ejecutar o atender actividades operativas.

Actualmente este módulo se utiliza únicamente como apoyo interno de seguimiento.
""")

# ------------------------------------------------------------
# 3️⃣ ENRUTAMIENTO OPERATIVO
# ------------------------------------------------------------

st.markdown("### 3️⃣ Enrutamiento Operativo")

st.markdown("""
Este módulo está orientado al apoyo operativo y visualización de rutas o distribución de actividades en campo.

Actualmente se encuentra en fase de ajustes, validaciones y pruebas internas para evaluar su posible implementación dentro de la operación.

El objetivo es facilitar futuros procesos de organización y seguimiento operativo en campo según las necesidades de la operación.
""")
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