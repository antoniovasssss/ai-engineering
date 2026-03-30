"""
- Define a create_embeddings() function that sends an input, texts, to the embedding model, and returns a list containing the embeddings for each input text.
- Embed short_description using create_embeddings(), and extract and print the embeddings in a single list.
- Embed list_of_descriptions using create_embeddings() and print.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

# Define test data
short_description = "This is a short description"
list_of_descriptions = ["Description one", "Description two", "Description three"]

# Define a create_embeddings function
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()

  return [data['embedding'] for data in response_dict['data']]

# Embed short_description and print
print(create_embeddings(short_description)[0])

# Embed list_of_descriptions and print
print(create_embeddings(list_of_descriptions))