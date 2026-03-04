""" 
- Define a `system_prompt` that defines the purpose of the chatbot and guides it to answer queries in a gentle way.
- Use the `system_prompt`, the `context_question`, and `context_answer` to formulate a conversation that the chatbot can use as context in order to respond to the new user query.
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

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Define the system prompt
system_prompt = "You are a helpful customer service assistant for MyPersonalDelivery, a delivery service that offers a wide range of delivery options for various items. Answer customer questions accurately and politely based on the information you have been provided."

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",    "content": system_prompt},
        {"role": "user",      "content": context_question},
        {"role": "assistant", "content": context_answer},
        {"role": "user",      "content": "Can I use your service to send my laptop and some groceries across town?"}
    ]
)
response = response.choices[0].message.content
print(response)