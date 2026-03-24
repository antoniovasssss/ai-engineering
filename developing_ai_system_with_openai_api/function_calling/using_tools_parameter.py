import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")





messages = [
    {
        "role": "system",
        "content": "You extract the title and year of publication from research papers."
    },
    {
        "role": "user",
        "content": """
        Research Paper:

        Title: Deep Learning for Natural Language Processing
        Authors: John Smith, Sarah Johnson
        Published in: Journal of AI Research, 2021

        Abstract:
        This paper explores the application of deep learning techniques in natural language processing tasks such as text classification, machine translation, and sentiment analysis.
        """
    }
]




function_definition = [
    {
        "type": "function",  
        "function": {
            "name": "extract_paper_info",
            "description": "Extract title and year from research papers",
            "parameters": {}
        }
    }
]

# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = 'object'

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    'title': {
        'type': 'string',
        'description': 'Title of the research paper'
    },
    'year': {
        'type': 'string',
        'description': 'Year of publication of the research paper'
    }
}

# (Optional but recommended)
function_definition[0]['function']['parameters']['required'] = ['title', 'year']

print(function_definition)



client = OpenAI(api_key=api_key)

def get_reponse(messages, tools): 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice='auto'
    )

# Extract tool call 
    return response.choices[0].message.tool_calls[0].function.arguments


print(get_reponse(messages, function_definition))