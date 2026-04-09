""" 
-Create a list of class descriptions from the labels in the `sentiments` dictionary using a list comprehension.
-Embed `class_descriptions` and `reviews` using the `create_embeddings()` function.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

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

# Create a list of class descriptions from the sentiment labels
class_descriptions = [sentiment['label'] for sentiment in sentiments]


# Embed the class_descriptions and reviews
class_embeddings = create_embeddings(class_descriptions)
review_embeddings = create_embeddings(reviews)