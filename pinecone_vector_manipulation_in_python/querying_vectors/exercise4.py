from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import os
import time
from dotenv import load_dotenv 

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

# Step 0: Recreate index with correct dimension (1536 for OpenAI embeddings)
index_name = 'data-index'
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)
    print("Old index deleted!")
    time.sleep(2)

pc.create_index(
    name=index_name,
    dimension=1536,  # OpenAI embeddings use 1536 dimensions
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)
print("Index created with dimension 1536!")
time.sleep(5)

# Step 1: Query text
query = "space adventure with astronauts"

# Step 2: Convert to embedding
query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

index = pc.Index('data-index')


# Step 3: Search in Pinecone
results = index.query(
    vector=query_embedding,
    top_k=3,
    include_metadata=True
)

# Step 4: Show results
for match in results["matches"]:
    print("Score:", match["score"])
    print("Text:", match["metadata"]["text"])
    print("Genre:", match["metadata"]["genre"])
    print("Year:", match["metadata"]["year"])
    print("-" * 40)