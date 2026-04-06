import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

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
response=client.embeddings.create(
model="text-embedding-3-small",
input=article_texts
)
result=response.model_dump()
print(result)
