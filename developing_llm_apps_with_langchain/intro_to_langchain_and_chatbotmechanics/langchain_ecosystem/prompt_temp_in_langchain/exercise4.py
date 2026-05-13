from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Create model
llm = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-4o-mini"
)

# Create chat prompt template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a geography expert that returns the colors present in a country's flag."
    ),
    ("human", "France"),
    ("ai", "blue, white, red"),
    ("human", "{country}")
])

# Create chain
llm_chain = prompt_template | llm

# Invoke chain
country = "Japan"

response = llm_chain.invoke({
    "country": country
})

print(response.content)