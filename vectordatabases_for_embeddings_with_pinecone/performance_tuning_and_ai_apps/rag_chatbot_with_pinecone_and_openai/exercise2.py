import os
from uuid import uuid4
from dotenv import load_dotenv
import requests
from openai import OpenAI
import pandas as pd
from pinecone import Pinecone

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index('pinecone-datacamp')

# ✅ Added: fetch and build df
url = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json"
data = requests.get(url).json()

records = []
for article in data["data"]:
    title = article["title"]
    for para in article["paragraphs"]:
        context = para["context"]
        records.append({
            "text_id": str(uuid4()),
            "title": title,
            "text": context
        })

df = pd.DataFrame(records)
df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)
print("Total documents:", len(df))

# Batching
batch_size = 100

batches = [df[i:i+batch_size] for i in range(0, len(df), batch_size)]

for batch in batches:
    ids = [str(uuid4()) for _ in range(len(batch))]
    texts = batch["text"].tolist()
    metadata = [
        {
            "title": row["title"],
            "text": row["text"]
        }
        for _, row in batch.iterrows()
    ]

    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )

    vectors = [r.embedding for r in response.data]

    index.upsert(
        vectors=list(zip(ids, vectors, metadata)),
        namespace="squad_rag_dataset"
    )

def retrieve_docs(query):
    query_embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True,
        namespace="squad_rag_dataset"
    )

    retrieved_docs = []
    
    sources = []

    for match in results["matches"]:
        retrieved_docs.append(match["metadata"]["text"])
        sources.append(match["metadata"]["title"])

    return retrieved_docs, sources

def build_prompt(query, docs):
    prompt_start = "Answer the question using the context below:\n\n"
    context = "\n\n".join(docs)
    prompt_end = f"\n\nQuestion:{query}"
    return prompt_start + context + prompt_end

def question_answering(prompt, sources):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    return {
        "answer": answer,
        "sources": sources
    }

query = "What is machine learning?"
docs, sources = retrieve_docs(query)
prompt = build_prompt(query, docs)
result = question_answering(prompt, sources)

print("Answer:\n", result["answer"])
print("\nSources:", result["sources"])