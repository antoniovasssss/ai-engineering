""" 
- Calculate the cosine distance between the `query_vector` and `embedding`.
- Append a dictionary containing `dist` and its `index` to the `distances` list.
- Sort the `distances` list by the `'distance'` key of each dictionary.
- Return the first `n` elements in `distances_sorted`.
"""
import os
from scipy.spatial import distance
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

def cosine_distance(vec1, vec2): # Calculate the cosine distance between two vectors
    return distance.cosine(vec1, vec2)

def semantic_search(query_vector, embeddings, n=3): # Perform semantic search by calculating distances and returning the top n results
    distances = []
    for i, embedding in enumerate(embeddings):
            distance = cosine_distance(query_vector, embedding)
            distances.append({
                "index": i,
                "distance": distance
            })
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    return distances_sorted[:n]
