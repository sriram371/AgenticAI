"""
app.py
------
Streamlit interface for Semantic PDF Q&A using LangChain, FAISS, and local models.
Uses a hash-based FAISS index folder per uploaded PDF to avoid overwriting previous indexes.
"""

import streamlit as st
import os
import time
import hashlib
from src.pdf_qa_pipeline import PDFQAPipeline

st.set_page_config(page_title="Semantic PDF Q&A", layout="wide")
st.title("Semantic PDF Question Answering Application")

st.markdown("""
This application allows you to:
1. Upload a PDF document
2. Process and embed it using local HuggingFace embeddings
3. Ask natural language questions, answered by a local LLM (via Ollama)
Each uploaded PDF creates its own FAISS index folder based on a unique hash, ensuring older indexes are retained.
""")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

load_existing = st.checkbox("Load existing FAISS index if available", value=True)
process_button = st.button("Process and Embed PDF")

os.makedirs("uploads", exist_ok=True)
os.makedirs("faiss_index", exist_ok=True)

if "pipeline" not in st.session_state:
    st.session_state.pipeline = None
if "ready" not in st.session_state:
    st.session_state.ready = False

if uploaded_file and process_button:
    pdf_path = os.path.join("uploads", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info(f"File uploaded: {uploaded_file.name} ({uploaded_file.size / 1e6:.2f} MB)")
    st.write("Initializing the processing pipeline...")

    # Unique FAISS folder per file based on hash
    name_hash = hashlib.sha256(uploaded_file.name.encode()).hexdigest()[:12]
    index_folder = os.path.join("faiss_index", name_hash)

    pipeline = PDFQAPipeline(pdf_path=pdf_path, index_path=index_folder)
    st.session_state.pipeline = pipeline

    if load_existing and pipeline.load_vectorstore():
        st.success("Existing FAISS index loaded successfully.")
        pipeline.create_qa_chain()
        st.session_state.ready = True
    else:
        with st.spinner("Processing and embedding the PDF. This may take several minutes..."):
            start_time = time.time()
            result = pipeline.run_full_pipeline()
            end_time = time.time()
        st.success(result)
        st.write(f"Total processing time: {end_time - start_time:.2f} seconds")
        st.session_state.ready = True

if st.session_state.ready:
    st.subheader("Ask a Question About the Document")

    user_query = st.text_input("Enter your question:")
    ask_button = st.button("Submit Question")

    if ask_button and user_query.strip():
        with st.spinner("Generating answer..."):
            try:
                answer = st.session_state.pipeline.ask(user_query)
                st.markdown("**Answer:**")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Developed by Pattabhi Ramayya | Powered by LangChain, FAISS, and local models (HuggingFace + Ollama)")
