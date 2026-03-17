"""
- Create the summarization `pipeline` using the task "summarization" and save as `summarizer`.
- Use the new pipeline to create a summary of the text and save as `summary_text`.
- Compare the length of the original and summary text.
"""
# Create the summarization pipeline
from transformers import pipeline

# Define the original text to be summarized
original_text = "Your text to summarize goes here. Add a longer article or document that you want to create a summary for."

summarizer = pipeline("text2text-generation" , model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['generated_text'])}")