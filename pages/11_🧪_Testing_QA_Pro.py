import streamlit as st
import pandas as pd

# =========================================
# CONFIGURACIÓN
# =========================================
st.set_page_config(page_title="Testing QA Pro", layout="wide")

st.title("🧪 Testing & QA - Nivel Profesional")
st.markdown("---")

# =========================================
# ¿QUÉ ES?
# =========================================
st.header("🧠 ¿Qué es Testing / QA?")

st.markdown("""
Testing (QA) es validar que tu sistema funcione correctamente antes de que lo use el usuario.

👉 No es solo probar manualmente:
Es tener un método para asegurar calidad.

🔥 En tu caso:
- NEXUS
- Scripts Python
- Dashboards

Todo debe validarse antes de producción.
""")

# =========================================
# ¿POR QUÉ ES CLAVE?
# =========================================
st.header("🎯 ¿Por qué es tan importante?")

st.markdown("""
Sin QA:
- Rompes funcionalidades sin darte cuenta
- Datos incorrectos
- Errores en producción

Con QA:
- Detectas errores antes del usuario
- Sistema confiable
- Mejor portafolio profesional

👉 Esto es lo que evita que “arregles algo y dañes otra cosa”
""")

# =========================================
# TIPOS DE TESTING
# =========================================
st.header("🔍 Tipos de Testing")

st.markdown("""
🔥 1. Manual  
Probar la app como usuario  

🔥 2. Unitario  
Probar funciones individuales  

🔥 3. Integración  
Probar flujo completo  

🔥 4. Validación de datos  
Verificar que los datos sean correctos  
""")

# =========================================
# CASO REAL NEXUS
# =========================================
st.header("📦 Caso real: NEXUS")

st.markdown("""
Ejemplo de QA real:

✔ Entrada de 200 unidades  
✔ Salida de 50  
✔ Reintegro de 50  

👉 Resultado esperado:
Stock final = 200

👉 Validaciones:
- Kardex correcto
- Seriales disponibles correctos
- Movimientos correctos
""")

# =========================================
# TEST UNITARIO
# =========================================
st.header("⚙️ Test unitario")

st.markdown("""
Validar funciones individuales
""")

def calcular_stock(stock, cantidad, afecta):
    return stock + (cantidad * afecta)

resultado = calcular_stock(100, 10, -1)

st.code("""
def calcular_stock(stock, cantidad, afecta):
    return stock + (cantidad * afecta)
""")

st.write("Resultado esperado: 90")
st.success(f"Resultado obtenido: {resultado}")

# =========================================
# VALIDACIÓN DE DATOS
# =========================================
st.header("📊 Validación de datos")

st.markdown("""
Evitar errores en datos
""")

df = pd.DataFrame({
    "producto": ["A", "B", "C"],
    "stock": [10, -5, 20]
})

st.dataframe(df)

errores = df[df["stock"] < 0]

if not errores.empty:
    st.error("❌ Hay stocks negativos")
    st.dataframe(errores)

# =========================================
# CHECKLIST QA
# =========================================
st.header("✅ Checklist QA")

st.markdown("""
✔ Probé flujo completo  
✔ Validé datos  
✔ Revisé errores  
✔ Probé casos extremos  
✔ Validé resultados esperados  
""")

# =========================================
# ERRORES COMUNES
# =========================================
st.header("❌ Errores comunes")

st.markdown("""
🔴 No probar antes de subir  
🔴 Probar solo casos normales  
🔴 No validar datos  
🔴 Confiar en que “funciona”  

👉 Resultado:
Errores en producción
""")

# =========================================
# PRÁCTICA
# =========================================
st.header("🧪 Cómo practicar")

st.markdown("""
Ejercicio:

1. Crear función de cálculo
2. Probar con distintos casos:
   - normal
   - cero
   - negativo
3. Validar resultados

👉 Objetivo:
Pensar como QA
""")

# =========================================
# TIPS REALES
# =========================================
st.header("💡 Tips de trabajo real")

st.markdown("""
🔥 Siempre prueba antes de commit  
🔥 Usa datos reales  
🔥 Valida casos extremos  
🔥 Documenta pruebas  

👉 QA no es opcional
""")

# =========================================
# BONUS
# =========================================
st.header("🚀 BONUS")

st.markdown("""
Siguiente nivel:

- pytest (testing automático)
- CI/CD
- Validaciones automáticas

🔥 Nivel empresa
""")