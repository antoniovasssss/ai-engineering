""" 
- Define a function called `find_closest()` that returns the distance and index of the most similar embedding to the `query_vector`.
- Use `find_closest()` to find the closest distance between each review's embeddings and the `class_embeddings`.
- Use the `'index'` of `closest` to subset `sentiments` and extract the `'label'`.
"""
import os
from scipy.spatial.distance import cosine
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def create_embeddings(texts):
    """Create embeddings for a list of texts using OpenAI API."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]
sentiments = [{'label': 'Positive'},
              {'label': 'Neutral'},
              {'label': 'Negative'}]
reviews = ["The food was delicious!",
           "The service was a bit slow but the food was good",
           "The food was cold, really disappointing!"]
topic_descriptions = ["Food quality", "Service speed", "Overall experience"]
topic_embeddings = create_embeddings(topic_descriptions)
review_embeddings = create_embeddings(reviews)
class_embeddings = create_embeddings([s['label'] for s in sentiments])

# Define a function to return the minimum distance and its index
def find_closest(query_vector, embeddings):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
  return min(distances, key=lambda x: x["distance"])

for index, review in enumerate(reviews):
  # Find the closest distance and its index using find_closest()
  closest = find_closest(review_embeddings[index], class_embeddings)
  # Subset sentiments using the index from closest
  label = sentiments[closest['index']]['label']
  print(f'"{review}" was classified as {label}')