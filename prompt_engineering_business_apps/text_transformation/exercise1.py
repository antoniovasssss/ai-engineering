""" 
Craft a prompt that translates the marketing_message from English to French, Spanish, and Japanese.
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

marketing_message = "Discover elegance redefined with our latest collection of premium leather handbags. Crafted from the finest quality leather and designed with timeless sophistication, each handbag blends luxury, durability, and modern style. Perfect for work, travel, or special occasions, our new collection offers versatile designs that elevate every outfit. Experience comfort craftsmanship, and confidence—because you deserve accessories as exceptional as you are."

# Craft a prompt that translates
prompt = f"""Translate the marketing materials from English to French, Spanish and Japanese. make sure to check for any grammer and language correctness. ```{marketing_message}``` """
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)