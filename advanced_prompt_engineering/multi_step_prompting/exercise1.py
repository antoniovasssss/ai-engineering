""" 
Imagine you're a developer taking a break and you want to apply your prompting skills to plan the perfect beach vacation. As an initial step, you decide to use a standard single-step prompt to seek assistance.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY") # retieves the value of the OPENAI_... environment variableand stores it in the api_key variable

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# OpenAI client
client = OpenAI(api_key=api_key) 

def get_response(prompt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content":prompt}],
    max_tokens=100
    )
    return response.choices[0].message.content

# Create a single-step prompt to get help planning the vacation
prompt = "I have 2 weeks of break from my job i need to plan for a beach vacation."

response = get_response(prompt)
print(response)