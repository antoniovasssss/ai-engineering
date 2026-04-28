""" 
- Initialize the Pinecone connection with your API key.
- Create a new index called `"dotproduct-index"` that uses the dot product distance metric.
- List your indexes to verify that it has been created and has the correct metric.
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

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    metric='dotproduct',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())