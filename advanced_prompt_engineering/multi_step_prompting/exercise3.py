""" 
Create a multi-step prompt asking the model to assess the function provided in the delimited code string according to the three criteria: correct syntax, receiving two inputs, and returning one output.
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

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""" 
access the function provided in the delimited code string.
step 1: check for correct syntax.
step 2: receiving two inputs, 5 and 9.
step 3: returning one output.

{code}
"""

response = get_response(prompt)
print(response)