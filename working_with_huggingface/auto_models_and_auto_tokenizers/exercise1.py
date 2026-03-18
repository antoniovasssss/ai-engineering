# Exercise 1: Loading a Pretrained Model and Tokenizer
from transformers import AutoModelForSequenceClassification

model=AutoModelForSequenceClassification.from_pretrained(
"distilbert-base-uncased-finetuned-sst-2-english"
)

# Loading the tokenizer
from transformers import AutoTokenizer

tokenizer=AutoTokenizer.from_pretrained(
"distilbert-base-uncased-finetuned-sst-2-english"
)

tokens=tokenizer.tokenize("I love learning AI!") # Tokenize the input text
print(tokens)

