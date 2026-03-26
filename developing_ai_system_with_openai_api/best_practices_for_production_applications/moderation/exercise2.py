""" 
- Use the moderation API to check the user message for inappropriate content within `categories`.
- Print the response.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
moderation_response = client.moderations.create(input=message) 

# Print the response
print(moderation_response.results[0].categories)