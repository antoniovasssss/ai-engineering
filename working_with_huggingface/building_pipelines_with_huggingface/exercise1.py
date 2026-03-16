from transformers import pipeline

classifier=pipeline(
task="text-classification",
model="distilbert-base-uncased-finetuned-sst-2-english"
) # Load the pre-trained model and tokenizer for sentiment analysis

result=classifier("I hate waiting in long queues")
print(result) # Output the sentiment analysis result for the input text