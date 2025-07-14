import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import docx

# ✅ Explicitly set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_image(img_path):
    """
    Extract text from an image using Tesseract OCR.
    """
    try:
        return pytesseract.image_to_string(Image.open(img_path))
    except Exception as e:
        return f"Error extracting text from image: {e}"

def extract_text_pdf(file_path):
    """
    Extract text from all pages of a PDF using PyMuPDF.
    """
    try:
        doc = fitz.open(file_path)
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_docx(file_path):
    """
    Extract text from a Word (.docx) document.
    """
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading Word file: {e}"

