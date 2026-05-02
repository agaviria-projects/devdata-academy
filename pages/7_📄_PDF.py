import streamlit as st

st.set_page_config(page_title="PDF", page_icon="📄", layout="wide")

st.title("📄 Compresor PDF Inteligente")
st.subheader("Compresión masiva de PDFs con Python, PyMuPDF y Pillow")

st.markdown("""
## 📘 ¿Qué es este proyecto?

El **Compresor PDF Inteligente** es un script en Python creado para reducir el peso de archivos PDF de forma masiva.

Su objetivo es tomar PDFs pesados desde una carpeta, comprimirlos y guardarlos en otra carpeta, manteniendo una calidad visual aceptable.
""")

st.divider()

st.markdown("## 🎯 ¿Para qué sirve?")

st.markdown("""
- Reducir peso de PDFs
- Optimizar documentos para envío por correo
- Comprimir archivos escaneados
- Automatizar carpetas completas
- Evitar comprimir PDF por PDF manualmente
- Intentar dejar archivos por debajo de un límite, por ejemplo **20 MB**
""")

st.divider()

st.markdown("## 🧠 Librerías usadas")

st.markdown("""
### `fitz` / PyMuPDF

Sirve para abrir, leer y reconstruir PDFs página por página.

### `PIL` / Pillow

Sirve para convertir cada página del PDF en imagen y guardarla como JPEG comprimido.

### `io.BytesIO`

Permite trabajar la imagen en memoria sin crear archivos temporales innecesarios.

### `pathlib.Path`

Permite manejar rutas y carpetas de forma limpia y profesional.
""")

st.divider()

st.markdown("## ⚙️ Configuración principal")

st.code("""
carpeta_origen = Path(r"C:\\Users\\hector.gaviria\\Desktop\\PDF")
carpeta_destino = Path(r"C:\\Users\\hector.gaviria\\Desktop\\PDF_COMPRIMIDOS")

DPI = 110
JPEG_QUALITY = 35
ESCALA_GRISES = False

REINTENTO_ACTIVO = True
TARGET_KB = 20000
""", language="python")

st.markdown("""
### Explicación

- `carpeta_origen`: carpeta donde están los PDFs originales.
- `carpeta_destino`: carpeta donde se guardan los PDFs comprimidos.
- `DPI`: controla la resolución de la imagen generada por página.
- `JPEG_QUALITY`: controla la calidad del JPEG.
- `ESCALA_GRISES`: permite convertir a blanco y negro si se requiere más compresión.
- `TARGET_KB`: límite objetivo del peso final. En este caso, **20 MB**.
""")

st.divider()

st.markdown("## 🔥 Flujo del proceso")

st.markdown("""
1. Busca todos los PDF dentro de la carpeta origen.
2. Abre cada PDF con PyMuPDF.
3. Convierte cada página en imagen.
4. Comprime la imagen como JPEG.
5. Crea un nuevo PDF con esas imágenes.
6. Guarda el resultado en la carpeta destino.
7. Si el resultado sigue pesado, aplica una compresión más agresiva.
8. Si todavía supera 20 MB, aplica ajuste fino.
""")

st.divider()

st.markdown("## 💻 Código base del compresor")

st.code("""
import io
from pathlib import Path

import fitz
from PIL import Image

carpeta_origen = Path(r"C:\\Users\\hector.gaviria\\Desktop\\PDF")
carpeta_destino = Path(r"C:\\Users\\hector.gaviria\\Desktop\\PDF_COMPRIMIDOS")

carpeta_destino.mkdir(parents=True, exist_ok=True)

DPI = 110
JPEG_QUALITY = 35
ESCALA_GRISES = False

REINTENTO_ACTIVO = True
TARGET_KB = 20000
""", language="python")

st.divider()

st.markdown("## 🧩 Función principal")

st.code("""
def comprimir_pdf(pdf_path, salida, dpi, quality, grises):
    doc_origen = fitz.open(pdf_path)
    doc_nuevo = fitz.open()

    for pagina in doc_origen:
        pix = pagina.get_pixmap(dpi=dpi, alpha=False)

        modo = "RGB" if pix.n != 1 else "L"
        img = Image.frombytes(modo, [pix.width, pix.height], pix.samples)

        img = img.convert("L" if grises else "RGB")

        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality, optimize=True)

        rect = pagina.rect
        nueva = doc_nuevo.new_page(width=rect.width, height=rect.height)
        nueva.insert_image(rect, stream=buffer.getvalue())

    doc_nuevo.save(salida, garbage=3, deflate=True)
    doc_origen.close()
    doc_nuevo.close()
""", language="python")

st.markdown("""
### ¿Qué hace esta función?

Esta función toma un PDF, convierte cada página en imagen, comprime esa imagen y reconstruye un nuevo PDF.

La ventaja es que permite reducir mucho el peso cuando el PDF viene de escáner, imágenes o documentos pesados.
""")

st.divider()

st.markdown("## 🚦 Lógica de compresión inteligente")

st.markdown("""
El script usa tres niveles:

### 1. Compresión inicial

Usa:

```text
DPI = 110
JPEG_QUALITY = 35

2. Reintento agresivo

Si el resultado puede mejorar, usa:

DPI = 96
QUALITY = 25
3. Ajuste fino

Si el PDF sigue por encima de 20 MB, usa:

DPI = 90
QUALITY = 23

""")

st.divider()

st.markdown("## ⚠️ Consideraciones importantes")

st.warning("""  
Este tipo de compresión funciona muy bien con PDFs escaneados o basados en imágenes.

Puede no reducir mucho PDFs que ya vienen optimizados o que contienen texto vectorial liviano.

También puede generar ligera pérdida de nitidez, porque cada página se convierte a imagen JPEG.
""")

st.divider()

st.markdown("## 🧪 Cómo usarlo")

st.success("""

1.Crear una carpeta llamada PDF.
2.Poner allí los PDFs originales.
3.Crear o dejar que el script cree PDF_COMPRIMIDOS.
4.Ejecutar el script.
5.Revisar el resultado final.
6.Validar peso y calidad visual.
""")

st.code("""
python compresor_pdf.py
""", language="bash")

st.divider()

st.markdown("## 🧯 Errores comunes")

st.warning("""

. La carpeta origen no existe.
. No hay PDFs en la carpeta origen.
. El PDF está abierto en otro programa.
. Falta instalar PyMuPDF.
. Falta instalar Pillow.
. La ruta tiene errores.
. El archivo final sigue superando el límite objetivo.
""")

st.divider()

st.markdown("## 📦 Dependencias")

st.code("""
pip install pymupdf pillow
""", language="bash")

st.markdown("## 📌 requirements.txt")

st.code("""
PyMuPDF
Pillow
""", language="text")

st.divider()

st.markdown("## 🧠 Tips técnicos")

st.info("""

. Si quieres más calidad, sube JPEG_QUALITY.
. Si quieres menos peso, baja DPI y JPEG_QUALITY.
. Si quieres reducir mucho, activa escala de grises.
. Guarda siempre los originales.
. No sobrescribas archivos fuente.
. Valida visualmente el resultado antes de entregar.
""")

st.divider()

st.markdown("## ✅ Checklist antes de entregar PDFs comprimidos")

st.success("""

1.Verificar que todos los PDFs fueron procesados.
2.Confirmar que el peso bajó.
3.Abrir algunos PDFs comprimidos.
4.Validar que se lea bien.
5.Confirmar que no se dañaron páginas.
6.Guardar respaldo de originales.
""")                      