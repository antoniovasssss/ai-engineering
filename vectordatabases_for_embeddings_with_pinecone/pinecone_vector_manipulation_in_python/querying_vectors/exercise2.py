""" 
- Initialize the Pinecone connection with your API key.
- Retrieve the *three* records with vectors that are most similar to `vector`.
"""
import os
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

index = pc.Index('my-index')

vector= [0.2,0.1,0.4,0.7]

# Retrieve the top three most similar records
query_result = index.query(
    vector=vector,
    top_k=3
)

print(query_result)