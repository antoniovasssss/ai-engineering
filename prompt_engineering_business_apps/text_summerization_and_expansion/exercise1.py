import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY") # retieves the value of the OPENAI_... environment variable and stores it in the api_key variable

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# OpenAI client
client = OpenAI(api_key=api_key) 

def get_response(prompt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content

report = "The market has seen rapid growth in the adoption of artificial intelligence across industries such as finance, healthcare, and retail. Businesses are increasingly using AI to personalize customer experiences, automate customer support, and analyze large data sets for better decision-making. However, this rapid adoption has raised concerns among customers regarding data privacy and security. Many consumers are becoming more cautious about how their personal data is collected, stored, and used by AI-driven systems. Regulatory frameworks and data protection laws are influencing how companies design their AI solutions. As a result, companies that prioritize transparency and ethical data practices are gaining higher customer trust and loyalty."

prompt = f"""
Summarize the following market research report in a maximum of five sentences.
Focus specifically on how artificial intelligence and data privacy are shaping the market
and how they are affecting customer behavior.

Report:{report}
"""

response = get_response(prompt)
print("Summarized report: \n", response)