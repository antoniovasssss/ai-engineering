""" 
- Create a list called `product_descriptions` containing the `'short_description'` for each product in `products` using a list comprehension.
- Create embeddings for each product `'short_description'` using **batching**, passing the input to the `text-embedding-3-small` model.
- Extract the embeddings for each product from `response_dict` and store them in `products` under a new key called `'embedding'`.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    }
]


# Extract a list of product short descriptions from products
product_descriptions = [product['short_description'] for product in products]

# Create embeddings for each product description
response = client.embeddings.create(
  model="text-embedding-3-small",
  input=product_descriptions
)
response_dict = response.model_dump()

# Extract the embeddings from response_dict and store in products
for i, product in enumerate(products):
    product['embedding'] = response_dict['data'][i]['embedding']
    
print(products[0].items())