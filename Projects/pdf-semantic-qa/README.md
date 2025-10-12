# Semantic PDF Question Answering (Local, Offline, Multi-Document)

This project implements an **offline semantic search and question-answering system** for PDF documents using **LangChain**, **FAISS**, **Hugging Face embeddings**, and **Ollama-based local LLMs** (for example, Mistral).  
Each uploaded PDF creates a **unique FAISS index folder** using a hash-based naming system, so multiple documents can be stored and queried independently.

---

## Key Features

- Fully **offline operation** after models are downloaded  
- Uses **Hugging Face Sentence Transformers** for embeddings  
- Employs **Ollama** to run local large language models (LLMs)  
- **FAISS vector indexing** for fast semantic search  
- **Streamlit** app interface for interactive document Q&A  
- **Hash-based FAISS directories** to preserve all processed PDFs  
- **Jupyter notebook** included for research and testing  

---

## System Requirements

- **Python 3.10+**
- **Ollama installed locally**  
  Download from: [https://ollama.com/download](https://ollama.com/download)
- **Mistral model pulled via Ollama**

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/semantic-pdf-qa.git
cd semantic-pdf-qa
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# OR
source venv/bin/activate       # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Configure Ollama

Ollama is required to run the LLM (like Mistral) **locally**.

#### a. Download Ollama
Go to [https://ollama.com/download](https://ollama.com/download)  
and install it for your operating system.

#### b. Pull the Mistral model
After installing Ollama, open a terminal and run:
```bash
ollama pull mistral
```

#### c. Start the Ollama server
Once the model is downloaded, start the Ollama backend:
```bash
ollama serve
```

> **Note:** If you see  
> `Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address...`,  
> it means Ollama is already running — you can proceed directly to the next step.

---

## Running the Application

### Step 1. Start the Ollama Server
Make sure Ollama is running before launching your Streamlit app:
```bash
ollama serve
```

If Ollama is already running in the background, skip this step.

### Step 2. Launch the Streamlit App
In your virtual environment:
```bash
streamlit run app.py
```

### Step 3. Use the Application
1. Upload a PDF file.  
2. Wait for the system to embed and index the document.  
3. Ask natural language questions about the content.  

Each PDF generates its own FAISS folder inside `faiss_index/`, ensuring previous indexes are not overwritten.

---

## Using the Jupyter Notebook

Alternatively, you can experiment using the included notebook:

```bash
jupyter notebook
```

Then open:
```
semantic_pdf_qa_pipeline.ipynb
```
and follow the cells sequentially to load, embed, and query a PDF.

---

## FAISS Index Behavior

- Each uploaded PDF gets its own unique hash-based FAISS folder.  
- Example:
  ```
  faiss_index/
  ├── 3f29bdf1ac43/
  ├── 7a1dc442ef22/
  ```
- This ensures every processed document is saved independently.

---

## Models Used

| Component | Model | Source | API Key Required |
|------------|--------|---------|------------------|
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 | Hugging Face | No |
| LLM | mistral | Ollama (local) | No |

---

## File Structure

```
semantic-pdf-qa/
├── src/
│   └── pdf_qa_pipeline.py         # Core backend pipeline
├── app.py                         # Streamlit frontend
├── notebooks/
│   └── semantic_pdf_qa_pipeline.ipynb
├── data/                          # PDFs
├── faiss_index/                   # FAISS vector stores
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .env (optional)                # Environment variables
```

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|--------|-----------|
| `ollama not recognized` | Ollama not installed or PATH not set | Install Ollama from [ollama.com/download](https://ollama.com/download) |
| `bind: Only one usage of each socket address` | Ollama already running | Skip `ollama serve` — proceed to run the app |
| `Connection refused to localhost:11434` | Ollama not started | Run `ollama serve` before `streamlit run app.py` |
| PDF not loading | File path issue | Ensure file is uploaded correctly or use absolute path |

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this code with proper attribution.

---

## Author

**Pattabhi Ramayya**  
AI and Agentic Systems Developer  
