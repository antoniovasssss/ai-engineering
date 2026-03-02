""" 
Craft a multi-step prompt that first proofreads the text without changing its structure, and then adjusts its tone to be formal and friendly.
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

text = "i really like this community because people share a lot of useful ideas. sometimes the posts are hard to read and there are many small mistakes, but overall the content is helpful and interesting. i think if the writing was clearer and more polished, more users would enjoy reading and contributing here."
 
 # Craft a prompt to transform the text
prompt = f"""
Generate the content from below text that can thrive.
step 1:  first proofreads the text without changing its structure, and then adjusts its tone to be formal and friendly.
step 2: Fix any grammar errors and refining writing tones to create a more polished and engaging environment for all users.
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)
