import re
import pandas as pd

def clean_text(text: str) -> str:
    cleaned = text.replace('\n', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def extract_customers(text):
    return re.findall(r"(Dr|Mr|Ms|Mrs)\.?\s+[A-Za-z.\s]+", text)

def extract_reference_numbers(text):
    return re.findall(r"\b\d{3,5}\s+[A-Z0-9]+\b", text)

def extract_amounts(text):
    return re.findall(r"\$\s?[A-Za-z0-9\s,.]+", text)

def extract_percentages(text):
    return re.findall(r"\d+\.?\d*\s?%", text)

def extract_durations(text):
    return re.findall(r"\d+\s+(Years|Months)", text)

def structure_to_table(text):
    from itertools import zip_longest
    data = list(zip_longest(
        extract_customers(text),
        extract_reference_numbers(text),
        extract_amounts(text),
        extract_percentages(text),
        extract_durations(text),
        fillvalue="Not Found"
    ))

    return pd.DataFrame(data, columns=[
        "Customer Name", "Reference Number", "Amount", "Interest %", "Loan Duration"
    ])
