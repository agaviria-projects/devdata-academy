import streamlit as st

st.set_page_config(page_title="Excel", page_icon="📘", layout="wide")

st.title("📘 Excel")
st.subheader("Tablas, fórmulas, Power Query, macros y análisis empresarial")

st.markdown("## 📘 ¿Qué es Excel?")

st.markdown("""
Excel es una herramienta para organizar, limpiar, calcular y analizar datos.

En empresas se usa para inventarios, reportes, controles, seguimiento de casos y análisis operativo.
""")

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Crear tablas estructuradas
- Limpiar información
- Hacer cálculos con fórmulas
- Crear reportes rápidos
- Usar Power Query para transformar datos
- Automatizar tareas con macros
""")

st.markdown("## 💻 Fórmulas esenciales")

st.code("""
=SUMA(A2:A10)

=PROMEDIO(B2:B10)

=SI(C2>100;"Alto";"Bajo")

=BUSCARX(A2;TablaProductos[Codigo];TablaProductos[Nombre])

=CONTAR.SI(A2:A100;"Cumplido")

=SI.ERROR(A2/B2;0)
""", language="text")

st.markdown("## 🧠 Power Query")

st.markdown("""
Power Query sirve para limpiar y transformar datos antes de analizarlos.

Permite:

- Quitar columnas
- Cambiar tipos de datos
- Unir tablas
- Reemplazar valores
- Quitar duplicados
- Automatizar limpieza
""")

st.markdown("## 🧪 Práctica")

st.success("""
Crea una tabla con productos, cantidades y precios.

Luego calcula:

1. Total por producto
2. Estado: Alto si total > 100000
3. Conteo de productos por categoría
4. Limpieza de nombres con Power Query
""")

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No convertir rangos en tablas
- No validar tipos de datos
- Usar fórmulas manuales sin estructura
- No documentar cambios de Power Query
- No proteger archivos importantes antes de usar macros
""")