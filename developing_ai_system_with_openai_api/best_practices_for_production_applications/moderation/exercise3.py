import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

user_request = "Can you recommend a good restaurant in Berlin?"

# Write the system and user message
messages = [{"role": "system", "content": "Your role is to assess whether the user question is allowed or not, and if it is, to be a helpful assistant to tourists visiting Rome. The allowed topics are food and drink, attractions, history and things to do around the city of Rome. If the topic is allowed, reply with an answer as normal, otherwise say 'Apologies, but I am not allowed to discuss this topic.'",},
            {"role": "user", "content": user_request}]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages
)

# Print the response
print(response.choices[0].message.content)