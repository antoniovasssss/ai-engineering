""" 
- Create an OpenAI client.
- Create a request to the Embeddings endpoint, passing the `text-embedding-3-small` model any text you wish.
- Convert the model `response` into a dictionary.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

# Create a request to obtain embeddings
response = client.embeddings.create(
  model="text-embedding-3-small",
  input="This can contain any text."
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)