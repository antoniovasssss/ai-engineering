""" 
In some cases, you may lack the hardware to run Hugging Face models locally. Large-parameter LLMs, and image and video generation models in particular often require Graphics Processing Units (GPUs) to parallelize the computations. Hugging Face providers inference providers to outsource this hardware to third-party partners.
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient( # creates a client that will route requests through TogetherAI
    provider="together",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create( # send a request to run the DeepSeek... model
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(completion.choices[0].message.content)