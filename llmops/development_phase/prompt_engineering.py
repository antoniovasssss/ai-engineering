""" 
Craft a prompt that asks the model to write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output.
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
    messages=[{"role": "user", "audience": "developer", "content":prompt}]
    )
    return response.choices[0].message.content

# Craft a prompt that asks the model for the function
prompt = f"""Explain cloud computing in simple terms."""

response = get_response(prompt)
print(response)