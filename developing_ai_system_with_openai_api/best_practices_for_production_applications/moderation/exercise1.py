import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI()

response=client.moderations.create(
model="omni-moderation-latest",
input="if the kitten gets killed you lose the game."
)

print(response)