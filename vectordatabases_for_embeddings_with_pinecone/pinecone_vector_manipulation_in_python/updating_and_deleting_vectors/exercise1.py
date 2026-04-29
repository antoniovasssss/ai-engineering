from operator import index
import os
from pinecone import Pinecone
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

index = pc.Index('data-index')

updated_text = "A futuristic AI spy mission with robots and explosions"

# Step 1: create embedding
new_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=updated_text
).data[0].embedding

# Step 2: upsert with SAME ID
index.upsert(
    vectors=[
        {
            "id": "0",  # same id → update happens
            "values": new_embedding,
            "metadata": {
                "genre": "sci-fi",  # updated
                "year": 2025,
                "text": updated_text
            }
        }
    ]
)