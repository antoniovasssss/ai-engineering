import os
from dotenv import load_dotenv

# LangChain imports
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.documents import Document

from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# =========================================================
# LOAD DOCUMENTS
# =========================================================

print("\nLoading documents...\n")

documents = []

from pathlib import Path

script_dir = Path(__file__).resolve().parent

data_folder = script_dir / "data"

if not data_folder.exists():
    raise FileNotFoundError(
        f"Data folder not found at {data_folder}.\n"
        "Create a 'data' directory next to exercise1.py and add the text files to load."
    )

for file_name in os.listdir(data_folder):

    file_path = data_folder / file_name

    loader = TextLoader(str(file_path), encoding="utf-8")

    docs = loader.load()

    documents.extend(docs)

print(f"Total documents loaded: {len(documents)}")

# =========================================================
# CHUNK DOCUMENTS
# =========================================================

print("\nChunking documents...\n")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# =========================================================
# CREATE EMBEDDINGS
# =========================================================

print("\nCreating embeddings model...\n")

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# =========================================================
# CREATE CHROMA VECTOR DATABASE
# =========================================================

print("\nCreating Chroma vector store...\n")

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="company_guidelines",
    persist_directory="chroma_db"
)

print("Vector database created successfully!")


# =========================================================
# CREATE RETRIEVER
# =========================================================

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# =========================================================
# USER INPUT
# =========================================================

user_input = """
hey bro,
i used chatgpt and github for this project
"""


print("\nUser Input:\n")
print(user_input)

# =========================================================
# RETRIEVE RELEVANT DOCUMENTS
# =========================================================

print("\nRetrieving relevant chunks...\n")

retrieved_docs = retriever.invoke(user_input)

for i, doc in enumerate(retrieved_docs, start=1):

    print(f"\n--- Chunk {i} ---\n")

    print(doc.page_content)


# =========================================================
# COMBINE RETRIEVED CONTEXT
# =========================================================

context = "\n\n".join([doc.page_content for doc in retrieved_docs])


# =========================================================
# CREATE PROMPT
# =========================================================

prompt = ChatPromptTemplate.from_template(
    """
You are a professional company writing assistant.

Use the provided company guidelines to fix the user text.

Guidelines:
{context}

User Text:
{input}

Return only the corrected professional version.
"""
)


# =========================================================
# CREATE LLM
# =========================================================

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4.1-mini",
    temperature=0
)


# =========================================================
# CREATE FINAL CHAIN
# =========================================================

chain = prompt | llm


# =========================================================
# GENERATE RESPONSE
# =========================================================

print("\nGenerating final response...\n")

response = chain.invoke({
    "context": context,
    "input": user_input
})


# =========================================================
# FINAL OUTPUT
# =========================================================

print("\n========== FINAL OUTPUT ==========\n")

print(response.content)

