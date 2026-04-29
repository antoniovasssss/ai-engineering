import os
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

# Create index (only once)
pc.create_index(
name="my-index",
dimension=4,
metric="cosine",
spec=ServerlessSpec(
cloud="aws",
region="us-east-1"
)
)

# Connect
index = pc.Index("my-index")

# Insert sample vectors
vectors= [
    {"id":"1","values": [0.1,0.2,0.3,0.4]},
    {"id":"2","values": [0.2,0.1,0.4,0.7]},
    {"id":"3","values": [0.9,0.8,0.7,0.6]},
]

index.upsert(vectors)

# Query
query_vector= [0.2,0.1,0.4,0.7]

results=index.query(
vector=query_vector,
top_k=2,
include_values=True
)

print(results)