import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

response=client.embeddings.create(
model="text-embedding-3-small",
input="Machine learning is amazing"
)

result=response.model_dump()

print(result)