import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import os
from dotenv import load_dotenv

# -----------------------------
# Load API key
# -----------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Step 1: Create Client
# -----------------------------
client = chromadb.PersistentClient(path="./chroma_db_filter")

# Clean start
try:
    client.delete_collection("netflix_titles")
except:
    pass

collection = client.create_collection(
    name="netflix_titles",
    embedding_function=OpenAIEmbeddingFunction(
        model_name="text-embedding-3-small",
        api_key=api_key
    )
)

# -----------------------------
# Step 2: Create Dataset (Manual for teaching)
# -----------------------------
documents = [
    "Terrifier is a horror movie with a terrifying killer clown",
    "Strawberry Shortcake is a fun kids TV show full of friendship",
    "A romantic love story with emotional moments",
    "A crime thriller full of suspense and investigation",
    "A futuristic sci-fi movie with advanced technology",
    "A funny comedy movie with lots of humor",
    "A horror movie with ghosts and dark mystery",
    "A kids animated show about adventures and fun"
]

ids = [
    "id_terrifier",
    "id_strawberry",
    "id_romance",
    "id_crime",
    "id_scifi",
    "id_comedy",
    "id_horror2",
    "id_kids2"
]

# Metadata (IMPORTANT 🔥)
metadatas = [
    {"type": "Movie", "release_year": 2022},
    {"type": "TV Show", "release_year": 2019},
    {"type": "Movie", "release_year": 2021},
    {"type": "Movie", "release_year": 2020},
    {"type": "Movie", "release_year": 2023},
    {"type": "Movie", "release_year": 2018},
    {"type": "Movie", "release_year": 2022},
    {"type": "TV Show", "release_year": 2021}
]

# -----------------------------
# Step 3: Add Data
# -----------------------------
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("✅ Total documents:", collection.count())

# -----------------------------
# Step 4: MULTIPLE QUERY (User history)
# -----------------------------
print("\n🎬 USER WATCH HISTORY:")

reference_items = collection.get(
    ids=["id_terrifier", "id_strawberry"]
)

reference_texts = reference_items["documents"]

for doc in reference_texts:
    print("-", doc)

# -----------------------------
# Step 5: Multiple Query Search
# -----------------------------
results = collection.query(
    query_texts=reference_texts,
    n_results=3
)

print("\n🔍 MULTIPLE QUERY RESULTS:")

for i, query in enumerate(reference_texts):
    print(f"\n👉 Based on: {query}\n")
    
    for doc in results["documents"][i]:
        print("-", doc)

# -----------------------------
# Step 6: Remove original items (optional)
# -----------------------------
print("\n🧹 CLEANED RESULTS (remove original items):")

filtered_docs = [
    doc for doc in results["documents"][0]
    if doc not in reference_texts
]

for doc in filtered_docs:
    print("-", doc)

# -----------------------------
# Step 7: FILTERING (Only Movies)
# -----------------------------
results_filtered = collection.query(
    query_texts=reference_texts,
    n_results=3,
    where={"type": "Movie"}
)

print("\n🎥 FILTERED (Only Movies):")

for i, query in enumerate(reference_texts):
    print(f"\n👉 Based on: {query}\n")
    
    for doc in results_filtered["documents"][i]:
        print("-", doc)

# -----------------------------
# Step 8: ADVANCED FILTER ($gt)
# -----------------------------
results_recent = collection.query(
    query_texts=reference_texts,
    n_results=3,
    where={"release_year": {"$gt": 2020}}
)

print("\n📅 FILTERED (Movies after 2020):")

for i, query in enumerate(reference_texts):
    print(f"\n👉 Based on: {query}\n")
    
    for doc in results_recent["documents"][i]:
        print("-", doc)

# -----------------------------
# Step 9: AND CONDITION
# -----------------------------
results_and = collection.query(
    query_texts=reference_texts,
    n_results=3,
    where={
        "$and": [
            {"type": "Movie"},
            {"release_year": {"$gt": 2020}}
        ]
    }
)

print("\n🔥 FILTERED (Movie AND year > 2020):")

for i, query in enumerate(reference_texts):
    print(f"\n👉 Based on: {query}\n")
    
    for doc in results_and["documents"][i]:
        print("-", doc)

# -----------------------------
# Step 10: OR CONDITION
# -----------------------------
results_or = collection.query(
    query_texts=reference_texts,
    n_results=3,
    where={
        "$or": [
            {"type": "TV Show"},
            {"release_year": {"$gt": 2021}}
        ]
    }
)

print("\n🔀 FILTERED (TV Show OR year > 2021):")

for i, query in enumerate(reference_texts):
    print(f"\n👉 Based on: {query}\n")
    
    for doc in results_or["documents"][i]:
        print("-", doc)