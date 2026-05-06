""" 
- Initialize the Pinecone client with your API key (the OpenAI client is available as `client`).
- Create a query vector by embedding the `query` provided with the same OpenAI embedding model you used for embedding the other vectors.
- Query the `"squad_dataset"` namespace using `query_emb`, returning the top *five* most similar results.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
from pinecone import Pinecone

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

index = pc.Index('pinecone-datacamp')

df=pd.read_csv("squad_dataset.csv")

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(
    vector=query_emb,
    top_k=5,
    namespace="squad_dataset")

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')