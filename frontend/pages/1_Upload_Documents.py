import streamlit as st

st.title("📄 Upload Documents")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "docx"]
)

if uploaded_file:
    st.success(
        f"Selected: {uploaded_file.name}"
    )