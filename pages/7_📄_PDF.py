import streamlit as st

st.set_page_config(page_title="PDF", page_icon="📄", layout="wide")

st.title("📄 Procesamiento de PDF")
st.subheader("Compresión, optimización y automatización")

st.markdown("""
## ¿Para qué sirve?

- Reducir peso de PDFs
- Optimizar archivos para envío
- Automatizar procesos masivos
- Preparar documentos para almacenamiento

## ¿Dónde lo usé?

- Script de compresión de PDFs
- Automatización de carpetas
""")

st.divider()

st.markdown("## Ejemplo básico (Python)")

st.code("""
import fitz  # PyMuPDF

doc = fitz.open("archivo.pdf")
doc.save("archivo_comprimido.pdf", garbage=4, deflate=True)
""", language="python")

st.success("💡 Práctica: tomar una carpeta de PDFs y reducir su tamaño automáticamente")