""" 
Create a multi-step prompt asking the model to make a plan for a beach vacation, which should include: four potential locations, each with some accommodation options, some activities, and an evaluation of the pros and cons.
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
    messages=[{"role": "user", "content":prompt}],
    max_tokens=100
    )
    return response.choices[0].message.content

# Create a prompt detailing steps to plan the trip
prompt = """
I need to plan for my 2 week beach vacation.
step 1: Four potential locations.
step 2: Each location must have accommodation options, some activities.
step 3: Evaluate pros and cons for each locations.
"""

response = get_response(prompt)
print(response)