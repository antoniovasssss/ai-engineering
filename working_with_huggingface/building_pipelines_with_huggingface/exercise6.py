""" 
- Create a text classification QNLI pipeline using the model `"cross-encoder/qnli-electra-base"` and save as `classifier`.
- Use this classifier to determine if the text provides enough information to answer the question.
"""

from transformers import pipeline

classifier = pipeline(task="text-classification", model="cross-encoder/qnli-electra-base") # Create a text classification pipeline using the specified model

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.") # Use the classifier to predict if the text provides enough information to answer the question

print(output)