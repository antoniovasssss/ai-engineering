""" 
Craft a prompt that asks the model to infer the Python function that maps the inputs to the outputs in the provided examples.
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

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""
 infer the Python function that maps the inputs to the outputs in the provided examples.

 ```{examples}```

"""

response = get_response(prompt)
print(response)