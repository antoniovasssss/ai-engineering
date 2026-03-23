""" 
- Provide a system message to request a response with all measurements as a table (make sure you specify that they are in kilometers and should be converted into miles).
- Append one user message per measurement to the messages list.
"""
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

measurements = [1, 5, 10, 20, 50, 100] # List of measurements in kilometers

messages = []
# Provide a system message and user messages to send the batch
messages.append({
            "role": "system",
            "content": "Convert each measurement, given in kilometers, into miles, and reply with a table of all measurements."
        })
# Append measurements to the message
[messages.append({"role": "user", "content": str(i)}) for i in measurements]


def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    return response.choices[0].message.content


response = get_response(messages)
print(response)
