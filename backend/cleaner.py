import re
import pandas as pd

def clean_text(text: str) -> str:
    """Clean the raw extracted text."""
    cleaned = text.replace('\n', ' ')                  # Remove newlines
    cleaned = re.sub(r'\s+', ' ', cleaned)             # Collapse multiple spaces
    cleaned = cleaned.strip()
    return cleaned

def structure_to_table(text: str) -> pd.DataFrame:
    """
    Convert cleaned text into line-by-line readable format.
    Each sentence or block becomes a row in a one-column DataFrame.
    """
    # Break text into sentences or key blocks
    lines = re.split(r'(?<=[.?!])\s+', text)
    lines = [line.strip() for line in lines if line.strip()]
    return pd.DataFrame({"Extracted Info": lines})



