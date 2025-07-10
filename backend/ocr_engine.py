# ocr_engine.py
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import docx

def extract_text_image(img_path):
    return pytesseract.image_to_string(Image.open(img_path))

def extract_text_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def extract_text_docx(file_path):
    return "\n".join([para.text for para in docx.Document(file_path).paragraphs])
