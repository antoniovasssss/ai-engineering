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

product_description = "The smartphone features a6.7-inch AMOLED display with a120Hz refresh rate, offering smooth visuals and vibrant colors. It is powered by a high-performance processor that ensures fast multitasking and gaming. The device includes a5000mAh battery that supports fast charging, allowing extended usage throughout the day. The smartphone comes with a triple-camera system, including a64MP main camera, an ultra-wide lens,and a macro sensor, delivering high-quality photos and videos. It also offers 5G connectivity, enhanced security features such as an in-display fingerprint sensor,and runs on the latest version of the operating system."

# prompt = f"""
# Summarize the following smartphone product description in no more than five bullet points.
# Highlight the key features that would help users quickly compare and evaluate the product.

# Product Description:{product_description}
# """

# prompt = f"""
# Summarize the product description delimited by triple backticks, in at most five bullet points.
#  ```{product_description}```

# """

prompt = f"""
Expand the product description from pre-loaded string, and writes  a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)