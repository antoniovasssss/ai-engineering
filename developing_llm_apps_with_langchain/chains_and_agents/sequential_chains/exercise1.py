from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# ================================
# PROMPTS
# ================================
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

# ================================
# LLM
# ================================
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ================================
# SEQUENTIAL CHAIN
# ================================
seq_chain = (
    {
        "learning_plan": learning_prompt | llm | StrOutputParser()
    }
    | time_prompt
    | llm
    | StrOutputParser()
)

# ================================
# CALL THE CHAIN
# ================================
response = seq_chain.invoke({
    "activity": "play the harmonica"
})

print(response)