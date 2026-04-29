""" 
- Initialize the Pinecone connection with your API key.
- Delete the index you've been working with: `"my-first-index"`.
- List your indexes to verify it has been deleted.
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

# Delete your Pinecone index
pc.delete_index("pc-1")

# List your indexes
print(pc.list_indexes())