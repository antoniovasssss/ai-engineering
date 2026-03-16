""" 
- Build the pipeline and save as `classifier`.
- Create a list of the labels - `"politics"`, `"science"`, `"sports"` - and save as `categories`.
- Predict the label of `text` using the classifier and predefined categories.
"""
from transformers import pipeline

text = "AI-powered robots assist in complex brain surgeries with precision." # The input text to classify

# Create the pipeline
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the categories list
categories = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, categories)

# Print the top label and its score
print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")