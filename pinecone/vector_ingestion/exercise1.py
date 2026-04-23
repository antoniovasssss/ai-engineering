""" 
- Initialize the Pinecone connection using your API key.
- Create a new serverless Pinecone index called `"data-index"`; leave the other settings as they are.
- Use a list comprehension to check that each vector in `vectors` is length `1536`, returning a single `True` or `False` indicating whether they all meet this condition.
"""
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
from openai import OpenAI

# Initialize the Pinecone client
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

vectors = [
    {
        "id": "0",
        "values": [0.025525547564029694, 0.0188823901116848],
        "metadata": {"genre": "action", "year": 2024}
    },
]


# Create your Pinecone index
pc.create_index(
    name="data-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))