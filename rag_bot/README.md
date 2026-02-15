RAG Application with LangChain, Ollama, and FAISS

A Retrieval-Augmented Generation (RAG) application that allows users to query PDF documents using local embeddings and vector search. This system processes PDFs, stores embeddings in a FAISS vector database, and retrieves relevant information to answer questions.

This project runs fully locally using Ollama embeddings, making it private, fast, and cost-efficient.

🚀 Features

📄 Load and process PDF documents

✂️ Split documents into semantic chunks

🧠 Generate embeddings using Ollama (nomic-embed-text)

🗄️ Store embeddings in FAISS vector database

🔎 Retrieve relevant document chunks

🤖 Answer questions using Retrieval-Augmented Generation

🔒 Fully local (no external API required)

🏗️ Architecture
PDF Documents
      │
      ▼
Document Loader (LangChain)
      │
      ▼
Text Splitter
      │
      ▼
Embeddings (Ollama)
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
LLM / QA Chain
      │
      ▼
Answer

📂 Project Structure
rag_application/
│
├── listentoyourgut/        # PDF documents folder
│
├── rag.ipynb               # Main notebook
│
├── ragenv/                 # Virtual environment
│
├── README.md
│
└── requirements.txt

⚙️ Installation
1. Clone the repository
git clone https://github.com/zeinabkobaissi/rag_bot.git
cd rag_bot

2. Create virtual environment
python -m venv ragenv


Activate environment:

Windows:

ragenv\Scripts\activate


Linux / Mac:

source ragenv/bin/activate

3. Install dependencies
pip install langchain
pip install langchain-community
pip install langchain-ollama
pip install faiss-cpu
pip install pypdf
pip install numpy
pip install transformers

4. Install Ollama

Download and install Ollama:

https://ollama.com

Run Ollama locally:

ollama serve


Pull embedding model:

ollama pull nomic-embed-text

▶️ Usage
Step 1: Add PDF documents

Place your PDF files inside:

listentoyourgut/

Step 2: Load documents
loader = PyPDFDirectoryLoader('./listentoyourgut/')
docs = loader.load()

Step 3: Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(docs)

Step 4: Create embeddings
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434/"
)

Step 5: Store in FAISS
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

Step 6: Create retriever
retriever = vectorstore.as_retriever()

Step 7: Ask questions
query = "What is Crohn's disease?"

docs = retriever.get_relevant_documents(query)

print(docs[0].page_content)

🧠 Example Workflow

Input:

"What are the symptoms?"


Process:

Embedding created

FAISS searches similar chunks

Relevant content retrieved

Answer generated

Output:

Relevant paragraph from PDF

🛠️ Technologies Used

LangChain

Ollama

FAISS

Python

Transformers

NumPy

PyPDF

📊 Why RAG?

RAG improves LLM responses by grounding answers in real documents.

Benefits:

Reduces hallucinations

Uses real data

Works with private data

No retraining required

🔒 Runs Fully Locally

No cloud required.

Your data never leaves your machine.

📈 Future Improvements

Add chat interface (Streamlit)

Add persistent FAISS storage

Support multiple documents

Add web UI

Add LLM answer generation
