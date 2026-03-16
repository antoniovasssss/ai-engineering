from transformers import pipeline

grammar_checker=pipeline(
task="text-classification",
model="textattack/bert-base-uncased-CoLA"
) # Load the pre-trained model and tokenizer for grammar checking

result=grammar_checker("He eat pizza every day") # Check the grammar of the input sentence
print(result)