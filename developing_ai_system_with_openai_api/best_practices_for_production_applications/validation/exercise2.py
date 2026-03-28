""" 
- Use the `uuid` library with `uuid4()` to generate a unique ID.
- Pass the unique ID to the chat completions endpoint to identify the user.
"""
import os
import uuid
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

# Generate a unique ID
unique_id = str(uuid.uuid4())

messages = [{"role": "user", "content": "Hello!"}]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages,
# Pass a user identification key
  user=unique_id
)

print(response.choices[0].message.content)