# Import the HuggingFacePipeline class for defining Hugging Face pipelines
from langchain_community.llms import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100},
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)