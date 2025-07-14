import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import docx
import platform
import os

# ✅ Automatically set tesseract path for Windows or Linux
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:  # Streamlit Cloud uses Linux
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text_image(img_path):
    try:
        return pytesseract.image_to_string(Image.open(img_path))
    except Exception as e:
        return f"Error extracting text from image: {e}"

def extract_text_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading Word file: {e}"
