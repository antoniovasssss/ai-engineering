from transformers import pipeline

qa_pipeline=pipeline(
task="question-answering",
model="distilbert-base-uncased-distilled-squad"
)

question="How many volunteer days are allowed per year?"

result=qa_pipeline(
question=question,
context=document_text
)

print(result)