import streamlit as st

st.set_page_config(page_title="SQL", page_icon="🗄️", layout="wide")

st.title("🗄️ SQL")
st.subheader("Consultas, bases de datos y análisis empresarial")

st.markdown("""
## ¿Qué es SQL?

SQL es el lenguaje usado para consultar, insertar, actualizar y analizar información guardada en bases de datos.

## ¿Para qué me sirve?

Me sirve para:

- Consultar datos reales de una empresa
- Validar información antes de llevarla a Power BI
- Crear reportes
- Revisar errores en inventarios, ventas o movimientos
- Conectar datos con Python o Power BI
""")

st.divider()

st.markdown("## Primera práctica: SELECT básico")

st.code("""
SELECT *
FROM ventas;
""", language="sql")

st.markdown("""
### ¿Qué hace?

Trae todos los registros de la tabla `ventas`.

### ¿Cuándo lo uso?

Cuando quiero revisar rápidamente qué información tiene una tabla.
""")

st.markdown("## Práctica para ti")

st.info("""
Crea una tabla llamada productos y consulta todos sus registros usando SELECT.
""")