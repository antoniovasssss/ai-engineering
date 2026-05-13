import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Create prompt template
template = """
You are an artificial intelligence assistant.
Answer the following question:

{question}
"""

prompt = PromptTemplate.from_template(template)

# Create model
llm = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-4o-mini"
)

# Create chain
llm_chain = prompt | llm

# Invoke chain
question = "How does LangChain make LLM application development easier?"

response = llm_chain.invoke({
    "question": question
})

print(response.content)