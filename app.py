import streamlit as st
import pandas as pd
import tempfile
import io
from backend.ocr_engine import extract_text_image, extract_text_pdf, extract_text_docx
from backend.cleaner import smart_structure
from backend.db_ops import save_to_mongo
from backend.export_excel import save_to_excel

st.set_page_config(page_title="Unstructured to Structured Extractor", layout="wide")
st.title("📄 Intelligent Document Structuring App")

uploaded_file = st.file_uploader("Upload an image / PDF / Word document", type=["png", "jpg", "jpeg", "pdf", "docx"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    try:
        if uploaded_file.type.startswith("image"):
            text = extract_text_image(temp_path)
        elif uploaded_file.type == "application/pdf":
            text = extract_text_pdf(temp_path)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_docx(temp_path)
        else:
            st.error("Unsupported file type.")
            st.stop()
    except Exception as e:
        st.error(f"Error extracting text from image: {e}")
        st.stop()

    st.subheader("🧹 Extracted Raw Text")
    st.code(text)

    st.subheader("📊 Structured Preview")
    df = smart_structure(text)
    st.dataframe(df, use_container_width=True)

    st.subheader("⬇️ Export Options")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save to MongoDB"):
            save_to_mongo(df.to_dict(orient="records"))
            st.success("Saved to MongoDB successfully!")

    with col2:
        if st.button("📥 Export to Excel"):
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)
            st.download_button(
                label="📥 Download Excel File",
                data=excel_buffer,
                file_name="structured_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
