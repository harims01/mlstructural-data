# export_excel.py
def save_to_excel(df, output_path="structured_output.xlsx"):
    df.to_excel(output_path, index=False)
