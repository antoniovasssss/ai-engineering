"""
- Craft a `prompt` that asks the model to generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand.
- Get the `response` using the `get_response()` function.

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
    temperature= 0
    )
    return response.choices[0].message.content

prompt = "Write a short poem about ChatGPT using simple and basic English that a young child can understand."

response = get_response(prompt)
print(response)