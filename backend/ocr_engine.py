import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
import fitz  # PyMuPDF
import docx

def extract_text_image(img_path):
    return pytesseract.image_to_string(Image.open(img_path))

def extract_text_pdf(file_path):
    """Extract text from all pages of a PDF using PyMuPDF."""
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def extract_text_docx(file_path):
    """Extract text from a Word (.docx) document."""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading Word file: {e}"

