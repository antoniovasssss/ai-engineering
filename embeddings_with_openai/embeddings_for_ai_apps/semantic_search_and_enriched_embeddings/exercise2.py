""" 
- Define a function called `create_product_text()` to combine the `title`, `short_description`, `category`, and `features` data into a single string with the desired structure.
- Use `create_product_text()` to combine the features for each product in `products`, storing the results in a list.
- Embed the text in `product_texts`.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()
products = [
    {
        "title": "Smartphone X",
        "short_description": "A powerful smartphone with a sleek design.",
        "category": "Electronics",
        "features": ["6.5-inch display", "128GB storage", "Triple camera system"]
    },
    {
        "title": "Wireless Headphones Y",
        "short_description": "Noise-cancelling wireless headphones with long battery life.",
        "category": "Audio",
        "features": ["Active noise cancellation", "30-hour battery life", "Bluetooth 5.0"]
    },
    {
        "title": "Fitness Tracker Z",
        "short_description": "A fitness tracker that monitors your health and activity.",
        "category": "Wearables",
        "features": ["Heart rate monitoring", "Sleep tracking", "Water-resistant"]
    }
]
# Define a function to combine the relevant features into a single string
def create_product_text(product):
  return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {'; '.join(product['features'])}"""

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = client.embeddings.create(
    model="text-embedding-3-small",
    input=product_texts
)
result = product_embeddings.model_dump()
print(result)