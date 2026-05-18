import pandas as pd
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import dotenv

# Load environment variables
dotenv.load_dotenv()

# -----------------------------
# Create Dummy Customer Data
# -----------------------------
data = {
    "customer_id": list(range(101, 121)),

    "name": [
        "TechNova Solutions",
        "CloudSync Inc",
        "DataBridge Systems",
        "NextGen AI",
        "PixelCraft Studio",
        "VisionSoft Labs",
        "CodeSphere Technologies",
        "BluePeak Analytics",
        "QuantumEdge",
        "Skyline Digital",
        "NexaCore Systems",
        "BrightPath AI",
        "FusionTech",
        "RapidScale Solutions",
        "AlphaWave Tech",
        "SmartGrid Software",
        "CyberNova",
        "InnoBridge",
        "FutureStack",
        "Peak Performance Co."
    ],

    "industry": [
        "Software Development",
        "Cloud Computing",
        "Data Analytics",
        "Artificial Intelligence",
        "Design Agency",
        "FinTech",
        "Web Development",
        "Business Intelligence",
        "Cybersecurity",
        "Digital Marketing",
        "IT Services",
        "Machine Learning",
        "Enterprise Software",
        "DevOps",
        "E-commerce",
        "Automation",
        "Security Solutions",
        "Consulting",
        "SaaS Platform",
        "Fitness & Wellness"
    ],

    "subscription_plan": [
        "Enterprise",
        "Pro",
        "Enterprise",
        "Starter",
        "Pro",
        "Business",
        "Starter",
        "Enterprise",
        "Business",
        "Pro",
        "Enterprise",
        "Business",
        "Pro",
        "Enterprise",
        "Starter",
        "Business",
        "Enterprise",
        "Pro",
        "Business",
        "Enterprise"
    ],

    "monthly_revenue": [
        12000,
        5000,
        15000,
        2500,
        7000,
        8500,
        3000,
        14000,
        11000,
        6500,
        20000,
        9500,
        7200,
        16000,
        2800,
        10000,
        17500,
        6200,
        13000,
        18000
    ],

    "customer_success_manager": [
        "Alice Johnson",
        "Bob Smith",
        "Charlie Brown",
        "Diana Lee",
        "Ethan Clark",
        "Sophia Miller",
        "James Wilson",
        "Olivia Davis",
        "Liam Anderson",
        "Emma Taylor",
        "Noah Thomas",
        "Ava Martinez",
        "William Moore",
        "Isabella Jackson",
        "Benjamin White",
        "Mia Harris",
        "Lucas Martin",
        "Charlotte Thompson",
        "Henry Garcia",
        "Amelia Robinson"
    ]
}

# Create DataFrame
customers = pd.DataFrame(data)

# Display sample data
print(customers.head())


# -----------------------------
# Create Tool
# -----------------------------
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their company name."""

    customer_info = customers[
        customers['name'].str.lower() == name.lower()
    ]

    if customer_info.empty:
        return f"No customer found with name: {name}"

    return customer_info.to_string(index=False)


# Print tool arguments
print("\nTool Arguments:")
print(retrieve_customer_info.args)


# -----------------------------
# Initialize LLM
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -----------------------------
# Create ReAct Agent
# -----------------------------
agent = create_agent(
    llm,
    [retrieve_customer_info]
)


# -----------------------------
# Invoke Agent
# -----------------------------
messages = agent.invoke({
    "messages": [
        (
            "human",
            "Create a summary of our customer: Peak Performance Co."
        )
    ]
})

# Print final response
print("\nAgent Response:\n")
print(messages['messages'][-1].content)