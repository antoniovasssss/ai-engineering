""" 
- Initialize the Pinecone connection with your API key.
- Retrieve the vectors with IDs in the `ids` list from the connected index.
- Create a list of dictionaries containing the metadata from each record in `fetched_vectors`.
"""
import os
from pinecone import Pinecone, ServerlessSpec
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)


index_name = "data-index"

# ✅ Step 0: Delete existing index if it has wrong dimension
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)
    print("Old index deleted!")
    time.sleep(2)

# ✅ Step 1: Create Index (only if not already created)
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=3,  # small for demo
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print("Index created!")

# ✅ Step 2: Connect to Index
index = pc.Index(index_name)

# ✅ Step 3: Insert Sample Data
vectors = [
    {"id": "1", "values": [0.1, 0.2, 0.3], "metadata": {"topic": "politics"}},
    {"id": "2", "values": [0.2, 0.3, 0.4], "metadata": {"topic": "sports"}},
    {"id": "3", "values": [0.3, 0.4, 0.5], "metadata": {"topic": "technology"}},
    {"id": "4", "values": [0.4, 0.5, 0.6], "metadata": {"topic": "business"}},
    {"id": "5", "values": [0.5, 0.6, 0.7], "metadata": {"topic": "health"}},
    {"id": "6", "values": [0.6, 0.7, 0.8], "metadata": {"topic": "education"}},
    {"id": "7", "values": [0.7, 0.8, 0.9], "metadata": {"topic": "science"}},
    {"id": "8", "values": [0.8, 0.9, 1.0], "metadata": {"topic": "finance"}}
]

# Upsert vectors
index.upsert(vectors=vectors)
print("Vectors inserted!")

# ⏳ Wait for indexing
time.sleep(5)

# ✅ Step 4: Fetch Specific Vectors
ids = ['2', '5', '8']

fetched_vectors = index.fetch(ids=ids)

# ✅ Step 5: Extract Metadata
metadatas = [
    fetched_vectors['vectors'][vector_id]['metadata']
    for vector_id in ids
]

print("Fetched Metadata:")
print(metadatas)