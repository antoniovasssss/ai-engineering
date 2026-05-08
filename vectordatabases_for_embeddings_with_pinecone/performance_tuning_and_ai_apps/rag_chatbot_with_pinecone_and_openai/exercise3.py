""" 
- Initialize the Pinecone client with your API key (the OpenAI client is available as `client`).
- Extract the `'id'`, `'text'`, `'title'`, `'url'`, and `'published'` metadata from each `row`.
- Encode `texts` using `'text-embedding-3-small'` from OpenAI.
- Upsert the vectors and metadatas to a namespace called `'youtube_rag_dataset'`.
"""
import os
from uuid import uuid4
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
from pinecone import Pinecone

load_dotenv(override=True)

# Initialized the Pinecone client with API key (the OpenAI client is available as client
openai_api_key = os.getenv('OPENAI_API_KEY')

pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)

index = pc.Index('pinecone-datacamp')

youtube_df = pd.read_csv("youtube_rag_data_small.csv")
type(youtube_df)

batch_limit = 100

count = 0

# Loop through the DataFrame in batches and upsert to Pinecone
for i in range(0, len(youtube_df), batch_limit):
    batch = youtube_df.iloc[i:i+batch_limit]

    metadatas = [{
        "text_id": row['id'],
        "text": row['text'],
        "title": row['title'],
        "url": row['url'],
        "published": row['published']
    } for _, row in batch.iterrows()]

    texts = batch['text'].tolist()
    ids = [str(uuid4()) for _ in range(len(texts))]

    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )

    embeds = [list(x.embedding) for x in response.data]

    vectors = [
        {
            "id": ids[i],
            "values": embeds[i],
            "metadata": metadatas[i]
        }
        for i in range(len(ids))
    ]

    index.upsert(vectors=vectors, namespace='youtube_rag_dataset')

    count += 1
    print(f"Batch {count} uploaded")

print(index.describe_index_stats())
