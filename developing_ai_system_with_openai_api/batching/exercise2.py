from tenacity import retry, wait_random_exponential, stop_after_attempt
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client=OpenAI()

@retry(wait=wait_random_exponential(min=1,max=60),
stop=stop_after_attempt(5))
def get_response():
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": "Tell me a joke"}]
    )
    return response.choices[0].message.content

print(get_response())