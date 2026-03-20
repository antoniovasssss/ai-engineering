from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response=client.chat.completions.create(
model="old-model-name",
messages=[{"role":"user","content":"Hello"}]
)

# Connection Errors
try:
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":"Hello"}]
    )


exceptExceptionase:
    print("Something went wrong. Please try again later.")
    
    
# Resource Limit Errors
import time

for i in range(5):
    try:
       response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":"Tell me a joke"}]
        )
    
print(response.choices[0].message.content)

except Exception:
    print("Rate limit reached. Waiting...")
time.sleep(5)


# Bad Request Errors
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {"role":"teacher","content":"Explain Python"}
    ]
)

# Handling Exceptions in Python
client = OpenAI(api_key=api_key)

try:
    response=client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":"List five data science profession"}],
   
    )
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
       print(f"Invalid API key. {e}")
except Exception as e:
    print(f"Unexpected error occurred.{e}")
    
    
# Handling Specific Errors
client = OpenAI(api_key=api_key)

try:
    response=client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":"List five data science profession"}],
   
    )
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
       print(f"Invalid API key. {e}")

# except openai.RateLimitError as e:
#         print(f"Too many requests. Please wait.{e}")
except Exception as e:
    print(f"Unexpected error occurred.{e}")
    
    
# Handling exceptions
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use the try statement
try: 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError as e:
    print("Please double check your authentication key and try again, the one provided is not valid.")