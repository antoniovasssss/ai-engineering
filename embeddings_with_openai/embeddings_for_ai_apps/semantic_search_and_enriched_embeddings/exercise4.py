""" 
- Create the query vector from `query_text`.
- Find the five closest distances and their corresponding indexes using the `find_n_closest()` function.
- Loop over `hits` and extract the product at each `'index'` in the `hits` list.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv
from scipy.spatial import distance

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

def create_embeddings(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return [emb.embedding for emb in response.data]

def find_n_closest(query_vector, embeddings, n=5):
    distances = distance.cdist([query_vector], embeddings, metric="cosine")[0] # Calculate cosine distances between the query vector and all embeddings
    closest_indexes = sorted(range(len(distances)), key=lambda i: distances[i])[:n]
    return [{"index": idx, "distance": float(distances[idx])} for idx in closest_indexes] # Return the five closest distances and their corresponding indexes

# Define products and compute their embeddings
products = [
    {"title": "Laptop computer"},
    {"title": "Wireless mouse"},
    {"title": "Mechanical keyboard"},
    {"title": "Gaming monitor"},
    {"title": "USB-C hub"},
]
product_embeddings = [create_embeddings(product["title"])[0] for product in products] # Compute embeddings for product titles

# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0] # Create the query vector from query_text

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, n=5) # Find the five closest distances and their corresponding indexes

print(f'Search results for "{query_text}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit['index']]
  print(product["title"])