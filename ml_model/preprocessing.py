import pandas as pd

def prepare_features(df):
    # Replace missing values
    df = df.fillna("")

    # Example: Convert Amount to number
    df["Amount"] = df["Amount"].str.replace(",", "").str.extract(r"(\d+\.?\d*)").astype(float)

    # Convert categories to lowercase
    df["Customer Name"] = df["Customer Name"].str.lower()

    return df
