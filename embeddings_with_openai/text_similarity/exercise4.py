""" 
- Embed the text, `"soap"`, using your `create_embeddings()` custom function and extract a single list of embeddings.
- Compute the cosine distance between the `query_embedding` and the embeddings in `product`.
- Find and print the `'short_description'` of the most similar product to the search text using the cosine distances in `distances`.
"""
import os
from scipy.spatial import distance
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()

  return [data['embedding'] for data in response_dict['data']]

# Load or define products data (example structure)
products = [
    {"embedding": create_embeddings("product1")[0], "short_description": "Product 1"},
    {"embedding": create_embeddings("product2")[0], "short_description": "Product 2"},
]

# Embed the search text
search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

distances = []
for product in products:
  # Compute the cosine distance for each product description
  dist = distance.cosine(search_embedding, product["embedding"])
  distances.append(dist)

# Find and print the most similar product short_description    
min_dist_ind = np.argmin(distances)
print(products[min_dist_ind]['short_description'])