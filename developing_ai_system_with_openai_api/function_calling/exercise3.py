import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Optional: check if key is loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")





messages = [
    {
        "role": "system",
        "content": "You extract sentiment and key product features from customer reviews."
    },
    {
        "role": "user",
        "content": """
        I recently bought this smartphone and I'm really impressed!
        The battery life is amazing and lasts all day.
        The camera quality is excellent, especially in low light.
        However, the phone feels a bit heavy.
        Overall, I love it.
        """
    }
]



# Function definition (tool)
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract sentiment and key features from customer reviews",
            "parameters": {
                "type": "object",
                "properties": {
                    "sentiment": {
                        "type": "string",
                        "description": "Overall sentiment of the review (positive, negative, neutral)"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Key product features mentioned in the review"
                    }
                },
                "required": ["sentiment", "features"]
            }
        }
    }
]


client = OpenAI(api_key=api_key)

def get_reponse(messages, tools): 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice='auto'
    )

# Extract tool call 
    return response


response = get_reponse(messages, function_definition)

# Function to extract dictionary from response
def extract_dictionary(response):
    arguments = response.choices[0].message.tool_calls[0].function.arguments
    return json.loads(arguments)  # Convert JSON string → Python dict

# Print extracted structured data
print(extract_dictionary(response))