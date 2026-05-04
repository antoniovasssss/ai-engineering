import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import itertools
import random

# --------------------------
# Load ENV
# --------------------------
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# --------------------------
# Init Clients
# --------------------------
client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)

index_name = "pc-2"

# --------------------------
# Create Index (if not exists)
# --------------------------
if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Thread pool for parallelism
index = pc.Index(index_name, pool_threads=10)

# --------------------------
# Generate Sample Data (Multi-Tenant)
# --------------------------
data = []

genres = ["action", "romance", "thriller", "sci-fi", "fantasy", "tech", "drama", "horror", "comedy", "history"]

tenants = ["tenant_1", "tenant_2", "tenant_3"]  # 👈 multi-tenant

for i in range(200):
    data.append({
        "id": str(i),
        "text": f"Sample story {i} about {genres[i % len(genres)]}",
        "genre": genres[i % len(genres)],
        "year": 2018 + (i % 8),
        "tenant": random.choice(tenants)  # 👈 assign tenant
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
# Parallel Upsert with Namespace
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

    # Step 2: group by namespace (VERY IMPORTANT)
    namespace_groups = {}

    for i, item in enumerate(batch):
        namespace = item["tenant"]

        vector = {
            "id": item["id"],
            "values": response.data[i].embedding,
            "metadata": {
                "genre": item["genre"],
                "year": item["year"],
                "text": item["text"]
            }
        }

        if namespace not in namespace_groups:
            namespace_groups[namespace] = []

        namespace_groups[namespace].append(vector)

    # Step 3: parallel upsert per namespace
    for namespace, vectors in namespace_groups.items():
        res = index.upsert(
            vectors=vectors,
            namespace=namespace,     # 👈 KEY LINE
            async_req=True
        )
        async_results.append(res)

# --------------------------
# Wait for all async tasks
# --------------------------
for res in async_results:
    res.get()

# --------------------------
# Stats
# --------------------------
print(index.describe_index_stats())