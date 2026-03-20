from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {"role":"system","content":"You are a helpful assistant"},
        {"role":"user","content":"Explain what an API is"}
    ]
)

print(response.choices[0].message.content)

try:
    response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":"Hello"}]
) # This is the API call that may raise an exception
except Exception as e:
    print("Something went wrong. Please try again later.")
    
# Formatting model response as JSON
response=client.chat.completions.create(
model="gpt-4.1-mini",
response_format={"type":"json_object"},
messages=[
        {
"role":"user",
"content":"List five trees with their scientific names in JSON format"
        }
    ]
)
print(response.choices[0].message.content)


# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format={"type":"json_object"}
)

# Print the response
print(response.choices[0].message.content)