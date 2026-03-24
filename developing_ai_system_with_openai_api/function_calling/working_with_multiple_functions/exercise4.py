""" 
Modify the messages to ask the model not to assume any values for the responses.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


# -----------------------------
# Messages (review input)
# -----------------------------
messages = [
    {
        "role": "system",
        "content": "You are an assistant that processes customer reviews."
    },
    {
        "role": "user",
        "content": "The delivery was fast and packaging was great, but nothing else to say."
    }
]

# 🔥 IMPORTANT: Avoid assumptions
messages.append({
    "role": "system",
    "content": (
        "Do not make assumptions about missing information. "
        "If the review does not contain a product name, variant, or clear sentiment, "
        "do not generate or guess those values. "
        "Only extract or respond when sufficient information is present."
    )
})

# -----------------------------
# Function Definitions
# -----------------------------
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Extract product name, variant, and sentiment from a review",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "variant": {"type": "string"},
                    "sentiment": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"]
                    }
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "reply_to_review",
            "description": "Generate a polite reply to a customer review",
            "parameters": {
                "type": "object",
                "properties": {
                    "reply": {
                        "type": "string",
                        "description": "Professional reply to the customer"
                    }
                },
                "required": ["reply"]
            }
        }
    }
]

# -----------------------------
# Helper function
# -----------------------------
def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition,
        tool_choice="auto"  # Let model decide whether to call a function
    )

    message = response.choices[0].message

    # If function is called
    if message.tool_calls:
        return message.tool_calls[0].function.arguments
    else:
        return message.content


# -----------------------------
# Call and print response
# -----------------------------
response = get_response(messages, function_definition)

print(response)