from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100
)

hf = HuggingFacePipeline(pipeline=pipe)

response = hf.invoke("Explain AI in simple terms")
print(response)