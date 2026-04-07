import os
from dotenv import load_dotenv
from openai import OpenAI
from scipy.spatial import distance
from scipy import spatial
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

current_article= {
"headline":"Computer hardware accelerates AI innovation",
"topic":"Technology",
"keywords": ["AI","hardware","computing"]
}

def create_article_text(article):
	return f"""
    Headline:{article['headline']}
    Topic:{article['topic']}
    Keywords:{', '.join(article['keywords'])}
    """

article_texts=[create_article_text(article) for article in articles]

current_article_text = create_article_text(current_article)
#print(article_texts)

def create_embeddings(texts):
    response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
    )
    response_dict = response.model_dump()
    
    return [data['embedding'] for data in response_dict['data']]



current_article_embeddings = create_embeddings(current_article_text)[0]

article_embeddings=create_embeddings(article_texts)


     
def find_n_closest(query_vector, embeddings, n=3):

    distances= []

    for i, embedding in enumerate(embeddings):
        distance=spatial.distance.cosine(query_vector,embedding)

        distances.append({
       "index":i,
        "distance":distance
        })

    distances=sorted(distances, key=lambda x:x["distance"]) 

    return distances[:n]


query_embedding=create_embeddings(["AI"])[0]
# print(query_embedding)

hits=find_n_closest(current_article_embeddings,article_embeddings,n=3)

# print(hits)

# for hit in hits:
#     print(articles[hit["index"]]["headline"])

# improving recommendations with user history
user_history= [
    {
"headline":"Tech giant buys 49% stake in AI startup",
"topic":"Technology",
"keywords": ["AI","startup","investment"]
    },
    {
"headline":"Computer hardware accelerates AI innovation",
"topic":"Technology",
"keywords": ["AI","hardware","computing"]
    }
]

history_texts= [create_article_text(article) for article in user_history]

history_embeddings=create_embeddings(history_texts)

user_vector=np.mean(history_embeddings, axis=0)

unseen_articles= [article for article in articles if article not in user_history]

# print(unseen_articles)

unseen_articles_text = [create_article_text(article) for article in unseen_articles]

unseen_embeddings = create_embeddings(unseen_articles_text)



hits=find_n_closest(user_vector, unseen_embeddings,n=3)

print(hits)

for hit in hits:
    print(unseen_articles[hit["index"]]["headline"])