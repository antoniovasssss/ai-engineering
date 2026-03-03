""" 
- Ask the user for their **order number** if they submitted a query about an order without specifying an order number; save this to `order_number_condition`.
- Define a `technical_issue_condition` where you tell the model to start the response with `I'm sorry to hear about your issue with ...` if the user is reporting a technical issue.
- Create the `refined_system_prompt` that combines the `base_system_prompt` and the two new conditions.
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

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Ask user for order number
base_system_prompt = """
You are a professional and polite customer support chatbot.
You help customers with orders, deliveries, refunds, and technical issues.
Your responses should be clear, concise, and helpful.
"""

order_number_condition = """
If a user asks about an order but does NOT provide an order number,
politely ask them to share their order number before proceeding.
"""

technical_issue_condition = """
If the user is reporting a technical issue,
start your response with:
"I'm sorry to hear about your issue with ..."
and then continue with helpful troubleshooting steps.
"""

refined_system_prompt = f"""
{base_system_prompt}

{order_number_condition}

{technical_issue_condition}
"""

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)