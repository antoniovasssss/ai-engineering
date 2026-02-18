"""
OPENAI API message roles

You are developing a chatbot for an event management agency that will be used to facilitate networking during events.

Using the OpenAI API, you prepare a dictionary to pass as the message to the `chat.completions` endpoint. The message needs to have 3 roles defined to ensure the model has enough guidance to provide helpful responses.

Throughout the course, you'll write Python code to interact with the OpenAI API.
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

conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing an event for my friend's marriage."}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation_messages
)
print(response.choices[0].message.content)