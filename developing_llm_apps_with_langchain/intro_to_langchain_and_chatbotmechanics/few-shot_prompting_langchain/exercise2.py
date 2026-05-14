from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

# Create the examples list of dicts
examples = [
  {
    "question": "How many courses has Jack completed?",
    "answer": "Jack has completed 36 courses."
  },
  {
    "question": "How much experience points does Jack have?",
    "answer": "Jack has 284,320 experience points."
  },
  {
    "question": "What technology does Jack focus on the most?",
    "answer": "Python is the technology that Jack focuses on the most."
  }
]

# Create the example prompt template
example_prompt = PromptTemplate.from_template(
    "Question: {question}\nAnswer: {answer}"
)

# Create the few shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}\nAnswer:",
    input_variables=["input"]
)

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

chain = few_shot_prompt | llm

# See the final prompt
formatted_prompt = few_shot_prompt.invoke({
    "input": "How many courses has Jack completed?"
}) 

response = chain.invoke({
    "input": "How many courses has Jack completed?"
})

print("\n======= LLM RESPONSE =======")
print(response.content)
