import streamlit as st

st.set_page_config(
    page_title="Entender Informe Actas",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Entender Informe Actas")

st.subheader(
    "Cómo actualizar y comprender el informe sin depender de la memoria"
)

st.markdown("""

## 🎯 Objetivo

Esta sección sirve para recordar cómo funciona el proceso completo de actualización del Informe Actas.

La idea no es memorizar cada paso técnico.

La idea es entender:

- De dónde vienen los datos
- Qué hace Python
- Qué hace Power Query
- Qué hace Excel
- Cómo validar que todo quedó correcto

""")

st.divider()

st.markdown("""

## 🧠 Mentalidad correcta

El Informe Actas no se construye directamente en Excel.

Excel es únicamente la capa visual.

La transformación real ocurre antes.

### Regla clave

ACTAS RAW

⬇️

Python

⬇️

ACTAS_UNIFICADAS.xlsx

⬇️

Power Query

⬇️

Informe_Actas.xlsb

Si algo sale mal, debo identificar en qué capa ocurrió el problema.

""")

st.divider()

st.markdown("""

## 🧩 Cómo funciona el sistema

El proceso tiene 4 capas.

### 1. Datos Fuente

Son las actas operativas recibidas cada mes.

Ubicación:

ACTAS_RAW

Ejemplo:

- ACTA 8
- ACTA 9
- ACTA 10

Cada archivo debe contener:

Extracción Acta

---

### 2. Transformación Python

Python es el encargado de:

- Leer todas las actas
- Unificarlas
- Limpiar registros
- Corregir pedidos
- Crear zonas
- Crear agrupaciones
- Crear reglas de negocio

Resultado:

ACTAS_UNIFICADAS.xlsx

---

### 3. Power Query

Power Query NO transforma la lógica principal.

Power Query solamente consume el archivo generado por Python.

Consultas principales:

- tbl_actas_unificadas
- consolidado_pedidos_por_municipio

---

### 4. Dashboard

Es la capa visual.

Archivo:

Informe_Actas.xlsb

Aquí existen:

- Tablas dinámicas
- Segmentadores
- Indicadores
- Dashboard de costos
- Dashboard de municipios

""")

st.divider()

st.markdown("""

## 🔍 Método práctico para actualizar el informe

### Paso 1

Recibir nuevas actas.

Copiar carpetas dentro de:

ACTAS_RAW

---

### Paso 2

Ejecutar:

python consolidar_actas.py

---

### Paso 3

Validar archivo generado:

ACTAS_UNIFICADAS.xlsx

---

### Paso 4

Abrir:

Informe_Actas.xlsb

---

### Paso 5

Seleccionar:

Datos → Actualizar Todo

---

### Paso 6

Validar resultados.

Si las consultas terminan correctamente:

✅ El informe quedó actualizado.

""")

st.divider()

st.markdown("""

## 📦 Qué columnas genera Python

Estas columnas NO vienen desde las actas.

Son creadas automáticamente por el script.

| Columna | Campo |
|----------|----------|
| AD | zona |
| AE | agrupado_por_actividad |
| AF | agrupado_actividad_region |

### Ejemplos

ALEGA → LEGALIZACIÓN

ACVIS → AGPE

ACRED → MOVIMIENTO DE REDES

AEJDO → HV

VITEC → MOVILIDAD ELECTRICA

""")

st.divider()

st.markdown("""

## 📈 Cómo construir el Dashboard Costo Ope. Vs Facturación

### 🎯 Objetivo

Este dashboard permite analizar:

- Costos Operativos
- Facturación
- Pedidos
- Municipios

por línea de negocio.

---

## 🧠 Mentalidad correcta

La construcción NO se realiza desde:

ACTAS_UNIFICADAS

La construcción se realiza desde:

Consolidado

utilizando:

- Segmentador Acta
- Segmentador Región
- Segmentador agrupado_por_actividad

---

## 🔍 Regla principal

Debo pensar siempre así:

Actividad + Región = Línea de Negocio

---

## 🏙️ HV Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = HV

Resultado:

HV MET

---

## 🏙️ Legalización Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = LEGALIZACIÓN

Resultado:

LEGALIZACIÓN MET

---

## 🏙️ Movilidad Eléctrica Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = MOVILIDAD ELECTRICA

Resultado:

MOVILIDAD ELÉCTRICA MET

---

## 🏙️ Movimiento de Redes Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = MOVIMIENTO DE REDES

Resultado:

MOVIMIENTO DE REDES MET

---

## 🏙️ Puntos de Conexión Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = PUNTOS DE CONEXIÓN

Resultado:

PUNTOS DE CONEXIÓN MET

---

## 🏙️ Técnicos GPS Metropolitano

Filtro:

- Región = METROPOLITANO
- agrupado_por_actividad = TECNICOS GPS

Resultado:

TECNICOS GPS MET

---

## 🏙️ AGPE

Filtro:

- agrupado_por_actividad = AGPE

Consolidar:

- MET
- OCC
- ORI
- SUR

Resultado:

AGPE CONSOLIDADO

Importante:

AGPE se analiza consolidado.

No se separa por región.

---

## 🏙️ HV Prepago

Filtro:

agrupado_actividad_region = HV-PREPAGO

Consolidar:

- NORDESTE
- OCCIDENTE
- ORIENTE
- SUROESTE

Resultado:

HV PREPAGO CONSOLIDADO

---

## 🏙️ Legalización Nordeste

Filtro:

- Región = NORDESTE
- agrupado_por_actividad = LEGALIZACIÓN

Resultado:

LEGALIZACIÓN NORDESTE

---

## 🏙️ Legalización Occidente

Filtro:

- Región = OCCIDENTE
- agrupado_por_actividad = LEGALIZACIÓN

Resultado:

LEGALIZACIÓN OCCIDENTE

---

## 🏙️ Legalización Oriente

Filtro:

- Región = ORIENTE
- agrupado_por_actividad = LEGALIZACIÓN

Resultado:

LEGALIZACIÓN ORIENTE

---

## 🏙️ Legalización Suroeste

Filtro:

- Región = SUROESTE
- agrupado_por_actividad = LEGALIZACIÓN

Resultado:

LEGALIZACIÓN SUROESTE

""")

st.divider()

st.markdown("""

## 🔥 Reglas de negocio que debo recordar

Python es quien crea las agrupaciones.

Power Query no debe modificar reglas.

El dashboard depende de:

- ACTAS_UNIFICADAS.xlsx

Si falla Python:

Power Query mostrará datos incorrectos.

Si falla Power Query:

El dashboard no se actualizará.

Si falla Excel:

Debo revisar:

- Tablas dinámicas
- Segmentadores
- Consultas

Siempre validar:

- Total registros
- Total pedidos
- Total municipios
- Costos
- Facturación

""")

st.divider()

st.markdown("""

## 🏆 Regla de Oro

Nunca construir el dashboard directamente desde:

ACTAS_RAW

Nunca construir el dashboard directamente desde:

ACTAS_UNIFICADAS

Siempre construirlo desde:

Consolidado

porque allí ya se encuentran aplicadas las reglas de negocio y agrupaciones generadas por Python.

""")

st.success("""

Conclusión:

No necesito recordar todos los detalles del proyecto.

Necesito recordar el flujo:

ACTAS RAW → Python → ACTAS_UNIFICADAS → Power Query → Dashboard

Si entiendo ese flujo, puedo recuperar rápidamente cualquier parte del proceso.

""")

