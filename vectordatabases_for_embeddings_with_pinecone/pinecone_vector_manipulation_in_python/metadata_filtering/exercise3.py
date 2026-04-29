""" 
- Initialize the Pinecone connection using your API key.
- Retrieve the MOST similar vector to the vector provided, only searching through vectors where the the "genre" metadata is "thriller" and "year" is less than 2018.
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

index = pc.Index('data-index')

# Generate embeddings using OpenAI
texts = [
    "A thriller movie from 2004",
    "A documentary from 2020",
    "A documentary from 2022",
    "An action movie from 2024"
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
)

# Extract embeddings
embeddings = [item.embedding for item in response.data]

vectors = [
    {
        "id": "1",
        "values": embeddings[0],
        "metadata": {"year": 2004, "genre": "thriller"}
    },
    {
        "id": "2",
        "values": embeddings[1],
        "metadata": {"year": 2020, "genre": "documentary"}
    },
    {
        "id": "3",
        "values": embeddings[2],
        "metadata": {"year": 2022, "genre": "documentary"}
    },
    {
        "id": "4",
        "values": embeddings[3],
        "metadata": {"year": 2024, "genre": "action"}
    }
]

index.upsert(vectors)

# Query with filter - genre is thriller AND year < 2018
query_text = "A thriller movie from 2004"

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[query_text]
)
query_vector = query_response.data[0].embedding

results = index.query(
    vector=query_vector,
    top_k=1,
    filter={
        "genre": {"$eq": "thriller"},
        "year": {"$lt": 2018}
    },
    include_metadata=True
)

print(results)