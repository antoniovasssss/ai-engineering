""" 
- Combine the text features in `last_product`, and for each product in `products`, using `create_product_text()`.
- Embed the `last_product_text` and `product_texts` using `create_embeddings()`, ensuring that `last_product_embeddings` is a single list.
- Find the three smallest cosine distances and their indexes using `find_n_closest()`.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

def create_product_text(product):
    """Combine the text features of a product into a single string."""
    return f"{product['title']} {product['description']}"

def create_embeddings(texts):
    """Create embeddings for the given text(s) using OpenAI API."""
    if isinstance(texts, str):
        texts = [texts]
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    return [item.embedding for item in response.data]

def find_n_closest(embedding, embeddings_list, n=3):
    """Find the n closest embeddings using cosine distance."""
    from numpy import dot
    from numpy.linalg import norm
    
    distances = []
    for i, emb in enumerate(embeddings_list):
        distance = 1 - (dot(embedding, emb) / (norm(embedding) * norm(emb)))
        distances.append({'index': i, 'distance': distance})
    
    return sorted(distances, key=lambda x: x['distance'])[:n]

# Define last_product and products (replace with your actual data)
last_product = {'title': 'Product Name', 'description': 'Product Description'}
products = [
    {'title': 'Smartphone', 'description': 'A high-end smartphone with advanced camera features and fast processing.'},
    {'title': 'Laptop', 'description': 'A powerful laptop designed for work, gaming, and multimedia tasks.'},
    {'title': 'Bestselling Novel', 'description': 'An engaging fiction book that has topped the bestseller lists.'},
    {'title': 'Wireless Headphones', 'description': 'Noise-cancelling wireless headphones for immersive audio experience.'},
    {'title': 'Coffee Maker', 'description': 'A programmable coffee maker that brews perfect coffee every morning.'},
    {'title': 'Running Shoes', 'description': 'Comfortable and durable running shoes for athletes and fitness enthusiasts.'},
    {'title': 'Smart Watch', 'description': 'A fitness tracking smartwatch with heart rate monitor and GPS.'},
    {'title': 'Digital Camera', 'description': 'A high-quality digital camera for professional photography and videography.'},
]

# Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
product_embeddings = create_embeddings(product_texts)

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings)

for hit in hits:
  product = products[hit['index']]
  print(product['title'])