# Building a Custom Pipeline with Auto Classes

from transformers import (
	AutoTokenizer,
	AutoModelForSequenceClassification,
	pipeline
)

model_name="distilbert-base-uncased-finetuned-sst-2-english"

tokenizer=AutoTokenizer.from_pretrained(model_name)
model=AutoModelForSequenceClassification.from_pretrained(model_name)

custom_pipeline=pipeline(
task="text-classification",
model=model,
tokenizer=tokenizer
)

custom_pipeline("This course is absolutely amazing!")