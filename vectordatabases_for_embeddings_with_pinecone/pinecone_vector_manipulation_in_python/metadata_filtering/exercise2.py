""" 
- Initialize the Pinecone connection with your API key.
- Retrieve the **MOST** similar vector to the `vector` provided, only searching through vectors where the metadata `'year'` equals `2024`.
"""
from operator import index
import os
from pinecone import Pinecone
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
    },
    {
"id":"4",
"values": [0.5,0.6,0.7,0.8],
"metadata": {"year":2024,"genre":"action"} 
    }
]

index.upsert(vectors)

# Retrieve the MOST similar vector with the year 2024
query_vector = [0.5, 0.6, 0.7, 0.8]

query_result = index.query(
    vector=query_vector,
    top_k=1,
    filter={
      "year": {"$eq":2024},    
    }
)

print(query_result)