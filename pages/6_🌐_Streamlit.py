import streamlit as st

st.set_page_config(page_title="Streamlit", page_icon="🌐", layout="wide")

st.title("🌐 Streamlit")
st.subheader("Crear aplicaciones web con Python")

st.markdown("## 📘 ¿Qué es Streamlit?")

st.markdown("""
Streamlit es una librería de Python que permite crear aplicaciones web de forma rápida.

Sirve para mostrar datos, formularios, tablas, gráficos y herramientas internas.
""")

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Crear dashboards rápidos
- Crear formularios
- Mostrar tablas
- Consultar información
- Crear apps internas
- Publicar herramientas en internet
""")

st.markdown("## 💻 Comandos esenciales")

st.code("""
import streamlit as st

st.title("Mi app")
st.subheader("Subtítulo")
st.write("Texto normal")

nombre = st.text_input("Escribe tu nombre")

if st.button("Saludar"):
    st.success(f"Hola {nombre}")

opcion = st.selectbox("Selecciona una opción", ["Python", "SQL", "Power BI"])

st.dataframe(df)
""", language="python")

st.markdown("## 🧠 Estructura básica de una app")

st.code("""
import streamlit as st

st.set_page_config(
    page_title="Mi App",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Mi primera app")

st.markdown("Bienvenido")

if st.button("Ejecutar"):
    st.success("Proceso terminado")
""", language="python")

st.markdown("## 🧪 Práctica")

st.success("""
Crea una mini app que tenga:

1. Título
2. Input de texto
3. Selectbox
4. Botón
5. Mensaje de éxito
""")

st.markdown("## ⚠️ Errores comunes")

st.warning("""
- No activar el entorno virtual
- No instalar streamlit
- Ejecutar mal el comando streamlit run app.py
- No guardar cambios antes de probar
- No subir requirements.txt a GitHub
""")