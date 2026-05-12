from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Create model
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,         # creativity
    max_completion_tokens=100
)

# Send prompt
response = llm.invoke("Help me understand html")

print(response)