"""Minimal RAG example: load PDF, build vector store, retrieve, and answer."""

import os
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment")

# Download PDF (kept minimal; remove if you already have the file)
PDF_URL = "https://arxiv.org/pdf/2307.09288.pdf"
PDF_PATH = Path("rag_vs_finetuning_paper.pdf")
if not PDF_PATH.exists():
    urllib.request.urlretrieve(PDF_URL, str(PDF_PATH))

# Load and chunk
loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Embeddings and vector store
embedding_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")
persist_directory = os.path.join(os.getcwd(), "chroma_db")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=persist_directory)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Prompt and LLM
prompt = ChatPromptTemplate.from_messages([
    (
        "human",
        "You are a helpful assistant. Use ONLY the context below.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
    )
])

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4.1-mini", temperature=0)

# LCEL RAG chain (minimal mapping)
rag_chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt | llm)

# Example question
question = "Tell me more about Llama 2 architecture."
response = rag_chain.invoke(question)
print(response.content)