# This code demonstrates how to batch multiple questions together when using the OpenAI API. By sending multiple questions in a single request, we can reduce the number of API calls and improve efficiency
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "Who wrote Hamlet?",
]

for question in questions:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": question}]
    )

    print(response.choices[0].message.content)

    time.sleep(2) # Add a delay between requests to avoid hitting rate limits
