import os
from uuid import uuid4
from dotenv import load_dotenv
import requests          # ← fixed
from openai import OpenAI
import pandas as pd
from pinecone import Pinecone

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)

index = pc.Index('pinecone-datacamp')

url = "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json"

data = requests.get(url).json()

records = []

for article in data["data"]:
    title = article["title"]
    for para in article["paragraphs"]:   # ← fixed indentation
        context = para["context"]
        records.append({                 # ← fixed indentation
            "text_id": str(uuid4()),
            "title": title,
            "text": context
        })

df = pd.DataFrame(records)
df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)
print("Total documents:", len(df))