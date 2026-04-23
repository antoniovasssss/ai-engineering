""" 
- Initialize the Pinecone connection with your API key.
- Connect to your index called ` "data-index"`.
- Upsert `vectors` to the index.
- Print the index's descriptive statistics.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables FIRST
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

client = OpenAI(api_key=openai_api_key)

index = pc.Index("data-index")

data = [
    {"id": "0", "text": "A high-speed car chase with explosions and spies", "genre": "action", "year": 2024},
    {"id": "1", "text": "A romantic story of two people finding love in Paris", "genre": "romance", "year": 2023},
    {"id": "2", "text": "A detective solving a complex murder mystery", "genre": "thriller", "year": 2022},
    {"id": "3", "text": "A group of astronauts exploring a distant planet", "genre": "sci-fi", "year": 2025},
    {"id": "4", "text": "A young wizard discovering magical powers and destiny", "genre": "fantasy", "year": 2021},
    
    {"id": "5", "text": "A hacker trying to break into a secure government system", "genre": "tech", "year": 2024},
    {"id": "6", "text": "A family dealing with emotional struggles and relationships", "genre": "drama", "year": 2020},
    {"id": "7", "text": "A zombie outbreak threatening humanity survival", "genre": "horror", "year": 2022},
    {"id": "8", "text": "A comedy about office workers and their daily chaos", "genre": "comedy", "year": 2021},
    {"id": "9", "text": "A soldier fighting in a historical war battlefield", "genre": "war", "year": 2019},

    {"id": "10", "text": "A superhero saving the world from a powerful villain", "genre": "action", "year": 2023},
    {"id": "11", "text": "A love triangle creating emotional conflict between friends", "genre": "romance", "year": 2022},
    {"id": "12", "text": "A detective chasing a serial killer across cities", "genre": "thriller", "year": 2024},
    {"id": "13", "text": "A robot gaining consciousness and questioning humanity", "genre": "sci-fi", "year": 2025},
    {"id": "14", "text": "A magical kingdom facing war between good and evil forces", "genre": "fantasy", "year": 2023},

    {"id": "15", "text": "A startup founder building a billion-dollar tech company", "genre": "tech", "year": 2024},
    {"id": "16", "text": "A heartbreaking story of loss and personal growth", "genre": "drama", "year": 2021},
    {"id": "17", "text": "A haunted house with mysterious paranormal activities", "genre": "horror", "year": 2020},
    {"id": "18", "text": "A stand-up comedian navigating life and relationships", "genre": "comedy", "year": 2022},
    {"id": "19", "text": "A historical story about an ancient empire and its downfall", "genre": "history", "year": 2018},
]

texts = [item["text"] for item in data]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
)

vectors = [
    {
        "id": data[i]["id"],
        "values": response.data[i].embedding,
        "metadata": {
            "genre": data[i]["genre"],
            "year": data[i]["year"],
            "text": data[i]["text"]
        }
    }
    for i in range(len(data))
]

is_valid = all(len(v["values"]) == len(vectors[0]["values"]) for v in vectors)
print(is_valid)  # ✅ True