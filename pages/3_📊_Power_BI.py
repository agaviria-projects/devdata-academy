import streamlit as st

st.set_page_config(page_title="Power BI", page_icon="📊", layout="wide")

st.title("📊 Power BI")
st.subheader("Dashboards, modelo de datos, DAX y análisis visual")

st.markdown("## 📘 ¿Qué es Power BI?")

st.markdown("""
Power BI es una herramienta de Microsoft para transformar datos en reportes visuales e interactivos.

Permite conectar fuentes como Excel, SQL Server, CSV o bases de datos, modelar la información y crear dashboards.
""")

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Crear dashboards empresariales
- Analizar ventas, inventarios, tiempos y cumplimiento
- Conectar datos desde SQL, Excel o archivos
- Crear indicadores KPI
- Automatizar reportes visuales
""")

st.markdown("## 🧠 Conceptos clave")

st.markdown("""
### Modelo estrella

Se compone de:

- **Tabla de hechos:** contiene datos transaccionales, por ejemplo ventas, movimientos o entregas.
- **Tablas de dimensión:** contienen información descriptiva, por ejemplo clientes, productos, técnicos, fechas o zonas.

### Medidas DAX

Las medidas permiten hacer cálculos dinámicos en los reportes.
""")

st.markdown("## 💻 Medidas DAX esenciales")

st.code("""
Ventas Totales = SUM(Ventas[Total])

Cantidad Total = SUM(Ventas[Cantidad])

Promedio Venta = AVERAGE(Ventas[Total])

Total Clientes = DISTINCTCOUNT(Clientes[IdCliente])

Ventas 2025 =
CALCULATE(
    [Ventas Totales],
    YEAR(Calendario[Fecha]) = 2025
)

Ventas Año Anterior =
CALCULATE(
    [Ventas Totales],
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)

Variación Ventas =
[Ventas Totales] - [Ventas Año Anterior]

% Variación Ventas =
DIVIDE(
    [Variación Ventas],
    [Ventas Año Anterior],
    0
)
""", language="text")

st.markdown("## 🧪 Práctica")

st.success("""
Crea un dashboard con:

1. Tarjeta de ventas totales
2. Gráfico de ventas por ciudad
3. Gráfico de ventas por producto
4. Segmentador por año
5. Medida de promedio de venta
6. Medida de variación frente al año anterior
""")

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No crear relaciones entre tablas
- Usar columnas calculadas cuando debería ser una medida
- No crear tabla calendario
- Cargar datos sucios sin limpiar
- No validar totales contra la fuente original
- Usar SUM donde corresponde DISTINCTCOUNT o AVERAGE
""")