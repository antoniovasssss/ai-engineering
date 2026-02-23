""" 
Craft a prompt that generates a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover.
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

# Create a prompt that generates the table
prompt = "Generate a table containing 10 books I should read if I am a science fiction lover, with columns for Title, Author, and Year."

# Get the response
response = get_response(prompt)
print(response)