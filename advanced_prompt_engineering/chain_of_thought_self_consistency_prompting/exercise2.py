""" 
Define an example that teaches the model how to sum the even numbers on the set {9, 10, 13, 4, 2}.

Define a question, similar to the one in the example, that asks the model to reason on a new set {15, 13, 82, 7, 14}.
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


# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: (10,4,2). Adding them:10+4+2=16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}.
             A: Even numbers: """

# Create the final prompt
prompt = f"""

Find the sum {question} and example is {example}


"""
response = get_response(prompt)
print(response)