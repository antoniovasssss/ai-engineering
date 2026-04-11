import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import random
import tiktoken
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Step 1: Create Client
# -----------------------------
client = chromadb.PersistentClient()

# साफ start (avoid duplicate error)
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
# Step 2: Generate Sample Data
# -----------------------------
titles = ["Shadow", "Empire", "Mystery", "Legend", "Game", "Chronicles", "Quest"]
types = ["Movie", "TV Show"]
genres = ["Crime", "Comedy", "Drama", "Sci-Fi", "Thriller", "Romance", "Action", "Horror"]

descriptions = [
    "A gripping story of power and betrayal",
    "A hilarious journey of friendship",
    "A dark mystery unfolds over time",
    "A futuristic world controlled by technology",
    "A love story that defies all odds",
    "A dangerous mission with unexpected twists",
    "A survival game where only one wins"
]

ids = []
documents = []

# generate 1000 records
for i in range(1000):  
    title = f"{random.choice(titles)} {random.randint(1, 100)}"
    show_type = random.choice(types)
    genre = random.choice(genres)
    description = random.choice(descriptions)

    doc = f"""
    Title: {title} ({show_type})
    Description: {description}
    Categories: {genre}
    """

    ids.append(f"id_{i}")
    documents.append(doc)

# -----------------------------
# Step 3: Add to Collection
# -----------------------------
collection.add(ids=ids, documents=documents)

# -----------------------------
# Step 4: Check Data
# -----------------------------
print("Total documents:", collection.count())
print("\nSample documents:\n", collection.peek()["documents"][:2])

# -----------------------------
# Step 5: Token Cost Estimation
# -----------------------------
enc = tiktoken.encoding_for_model("text-embedding-3-small")

total_tokens = sum(len(enc.encode(doc)) for doc in documents)
cost_per_1k_tokens = 0.00002
cost = cost_per_1k_tokens * total_tokens / 1000

print("\nTotal tokens:", total_tokens)
print("Estimated cost: $", cost)

# -----------------------------
# Step 6: Query (Recommendation)
# -----------------------------
query = "crime and betrayal story"

results = collection.query(
    query_texts=[query],
    n_results=5
)

print("\n🔍 Query:", query)
print("\n🎬 Recommendations:")

for doc in results["documents"][0]:
    print("-", doc.strip(), "\n")