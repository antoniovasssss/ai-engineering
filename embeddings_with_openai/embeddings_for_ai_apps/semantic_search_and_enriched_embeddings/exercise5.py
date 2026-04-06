import os
from dotenv import load_dotenv
from openai import OpenAI
from scipy.spatial import distance
import numpy as np

# -----------------------------
# Load API Keys
# uv add scipy
# -----------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

articles= [
    {
"headline":"AI is transforming healthcare",
"topic":"Technology",
"keywords": ["AI","machine learning","healthcare"]
    },
    {
"headline":"New GPU architecture released",
"topic":"Hardware",
"keywords": ["GPU","computing","graphics"]
    },
    {
"headline":"Climate change impacts agriculture",
"topic":"Environment",
"keywords": ["climate","agriculture","environment"]
    }
]

def create_article_text(article):
	return f"""
    Headline:{article['headline']}
    Topic:{article['topic']}
    Keywords:{', '.join(article['keywords'])}
    """

article_texts=[create_article_text(article) for article in articles]

#print(article_texts)

def create_embeddings(texts):
	response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
    )
	return [item.embedding for item in response.data]

article_embeddings=create_embeddings(article_texts)

#print(article_embeddings)

def cosine_distance(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return distance.cosine(v1, v2)
     

def find_n_closest(query_vector, embeddings, n=3):

    distances= []

    for i, embedding in enumerate(embeddings):
        distance=cosine_distance(query_vector,embedding)

        distances.append({
       "index":i,
        "distance":distance
        })

    distances=sorted(distances, key=lambda x:x["distance"]) 

    return distances[:n]


query_embedding=create_embeddings(["AI"])[0]
print(query_embedding)

hits=find_n_closest(query_embedding,article_embeddings,n=3)

print(hits)

for hit in hits:
    print(articles[hit["index"]]["headline"])


# list = [0.5, 0.1, 0.2, 0.8, 0.9, 0.1]

# print(sorted(list, key=lambda x:x, reverse=True))
