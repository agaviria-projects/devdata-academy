import streamlit as st
import io
import contextlib

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Python Evaluador PRO", layout="wide")

st.title("🐍 Evaluador Python PRO (Ejecución Real)")
st.markdown("---")

# =========================================
# EXPLICACIÓN
# =========================================
st.info("""
💡 Escribe código Python.

Regla:
Debes imprimir el resultado usando print()
""")

# =========================================
# INPUT
# =========================================
codigo_usuario = st.text_area("✍️ Escribe tu código aquí:", height=200)

# =========================================
# FUNCIÓN SEGURA
# =========================================
def ejecutar_codigo_seguro(codigo):

    salida = io.StringIO()

    try:
        # ⚠️ entorno restringido
        entorno = {}

        with contextlib.redirect_stdout(salida):
            exec(codigo, {"__builtins__": {}}, entorno)

        return salida.getvalue(), None

    except Exception as e:
        return None, str(e)

# =========================================
# RETO
# =========================================
st.markdown("### 🎯 Reto:")
st.markdown("""
Crea una función que sume 2 números y muestre el resultado.

Ejemplo esperado:
print(5 + 5)
""")

# =========================================
# EVALUACIÓN
# =========================================
if st.button("🚀 Ejecutar y evaluar"):

    if not codigo_usuario.strip():
        st.warning("Escribe código primero")
        st.stop()

    salida, error = ejecutar_codigo_seguro(codigo_usuario)

    if error:
        st.error("❌ Error en el código")
        st.code(error)
    else:
        st.success("✅ Código ejecutado")
        st.code(salida)

        # =========================================
        # VALIDACIÓN
        # =========================================
        if "10" in salida:
            st.success("🎯 Resultado correcto")
        else:
            st.warning("⚠️ Código ejecuta pero resultado incorrecto")
            st.info("👉 Debes imprimir 10")

# =========================================
# TIPS
# =========================================
st.markdown("---")
st.header("💡 Tips")

st.markdown("""
✔ Usa print()  
✔ Evita errores de sintaxis  
✔ Prueba lógica simple  

👉 Este sistema evalúa la salida
""")