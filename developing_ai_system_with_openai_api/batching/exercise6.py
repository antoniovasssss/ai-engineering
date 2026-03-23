""" 
- Use the tiktoken library to create an encoding for the gpt-4o-mini model.
- Check for the expected number of tokens in the input message.
- Print the response if the message passes both checks.
"""
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken


load_dotenv()

client = OpenAI()

input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}

# Use tiktoken to create the encoding for your model
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
# Check for the number of tokens
num_tokens = len(encoding.encode(input_message["content"]))

# Run the chat completions function and print the response
if num_tokens <= 100:
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[input_message])
    print(response.choices[0].message.content)
else:
    print("Message exceeds token limit")