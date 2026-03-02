""" 
Craft a few-shot prompt that uses three tickets and corresponding entities, to extract entities from the new ticket ticket_4.
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

# Sample tickets
ticket_1 = (
    "Hi Support Team, I’m unable to log into my account since yesterday. "
    "I keep getting an error message saying “authentication failed” even though my password "
    "is correct. My username is john.doe@email.com. Please help me fix this issue as soon as "
    "possible."
)

ticket_2 = (
    "Hello, I noticed that my credit card was charged twice for my monthly "
    "subscription on August 10, 2025. The amount charged was $49.99 each time. "
    "My order ID is ORD-45821. I’d appreciate it if you could check this and process a "
    "refund for the extra charge."
)

ticket_3 = (
    "Hey team, I just wanted to share some feedback about your new mobile app update. "
    "The interface looks much cleaner and the app feels faster, but the notification "
    "settings are a bit confusing to use. Overall, great work!"
)

ticket_4 = (
    "Good afternoon, my name is David Miller and I’m contacting you regarding a "
    "booking I made through your travel app. My reservation ID is TRV-90217 for a flight "
    "from New York to London scheduled on September 15, 2025. I need to update the passenger "
    "phone number linked to this booking. Please let me know how to proceed."
)

# Sample extracted entities
entities_1 = {
    "issue_type": "technical_issue",
    "problem": "authentication failed",
    "username": "john.doe@email.com"
}

entities_2 = {
    "issue_type": "billing_inquiry",
    "charge_amount": "$49.99",
    "charge_date": "August 10, 2025",
    "order_id": "ORD-45821",
    "request": "refund"
}

entities_3 = {
    "issue_type": "product_feedback",
    "product": "mobile app",
    "positive_feedback": ["cleaner interface", "faster performance"],
    "negative_feedback": ["confusing notification settings"]
}

# Craft a few-shot prompt
prompt = f"""
Extract entities from the new ticket using the same structure as the examples below.

sample 1:
{ticket_1}
entities:
{entities_1}

sample 2:
{ticket_2}
entities:
{entities_2}

sample 3:
{ticket_3}
entities:
{entities_3}

new ticket:
```{ticket_4}```
"""

response = get_response(prompt)

print("Ticket:\n", ticket_4)
print("Entities:\n", response)

