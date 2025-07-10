# cleaner.py
import re
import pandas as pd

def clean_text(text):
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r" +", " ", text)
    return text.strip()
def structure_to_table(text):
    lines = text.split('\n')
    data = []

    for line in lines:
        if ":" in line:
            parts = line.split(":")
            key = parts[0].strip()
            value = ":".join(parts[1:]).strip()  # rejoin in case multiple colons
            data.append([key, value])

    return pd.DataFrame(data, columns=["Field", "Value"])
