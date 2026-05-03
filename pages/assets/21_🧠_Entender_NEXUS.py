import streamlit as st

st.set_page_config(page_title="Entender NEXUS", page_icon="🧠", layout="wide")

st.title("🧠 Entender NEXUS")
st.subheader("Cómo leer y comprender un sistema real sin perderse en el código")

st.markdown("""
## 🎯 Objetivo

Esta sección sirve para aprender a entender NEXUS como sistema, no solo como código.

La idea no es memorizar cada línea, sino comprender:

- Qué problema resuelve
- Cómo fluye la información
- Qué reglas de negocio existen
- Qué impacto tiene cada acción
""")

st.divider()

st.markdown("""
## 🧠 Mentalidad correcta

Un buen analista o desarrollador no se define por memorizar código.

Se define por entender cómo funciona el sistema.

### Regla clave

```text
No necesito saber cómo está escrito todo,
pero sí debo entender qué hace cada parte del sistema.
            
""")
st.divider()
st.markdown("""
🧩 Cómo leer NEXUS
NEXUS se puede entender en 3 capas:
1. Entrada
Es lo que el usuario escribe o selecciona.
Ejemplos:


Código material


Cédula técnico


Tipo de movimiento


Cantidad


Bodega


Observación


2. Proceso
Es la lógica que ejecuta el sistema.
Ejemplos:


Validar material


Calcular stock


Registrar movimiento


Crear trazabilidad


Generar Excel


Consultar SQLite


3. Salida
Es lo que el usuario ve o descarga.
Ejemplos:


Tabla en pantalla


Mensaje de éxito o error


Archivo Excel


Dashboard


Consulta Kardex
""")


st.divider()
st.markdown("""
🔍 Método práctico: Input → Proceso → Output
Cuando revises cualquier módulo, hazte estas preguntas:
INPUT
¿Qué datos recibe el sistema?
PROCESO
¿Qué validaciones o cálculos realiza?
OUTPUT
¿Qué resultado entrega al usuario?
Este método evita perderse leyendo línea por línea.
""")
st.divider()
st.markdown("""
📦 Ejemplo: Conciliación Inventario
Input
El usuario hace clic en:
Exportar plantilla conciliación
Proceso
NEXUS consulta la base de datos y obtiene:
Último movimiento de cada material en METROPOLITANA SUR
Luego genera un Excel con:


Stock Sistema


Stock Físico


Diferencia


Tipo Ajuste Sugerido


Output
El usuario descarga un Excel para comparar:
Sistema vs Físico
Y con eso decide si debe hacer:


AJUSTE ENTRADA


AJUSTE SALIDA


OK
""")


st.divider()
st.markdown("""
⚙️ Ejemplo: Ajustes Kardex
Input
El usuario ingresa:


ID Movimiento


Tipo de ajuste


Nueva cantidad correcta


Proceso
NEXUS calcula internamente la diferencia entre:
Stock actual del sistema vs nueva cantidad correcta
Output
El sistema crea un nuevo movimiento de ajuste.
Importante:
El ajuste no modifica el movimiento original.Crea un nuevo movimiento para conservar trazabilidad.
""")
st.divider()
st.markdown("""
🔥 Reglas de negocio que debo recordar


Solo METROPOLITANA SUR afecta stock real.


Las zonas son trazabilidad operativa.


Reintegro corrige entregas mal hechas.


Ajuste corrige diferencias físico vs sistema.


Serializado exige serial.


TRAS representa traslado.


TR representa transferencia.


La conciliación no es mensual: es estado actual acumulado.
""")


st.divider()
st.markdown("""
🏆 Nivel profesional
Un analista/desarrollador realmente útil puede:


Explicar el sistema sin mostrar código


Detectar errores de lógica de negocio


Validar datos contra la realidad


Proponer mejoras funcionales


Saber dónde tocar sin romper
""")


st.success("""
Conclusión:
No necesito memorizar todo el código de NEXUS.
Necesito entender cómo fluye el dato, qué regla aplica y qué resultado espera el usuario.
""")
            