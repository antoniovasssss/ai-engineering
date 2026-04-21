""" 
- Import the `ServerlessSpec` class from `pinecone`.
- Initialize the Pinecone connection using your API key.
- Create a serverless index called `"my-first-index"` to hold vectors with `256` dimensions, and configure the index for the `'aws'` cloud platform in the `'us-east-1'` region.
"""
# Import the Pinecone library
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
from openai import OpenAI

# Initialize the Pinecone client
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Create your Pinecone index
pc.create_index(
    name="pc-1", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

index = pc.Index("pc-1")
# index = pc.list_indexes()
print(index)

stats = index.describe_index_stats() # Get index status and statistics
print(stats)