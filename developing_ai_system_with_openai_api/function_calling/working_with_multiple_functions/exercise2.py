""" 
- Add your function definition as tools.
- Set the `extract_review_info` function to be called for the response.
- Print the response.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI(api_key=api_key)




messages = [
    {
        "role": "system",
        "content": "You are an assistant that extracts structured data from customer reviews."
    },
    {
        "role": "user",
        "content": """Extract product name, variant, and sentiment from the following reviews:

        1. "I absolutely love the iPhone 14 Pro Max 256GB! The camera is amazing."
        2. "The Samsung Galaxy S23 Ultra is too expensive for what it offers."
        3. "My Sony WH-1000XM5 headphones are decent but not worth the price."
        """
    }
]

# -----------------------------
# Function Definition
# -----------------------------
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract product name, variant, and sentiment from customer reviews",
            "parameters": {
                "type": "object",
                "properties": {
                    "reviews": {
                        "type": "array",
                        "description": "List of extracted review data",
                        "items": {
                            "type": "object",
                            "properties": {
                                "product_name": {
                                    "type": "string",
                                    "description": "Name of the product"
                                },
                                "variant": {
                                    "type": "string",
                                    "description": "Product variant like storage, model, etc."
                                },
                                "sentiment": {
                                    "type": "string",
                                    "enum": ["positive", "negative", "neutral"],
                                    "description": "Customer sentiment"
                                }
                            },
                            "required": ["product_name", "variant", "sentiment"]
                        }
                    }
                },
                "required": ["reviews"]
            }
        }
    }
]

# -----------------------------
# API Call
# -----------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=function_definition,
    tool_choice={
        "type": "function",
        "function": {"name": "extract_review_info"}
    }
)

# -----------------------------
# Print Output
# -----------------------------
print(response.choices[0].message.tool_calls[0].function.arguments)