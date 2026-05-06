""" 
- Configure the Pinecone client with your API key.
- Create a Pinecone index called `'pinecone-datacamp'` with dimensionality of `1536`.
- Connect to the newly created index and view its statistics.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print tBhe index statistics
index = pc.Index("pinecone-datacamp")

print(index.describe_index_stats())