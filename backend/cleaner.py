# cleaner.py
import re
import pandas as pd

def smart_structure(text: str) -> pd.DataFrame:
    """
    Extracts structured data from unstructured OCR text using regex patterns
    and dynamically generates a DataFrame with only matched columns.
    """

    # Define fields and their extraction regex
    patterns = {
        "Customer Reference Number": r"\b\d{3,5}(?:\s+[A-Z0-9]+){2,}\b",
        "Customer Name": r"(Dr|Mr|Ms|Mrs)\.?\s?[A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z\.]+(?:\s+[A-Z][a-zA-Z]+)?",
        "City/State": r"\b[A-Z][a-z]+(?:\s?[A-Z]{2})\b",
        "Purchase Value": r"\$\s?[A-Za-z\s,]+Dollars",
        "Loan Duration": r"\d{1,2}\s?(?:Years?|Months?)",
        "Interest %": r"\d{1,2}\.?\d*\s?%",
        "Guarantor Name": r"(?:Mr|Mrs|Ms|Dr)\.?\s+[A-Z][a-z]+\s+[A-Z][a-z]+"
    }

    data = {}

    for field, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            data[field] = matches  # Add only non-empty columns

    if not data:
        return pd.DataFrame({"Message": ["No structured data found."]})

    # Normalize column lengths by padding shorter columns with empty strings
    max_len = max(len(v) for v in data.values())
    for k in data:
        data[k] += [""] * (max_len - len(data[k]))

    return pd.DataFrame(data)
