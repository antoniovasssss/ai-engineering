import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

articles = [
    {"headline":"Government announces new tax reform","topic":"politics"},
    {"headline":"Local team wins national championship","topic":"sports"},
    {"headline":"New AI model beats humans at chess","topic":"technology"},
    {"headline":"Stock market hits record high","topic":"business"},

    {"headline":"President meets foreign leaders for climate summit","topic":"politics"},
    {"headline":"New law passed to improve public healthcare","topic":"politics"},
    
    {"headline":"Star player scores hat-trick in final match","topic":"sports"},
    {"headline":"Olympic committee announces new events","topic":"sports"},
    
    {"headline":"Breakthrough in quantum computing announced","topic":"technology"},
    {"headline":"Tech company releases next-gen smartphone","topic":"technology"},
    
    {"headline":"Global oil prices see significant drop","topic":"business"},
    {"headline":"Startup raises millions in funding round","topic":"business"},
    
    {"headline":"Scientists discover new species in rainforest","topic":"science"},
    {"headline":"Space agency plans mission to Mars","topic":"science"},
    
    {"headline":"New movie breaks box office records","topic":"entertainment"},
    {"headline":"Famous actor wins international award","topic":"entertainment"},
]


headlines= [article["headline"] for article in articles]
print(headlines)