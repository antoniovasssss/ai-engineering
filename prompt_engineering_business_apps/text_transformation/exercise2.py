""" 
Craft a prompt that transforms the sample_email by changing its tone to be professional, positive, and user-centric.
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

sample_email = "Dear Valued Customer, We’re pleased to share the latest updates from our store and invite you to explore our newest product arrivals. Each item has been thoughtfully selected to deliver quality, style, and value—designed with your needs and preferences in mind. As a thank you for being part of our community, we’re also offering exclusive deals available for a limited time. This is our way of ensuring you get more from every shopping experience with us. We look forward to supporting your journey with products you can trust and enjoy. Should you have any questions or need assistance, our team is always here to help. Warm regards, The Customer Care Team"

# Craft a prompt to change the email's tone
prompt = f"""
Transforms the sample email by changing its tone to be professional, positive and user-centric

```{sample_email}```
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)