""" 
- Initialize the Pinecone connection with your API key.
- Connect to the `"my-first-index"` index.
- Print key statistics about the index using an index method.
"""
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
from openai import OpenAI

# Initialize the Pinecone client
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("pc-1") # Connect to the index
print(index)

# Print the index statistics
print(index.describe_index_stats())