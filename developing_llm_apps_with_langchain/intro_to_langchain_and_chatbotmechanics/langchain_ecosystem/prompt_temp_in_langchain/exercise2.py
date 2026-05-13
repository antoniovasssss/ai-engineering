# 🔗 4. Connect PromptTemplate with LLM

# Combine:
# - PromptTemplate
# - LLM
# using the LCEL pipe operator (|)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError(
        "OPENAI_API_KEY is not set. Add OPENAI_API_KEY=sk-... to a .env file or set it in your environment."
    )
if openai_api_key == "your-api-key":
    raise ValueError(
        "OPENAI_API_KEY is currently the placeholder 'your-api-key'. Replace it with your real OpenAI API key."
    )

# Create LLM
llm = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-4o-mini"
)

# Create PromptTemplate
template = PromptTemplate.from_template(
    "Explain {concept} in easy language"
)

# Create chain using LCEL
chain = template | llm

# Invoke chain
response = chain.invoke({
    "concept": "Neural Networks"
})

# Print response
print(response.content)