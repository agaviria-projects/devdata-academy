import streamlit as st

st.set_page_config(page_title="NEXUS Kardex", page_icon="📦", layout="wide")

st.title("📦 NEXUS / Kardex")
st.subheader("Reglas de negocio, inventario, seriales y trazabilidad")

st.markdown("""
## ¿Qué es NEXUS?

NEXUS es un sistema local tipo ERP/Kardex creado para controlar inventario, movimientos, seriales, técnicos, reintegros y trazabilidad.

## Regla clave del sistema

Solo la bodega principal `METROPOLITANA SUR` afecta el stock real.

Las demás zonas sirven para trazabilidad, pero no deben modificar el stock Kardex.
""")

st.divider()

st.markdown("## Regla de negocio: Reintegro")

st.warning("""
Si una ENTREGA AH se hizo mal, no se debe corregir con Ajuste Kardex.

La corrección correcta es hacer un REINTEGRO para conservar la trazabilidad.
""")

st.markdown("## ¿Por qué se hizo así?")

st.markdown("""
Porque el ajuste manual puede borrar o disfrazar la historia real del movimiento.

El reintegro permite saber:

- Qué se entregó
- A quién se entregó
- Qué regresó
- Cuándo regresó
- Quién hizo la corrección
""")