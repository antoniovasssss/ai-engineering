"""
- Initialize a question-answering pipeline with the correct task and model.
- Pass the question and `document_text` to the pipeline.
- Print the result to view the answer.
"""
from transformers import pipeline

# Load the question-answering pipeline
qa_pipeline = pipeline(task="question-answering", model="distilbert-base-cased-distilled-squad")

question = "What is the notice period for resignation?"

# Get the answer from the QA pipeline
result = qa_pipeline(question=question, context=document_text)

# Print the answer
print(f"Answer: {result['answer']}")