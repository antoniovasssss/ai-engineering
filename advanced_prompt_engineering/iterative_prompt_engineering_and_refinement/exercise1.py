""" 
Iteratively refine the prompt to get the desired outcome: a table with three columns for the top ten pre-trained language models, listing the model name, release year, and owning company.
"""
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

# Refine the following prompt
prompt = "Give me the top 10 pre-trained language models, add a table with three columns, list model name, release year and owning company"

response = get_response(prompt)
print(response)