""" 
- Define a `system_prompt` that defines the purpose of the chatbot including the `service_description`, and guides it to answer queries in a gentle way.
- Get the response using the `get_response()` function, that receives a system and a user prompt as inputs and returns the response as an output.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# OpenAI client
client = OpenAI(api_key=api_key)


def get_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

service_description = """MyPersonalDelivery is a fast and reliable delivery service that helps customers
send and receive everyday items with ease. The service delivers groceries,
medicines, electronics, clothing, documents, and small household items.

MyPersonalDelivery offers same-day delivery for groceries and medicines in most
cities, affordable pricing, real-time order tracking, and friendly customer
support. The goal of the service is to make daily deliveries simple, safe, and
stress-free for customers."""

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)