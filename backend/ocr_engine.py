# ocr_engine.py
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import docx
import pandas as pd
from backend.cleaner import extract_customers, extract_reference_numbers, extract_amounts


def extract_text_image(img_path):
    return pytesseract.image_to_string(Image.open(img_path))

def extract_text_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def extract_text_docx(file_path):
    return "\n".join([para.text for para in docx.Document(file_path).paragraphs])

def structure_to_table(text):
    customers = extract_customers(text)
    refs = extract_reference_numbers(text)
    amounts = extract_amounts(text)

    data = list(zip(customers, refs, amounts))
    return pd.DataFrame(data, columns=["Customer Name", "Ref No", "Loan Amount"])
def extract_text_docx(file_path):
    from docx import Document
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading Word file: {e}"
