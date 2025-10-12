"""
pdf_qa_pipeline.py
------------------
Backend pipeline for Semantic PDF Q&A with LangChain, FAISS, and local models.

Uses:
- HuggingFaceEmbeddings (free, local)
- Ollama LLM (e.g., Mistral or Llama3)
- PyMuPDFLoader for fast PDF parsing

Author: Pattabhi Ramayya
License: MIT
"""

from typing import List
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()

class PDFQAPipeline:
    def __init__(
        self,
        pdf_path: str,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        llm_model: str = "mistral",
        index_path: str = "faiss_index",
    ):
        self.pdf_path = pdf_path
        self.embedding_model = embedding_model
        self.llm_model = llm_model
        self.index_path = index_path
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        self.vectorstore = None
        self.qa_chain = None

    def load_pdf(self) -> List:
        loader = PyMuPDFLoader(self.pdf_path)
        docs = loader.load()
        return docs

    def semantic_chunk(self, docs: List) -> List:
        chunker = SemanticChunker(self.embeddings)
        return chunker.split_documents(docs)

    def build_vectorstore(self, chunked_docs: List):
        self.vectorstore = FAISS.from_documents(chunked_docs, self.embeddings)

    def save_vectorstore(self):
        if self.vectorstore:
            self.vectorstore.save_local(self.index_path)

    def load_vectorstore(self):
        if os.path.exists(self.index_path):
            self.vectorstore = FAISS.load_local(
                self.index_path, self.embeddings, allow_dangerous_deserialization=True
            )
            return True
        return False

    def create_qa_chain(self, k: int = 3):
        if not self.vectorstore:
            raise ValueError("Vector store not initialized.")
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOllama(model=self.llm_model, temperature=0.3),
            retriever=retriever,
            return_source_documents=False,
        )

    def ask(self, query: str) -> str:
        if not self.qa_chain:
            raise ValueError("QA chain not initialized.")
        return self.qa_chain.run(query)

    def run_full_pipeline(self):
        docs = self.load_pdf()
        chunks = self.semantic_chunk(docs)
        self.build_vectorstore(chunks)
        self.save_vectorstore()
        self.create_qa_chain()
        return f"Pipeline setup complete for {os.path.basename(self.pdf_path)}"
