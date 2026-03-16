""" 
- Create a pipeline for the task `text-classification` and use the model `"abdulmatinomotoso/English_Grammar_Checker"`, saving the pipeline as `grammar_checker`.
- Use the `grammar_checker` to predict the grammatical correctness of the input sentence provided and save as `output`.
"""
# Grammatical Error Correction Pipeline

from transformers import pipeline

# Create a pipeline for grammar checking
grammar_checker = pipeline(
    task="text-classification",
    model="abdulmatinomotoso/English_Grammar_Checker"
)

# Check grammar of the input text
output = grammar_checker("I will walk dog")
print(output)
