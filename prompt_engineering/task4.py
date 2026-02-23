""" 
Write a conditional prompt that:

- summarizes text only if it is in English
- otherwise says: "Unsupported language"
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
    messages=[{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content

text = "I love python."

prompt = f"""Summerize text only if it is in English if it is not in English, respond with:"Unsupported language".
 ```{text}```"""
 
response = get_response(prompt)
print(response)