import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import itertools

# Load env
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Init clients
client = OpenAI(api_key=openai_api_key)

pc = Pinecone(api_key=pinecone_api_key)

index_name = "pc-2"

# Create index (only if not exists)
if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Connect to index with parallel threads
index = pc.Index(index_name, pool_threads=10)

# --------------------------
# Generate sample data
# --------------------------
data = []

genres = ["action", "romance", "thriller", "sci-fi", "fantasy", "tech", "drama", "horror", "comedy", "history"]

for i in range(200):
    data.append({
        "id": str(i),
        "text": f"Sample story {i} about {genres[i % len(genres)]} with interesting plot",
        "genre": genres[i % len(genres)],
        "year": 2018 + (i % 8)
    })

# --------------------------
# Helper: chunking
# --------------------------
def chunks(iterable, batch_size):
    iterator = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(iterator, batch_size))
        if not chunk:
            break
        yield chunk

# --------------------------
# Parallel Upsert Logic
# --------------------------
batch_size = 50
async_results = []

for batch in chunks(data, batch_size):

    texts = [item["text"] for item in batch]

    # Step 1: embeddings
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )

    # Step 2: prepare vectors
    vectors = [
        {
            "id": batch[i]["id"],
            "values": response.data[i].embedding,
            "metadata": {
                "genre": batch[i]["genre"],
                "year": batch[i]["year"],
                "text": batch[i]["text"]
            }
        }
        for i in range(len(batch))
    ]

    # Step 3: PARALLEL UPSERT
    res = index.upsert(vectors=vectors, async_req=True)
    async_results.append(res)

# --------------------------
# Wait for all to finish
# --------------------------
for res in async_results:
    res.get()

# --------------------------
# Stats
# --------------------------
print(index.describe_index_stats())