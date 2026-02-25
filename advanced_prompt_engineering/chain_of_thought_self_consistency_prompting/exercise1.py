""" 
Create a chain-of-thought prompt to determine your friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20.
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

# Create the chain-of-thought prompt
prompt = """
Guess the age of my friend father in 10 years based on below conditions.
step 1: My frind is 20.
step 2: My frind father is twice the age of my friend.
"""

response = get_response(prompt)
print(response)