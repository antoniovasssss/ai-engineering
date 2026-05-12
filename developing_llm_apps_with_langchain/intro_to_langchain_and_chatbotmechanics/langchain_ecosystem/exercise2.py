from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

pipe=pipeline("text-generation",model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

hf = HuggingFacePipeline(pipeline=pipe)

response = hf.invoke("Explain AI in simple terms")
print(response)