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


def get_response(prompt): # defines reusable function called get_response that takes one argument (prompt) which is the text sent to the AI
    response = client.chat.completions.create(
        model="gpt-4o-mini", # AI model used
        messages=[{"role":"user", "content":prompt}], # the conversation history
        temperature= 0 # controls creativity
    )
    return response.choices[0].message.content # the API returns a response object that contain multiple reply options ("choices"). This grabs the first one [0] and extracts just the text of the message

response = get_response("What is prompt engineering?") # function is called with a question and stores the AI's reply in the variable response
print(response) # prints the response in the terminal