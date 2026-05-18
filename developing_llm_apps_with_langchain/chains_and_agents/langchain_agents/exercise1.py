import wikipedia
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.agent_toolkits.load_tools import load_tools

# Set a Wikipedia user-agent so the Wikipedia API accepts the request
wikipedia.set_user_agent("ai-engineering-bot/1.0 (https://example.com)")

# Create LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Load Wikipedia tool
tools = load_tools(["wikipedia"])

# Create ReAct Agent
agent = create_agent(
    llm,
    tools
)

# User input
query = "Who invented Python programming language?"

# Run the agent
response = agent.invoke(
    {
        "messages": [
            ("human", query)
        ]
    }
)

# Print final response
print(response["messages"][-1].content)