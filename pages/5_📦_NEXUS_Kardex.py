import streamlit as st

st.set_page_config(page_title="NEXUS / Kardex", page_icon="📦", layout="wide")

st.title("📦 NEXUS / Kardex")
st.subheader("Sistema de inventario, trazabilidad, seriales y control operativo")

st.markdown("""
## 📘 ¿Qué es NEXUS?

NEXUS es un sistema local tipo ERP/Kardex desarrollado con:

- **Python**
- **SQLite**
- **Streamlit**

Su objetivo es controlar inventario, movimientos, seriales, técnicos, reintegros, consultas y trazabilidad operativa.

La idea principal es reemplazar controles manuales en Excel por una herramienta más ordenada, consultable y trazable.
""")

st.divider()

st.markdown("## 🧠 Regla principal del sistema")

st.warning("""
Solo la bodega **METROPOLITANA SUR** afecta el stock real.

Las demás zonas o bodegas funcionan principalmente como trazabilidad operativa.
""")

st.markdown("""
### ¿Qué significa esto?

Si el material está en **METROPOLITANA SUR**, afecta el inventario real.

Si el material se mueve hacia una zona como ORIENTE, OCCIDENTE, NORDESTE u otra, debe quedar trazabilidad del movimiento, pero no debe alterar el stock principal como si fuera una nueva compra o entrada real.
""")

st.divider()

st.markdown("## 🧩 Módulos principales de NEXUS")

st.markdown("""
### 📦 Inventario General

Permite consultar el estado general del inventario.

Sirve para revisar:

- Materiales disponibles
- Stock actual
- Stock Kardex
- Seriales disponibles
- Movimientos asociados
- Diferencias entre sistema y físico

---

### 📊 Kardex

Muestra el historial de movimientos de un material.

Sirve para revisar:

- Entradas
- Salidas
- Reintegros
- Ajustes
- Stock antes
- Stock después
- Responsable
- Técnico
- Bodega o zona

---

### 👨‍🔧 Inventario Técnico

Permite consultar materiales asignados a técnicos.

Sirve para responder preguntas como:

- ¿Qué tiene asignado un técnico?
- ¿Qué seriales tiene?
- ¿Qué material debe reintegrar?
- ¿Qué movimientos están asociados a una cédula?

---

### 🔁 Reintegros

Permite devolver material al inventario.

Es clave para corregir errores operativos sin perder trazabilidad.

Ejemplo:

Si se entregó material a un técnico equivocado, **no se debe hacer ajuste manual**.  
Primero se debe hacer **REINTEGRO** y luego asignar correctamente.

---

### 📄 Seriales

Controla materiales serializados.

Sirve para:

- Registrar seriales
- Validar duplicados
- Consultar estado
- Saber si un serial está disponible o asignado
- Auditar movimientos de equipos únicos

---

### ⚙️ Ajustes Kardex

Permite corregir diferencias puntuales.

Debe usarse con mucho cuidado.

No debe usarse para corregir entregas operativas mal hechas si existe una trazabilidad que debe conservarse.

---

### 📈 Dashboard

Permite visualizar indicadores generales del sistema.

Puede mostrar:

- Movimientos por tipo
- Materiales más movidos
- Actividad por fechas
- Técnicos con más movimientos
- Tendencias de inventario

---

### 📚 Manual

Módulo de apoyo para explicar reglas del sistema, módulos, criterios y uso correcto.
""")

st.divider()

st.markdown("## 🔥 Reglas de negocio importantes")

st.markdown("""
### 1. Reintegro antes que ajuste

Si una entrega operativa se hizo mal, se debe corregir con **REINTEGRO**, no con ajuste manual.

Esto permite conservar:

- Quién recibió
- Qué recibió
- Cuándo recibió
- Qué regresó
- Quién corrigió

---

### 2. Serializado exige serial

Si un material es serializado, la cantidad debe coincidir con la cantidad de seriales ingresados.

Ejemplo:

Cantidad = 3  
Seriales ingresados = 3

---

### 3. Evitar duplicidad de seriales

Un serial no debe registrarse dos veces como disponible.

---

### 4. Diferenciar traslado y transferencia

Los movimientos deben conservar una observación o identificador que permita cruzar salida y entrada.

Ejemplos:

- TRAS-xxxxx → Traslado
- TR-xxxxx → Transferencia

---

### 5. Ajustes solo con control

Los ajustes deben aplicarse únicamente cuando corresponda y preferiblemente sobre la bodega principal.
""")

st.divider()

st.markdown("## 💻 Consultas SQLite útiles para diagnóstico")

st.markdown("### 1. Ver tablas existentes")

st.code("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;
""", language="sql")

st.markdown("### 2. Ver estructura de una tabla")

st.code("""
PRAGMA table_info(materiales);
PRAGMA table_info(movimientos);
PRAGMA table_info(seriales);
""", language="sql")

st.markdown("### 3. Contar registros principales")

st.code("""
SELECT 'materiales' AS tabla, COUNT(*) AS total FROM materiales
UNION ALL
SELECT 'movimientos', COUNT(*) FROM movimientos
UNION ALL
SELECT 'seriales', COUNT(*) FROM seriales
UNION ALL
SELECT 'tecnicos', COUNT(*) FROM tecnicos
UNION ALL
SELECT 'almacenes', COUNT(*) FROM almacenes;
""", language="sql")

st.markdown("### 4. Últimos movimientos registrados")

st.code("""
SELECT *
FROM movimientos
ORDER BY id_movimiento DESC
LIMIT 20;
""", language="sql")

st.markdown("### 5. Buscar material por código o nombre")

st.code("""
SELECT *
FROM materiales
WHERE codigo LIKE '%219404%'
   OR nombre LIKE '%ONT%'
   OR descripcion LIKE '%ONT%';
""", language="sql")

st.markdown("### 6. Movimientos de un material específico")

st.code("""
SELECT 
    m.id_movimiento,
    m.fecha,
    mat.codigo,
    mat.nombre,
    tm.nombre AS tipo_movimiento,
    m.cantidad,
    m.stock_antes,
    m.stock_despues,
    a.nombre AS almacen,
    m.observacion
FROM movimientos m
LEFT JOIN materiales mat ON m.id_material = mat.id_material
LEFT JOIN tipos_movimiento tm ON m.id_tipo = tm.id_tipo
LEFT JOIN almacenes a ON m.id_almacen = a.id_almacen
WHERE mat.codigo = '219404'
ORDER BY m.fecha DESC;
""", language="sql")

st.markdown("### 7. Validar stock negativo")

st.code("""
SELECT *
FROM movimientos
WHERE stock_despues < 0
ORDER BY fecha DESC;
""", language="sql")

st.markdown("### 8. Validar seriales duplicados")

st.code("""
SELECT serial, COUNT(*) AS veces
FROM seriales
GROUP BY serial
HAVING COUNT(*) > 1;
""", language="sql")

st.markdown("### 9. Seriales disponibles por material")

st.code("""
SELECT 
    mat.codigo,
    mat.nombre,
    COUNT(s.serial) AS seriales_disponibles
FROM materiales mat
LEFT JOIN seriales s 
    ON CAST(mat.id_material AS TEXT) = s.codigo_material
WHERE s.estado = 'DISPONIBLE'
GROUP BY mat.codigo, mat.nombre
ORDER BY seriales_disponibles DESC;
""", language="sql")

st.markdown("### 10. Seriales asignados")

st.code("""
SELECT *
FROM seriales
WHERE estado = 'ASIGNADO'
ORDER BY fecha DESC;
""", language="sql")

st.markdown("### 11. Buscar un serial específico")

st.code("""
SELECT *
FROM seriales
WHERE serial LIKE '%ABC123%';
""", language="sql")

st.markdown("### 12. Movimientos por técnico")

st.code("""
SELECT 
    t.cedula,
    t.nombre,
    COUNT(m.id_movimiento) AS total_movimientos
FROM movimientos m
LEFT JOIN tecnicos t ON m.id_tecnico = t.id_tecnico
GROUP BY t.cedula, t.nombre
ORDER BY total_movimientos DESC;
""", language="sql")

st.markdown("### 13. Movimientos por tipo")

st.code("""
SELECT 
    tm.nombre AS tipo_movimiento,
    COUNT(*) AS total
FROM movimientos m
LEFT JOIN tipos_movimiento tm ON m.id_tipo = tm.id_tipo
GROUP BY tm.nombre
ORDER BY total DESC;
""", language="sql")

st.markdown("### 14. Buscar movimientos por observación")

st.code("""
SELECT *
FROM movimientos
WHERE observacion LIKE '%TRAS-%'
   OR observacion LIKE '%TR-%'
ORDER BY fecha DESC;
""", language="sql")

st.markdown("### 15. Validar movimientos de una fecha")

st.code("""
SELECT *
FROM movimientos
WHERE DATE(fecha) = '2026-05-01'
ORDER BY fecha DESC;
""", language="sql")

st.divider()

st.markdown("## 🧯 Errores comunes y diagnóstico")

st.markdown("### Error: database is locked")

st.warning("""
Este error aparece cuando SQLite está bloqueado por otro proceso.

Puede pasar si:

- Hay otra ventana de Streamlit abierta
- Un script dejó conexión abierta
- DB Browser está usando la base
- Se cerró mal una ejecución
""")

st.code("""
# Ver procesos usando Python o Streamlit
tasklist | findstr python
tasklist | findstr streamlit

# Cerrar procesos
taskkill /F /IM python.exe
taskkill /F /IM streamlit.exe
""", language="bash")

st.markdown("### Liberar puerto 8503")

st.code("""
netstat -ano | findstr :8503

taskkill /PID NUMERO_PID /F
""", language="bash")

st.markdown("### Validar si la app está corriendo")

st.code("""
streamlit run app.py --server.port 8503 --server.address 0.0.0.0
""", language="bash")

st.divider()

st.markdown("## 🧱 Guía básica de instalación de NEXUS")

st.markdown("""
### 1. Estructura esperada

El proyecto puede estar en una ruta como:

```text
C:\\SIGEM
Estructura típica:

SIGEM/
├── app.py
├── requirements.txt
├── data/
│   └── sigem.db
├── modules/
├── ui/
├── scripts/
└── venv/

""")    

st.markdown("### 2. Crear entorno virtual")

st.code("""
python -m venv venv
""", language="bash")

st.markdown("### 3. Activar entorno virtual")

st.code("""
venv\Scripts\activate
""", language="bash")

st.markdown("### 4. Instalar dependencias")

st.code("""
pip install -r requirements.txt
""", language="bash")

st.markdown("### 5. Ejecutar aplicación")

st.code("""
streamlit run app.py --server.port 8503 --server.address 0.0.0.0
""", language="bash")

st.markdown("### 6. Acceso desde otro equipo en red local")

st.code("""
http://IP_DEL_EQUIPO:8503
""", language="text")

st.warning("""
Para que otros equipos puedan entrar, el firewall debe permitir el puerto usado por Streamlit.
""")

st.divider()

st.markdown("## 🧰 Comandos útiles del día a día")

st.code("""
Revisar estado de Git

git status

Guardar cambios

git add .
git commit -m "descripcion del cambio"
git push

Ver rama actual

git branch

Ejecutar app

streamlit run app.py --server.port 8503

Ver paquetes instalados

pip freeze

Actualizar requirements

pip freeze > requirements.txt
""", language="bash")

st.divider()

st.markdown("## 📌 Checklist antes de entregar o instalar")

st.success("""
Antes de instalar o entregar NEXUS en otro equipo:

1.Hacer backup de la base de datos.
2.Validar que requirements.txt esté actualizado.
3.Confirmar que la app abre localmente.
4.Confirmar que el puerto no esté ocupado.
5.Probar consultas principales.
6.Validar que sigem.db exista en la carpeta correcta.
7.Confirmar que los módulos carguen sin errores.
8.Revisar que el usuario final tenga acceso al navegador.
9.Crear acceso directo o archivo .bat si aplica.
10.Documentar cualquier cambio realizado.
""")

st.divider()

st.markdown("## 🧠 Cómo usar esta guía")

st.info("""
Cuando tengas un problema en NEXUS:

Identifica el módulo afectado.
Revisa si es inventario, seriales, técnico, reintegro o Kardex.
Ejecuta consultas SQLite de diagnóstico.
Valida reglas de negocio.
Haz backup antes de modificar datos.
Corrige con trazabilidad, no borrando información sin control.
""")