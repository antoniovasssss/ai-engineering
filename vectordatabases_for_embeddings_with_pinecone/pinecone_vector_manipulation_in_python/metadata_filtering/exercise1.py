import os
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

index=pc.Index("my-index")

# Insert vectors with metadata
vectors= [
    {
"id":"1",
"values": [0.1,0.2,0.3,0.4],
"metadata": {"year":2018,"genre":"action"}
    },
    {
"id":"2",
"values": [0.2,0.3,0.4,0.5],
"metadata": {"year":2020,"genre":"documentary"}
    },
    {
"id":"3",
"values": [0.9,0.8,0.7,0.6],
"metadata": {"year":2022,"genre":"documentary"}
    }
]

index.upsert(vectors)

# Query with filter
query_vector= [0.2,0.3,0.4,0.5]

results=index.query(
vector=query_vector,
top_k=2,
filter={
"year": {"$gt":2019},
"genre": {"$eq":"documentary"}
    },
include_metadata=True
)

print(results)