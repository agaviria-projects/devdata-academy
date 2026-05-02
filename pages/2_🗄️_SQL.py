import streamlit as st

st.set_page_config(page_title="SQL", page_icon="🗄️", layout="wide")

st.title("🗄️ SQL")
st.subheader("Consultas, bases de datos y análisis empresarial")

st.markdown("## 📘 ¿Qué es SQL?")

st.markdown("""
SQL es el lenguaje usado para consultar, insertar, actualizar y analizar información guardada en bases de datos.

En empresas se usa para validar datos, construir reportes, alimentar Power BI, revisar inventarios, ventas, clientes, entregas y movimientos.
""")

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Consultar datos reales de una empresa
- Filtrar información
- Unir tablas
- Agrupar resultados
- Crear reportes base para Power BI
- Validar datos antes de analizarlos
- Insertar, actualizar o eliminar registros
""")

st.divider()

st.markdown("## 💻 Comandos esenciales")

st.markdown("### 1. SELECT")

st.code("""
SELECT *
FROM ventas;
""", language="sql")

st.info("Sirve para consultar registros de una tabla.")

st.markdown("### 2. SELECT columnas específicas")

st.code("""
SELECT cliente, ciudad, total_venta
FROM ventas;
""", language="sql")

st.info("Sirve para traer solo las columnas necesarias.")

st.markdown("### 3. WHERE")

st.code("""
SELECT *
FROM ventas
WHERE ciudad = 'Medellín';
""", language="sql")

st.info("Sirve para filtrar registros según una condición.")

st.markdown("### 4. ORDER BY")

st.code("""
SELECT *
FROM ventas
ORDER BY total_venta DESC;
""", language="sql")

st.info("Sirve para ordenar resultados de mayor a menor o de menor a mayor.")

st.markdown("### 5. JOIN")

st.code("""
SELECT 
    c.nombre,
    c.ciudad,
    v.total_venta
FROM clientes c
JOIN ventas v ON c.id_cliente = v.id_cliente;
""", language="sql")

st.info("Sirve para unir información de dos tablas relacionadas.")

st.markdown("### 6. GROUP BY")

st.code("""
SELECT 
    ciudad,
    SUM(total_venta) AS ventas_totales
FROM ventas
GROUP BY ciudad;
""", language="sql")

st.info("Sirve para agrupar datos y calcular totales por categoría.")

st.markdown("### 7. HAVING")

st.code("""
SELECT 
    ciudad,
    SUM(total_venta) AS ventas_totales
FROM ventas
GROUP BY ciudad
HAVING SUM(total_venta) > 1000000;
""", language="sql")

st.info("Sirve para filtrar resultados después de agrupar.")

st.markdown("### 8. CASE")

st.code("""
SELECT 
    cliente,
    total_venta,
    CASE
        WHEN total_venta >= 1000000 THEN 'Venta alta'
        WHEN total_venta >= 500000 THEN 'Venta media'
        ELSE 'Venta baja'
    END AS categoria_venta
FROM ventas;
""", language="sql")

st.info("Sirve para crear clasificaciones condicionales.")

st.markdown("### 9. INSERT")

st.code("""
INSERT INTO clientes (id_cliente, nombre, ciudad)
VALUES (1, 'Juan Pérez', 'Medellín');
""", language="sql")

st.info("Sirve para insertar nuevos registros en una tabla.")

st.markdown("### 10. UPDATE")

st.code("""
UPDATE clientes
SET ciudad = 'Bogotá'
WHERE id_cliente = 1;
""", language="sql")

st.warning("Siempre usa WHERE en UPDATE para evitar modificar toda la tabla.")

st.markdown("### 11. DELETE")

st.code("""
DELETE FROM clientes
WHERE id_cliente = 1;
""", language="sql")

st.warning("Siempre usa WHERE en DELETE para evitar borrar todos los registros.")

st.divider()

st.markdown("## 🧠 Consultas útiles para análisis")

st.markdown("### Ventas por ciudad")

st.code("""
SELECT 
    ciudad,
    SUM(total_venta) AS total_ventas
FROM ventas
GROUP BY ciudad
ORDER BY total_ventas DESC;
""", language="sql")

st.markdown("### Top 5 productos más vendidos")

st.code("""
SELECT TOP 5
    p.nombre_producto,
    SUM(v.cantidad) AS unidades_vendidas
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.nombre_producto
ORDER BY unidades_vendidas DESC;
""", language="sql")

st.markdown("### Clientes con mayor compra")

st.code("""
SELECT 
    c.nombre,
    SUM(v.total_venta) AS total_comprado
FROM clientes c
JOIN ventas v ON c.id_cliente = v.id_cliente
GROUP BY c.nombre
ORDER BY total_comprado DESC;
""", language="sql")

st.divider()

st.markdown("## 🧪 Práctica guiada")

st.success("""
Crea tres tablas:

1. clientes
2. productos
3. ventas

Luego practica:

- Consultar ventas
- Filtrar por ciudad
- Unir clientes con ventas
- Agrupar ventas por producto
- Crear una categoría con CASE
""")

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- Olvidar el WHERE en UPDATE o DELETE
- Hacer JOIN con columnas incorrectas
- Usar GROUP BY sin incluir correctamente las columnas
- Confundir WHERE con HAVING
- No validar los datos antes de llevarlos a Power BI
- No usar alias claros para tablas y columnas
""")

st.markdown("## 📌 Tip para entrevistas")

st.info("""
En entrevistas suelen preguntar:

- Diferencia entre WHERE y HAVING
- Tipos de JOIN
- Cómo agrupar datos
- Cómo evitar duplicados
- Cómo validar totales antes de hacer un dashboard
""")