# ================================
# IMPORTS
# ================================
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI
import os

# ================================
# LOAD ENV VARIABLES
# ================================
load_dotenv()

# ================================
# EXAMPLES
# ================================
examples = [
    {
        "question": "What is AI?",
        "answer": "Artificial Intelligence"
    },
    {
        "question": "What is ML?",
        "answer": "Machine Learning"
    },
    {
        "question": "What is NLP?",
        "answer": "Natural Language Processing"
    }
]

# ================================
# EXAMPLE FORMAT
# ================================
example_prompt = PromptTemplate.from_template(
    "Question: {question}\nAnswer: {answer}"
)

# ================================
# FEW SHOT PROMPT
# ================================
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}\nAnswer:",
    input_variables=["input"]
)

# ================================
# SEE FINAL PROMPT
# ================================
formatted_prompt = few_shot_prompt.invoke({
    "input": "What is DL?"
})

print("======= GENERATED PROMPT =======")
print(formatted_prompt.to_string())

# ================================
# LLM
# ================================
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=1
)

# ================================
# CREATE CHAIN
# ================================
chain = few_shot_prompt | llm

# ================================
# INVOKE CHAIN
# ================================
response = chain.invoke({
    "input": "What is DL?"
})

# ================================
# OUTPUT
# ================================
print("\n======= LLM RESPONSE =======")
print(response.content)