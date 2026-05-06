""" 
- Initialize the Pinecone client with your API key (the OpenAI client is already available as `client`).
- Extract the `'id'`, `'text'`, and `'title'` metadata from each `row` in the batch.
- Encode `texts` using `'text-embedding-3-small'` from OpenAI with dimensionality `1536`.
- Upsert the vectors and metadatas to a namespace called `'squad_dataset'`.
"""
import os
from uuid import uuid4
from dotenv import load_dotenv
import numpy as np
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

batch_limit = 100

for i in range(0, len(df), batch_limit):
    batch = df.iloc[i:i + batch_limit]
    
    metadatas = [{
        "text_id": row['id'],
        "text": row['text'],
        "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')