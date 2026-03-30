# Creating a Reusable Embedding Function
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

def create_embeddings(texts):

    response=client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
    )

    return [item.embedding for item in response.data]