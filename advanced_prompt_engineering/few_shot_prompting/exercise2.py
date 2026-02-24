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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= [{"role": "user", "content": "The product quality exceeded my expectations"},
               {"role": "assistant", "content": "1"},
               {"role": "user", "content": "I had terrible experience with this product's customer service"},
               {"role": "assistant", "content": "-1"},
               {"role": "user", "content":"The price of the product is really fair given its features"}
               ],
    temperature= 0
    )
print(response.choices[0].message.content)
