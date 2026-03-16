from transformers import pipeline

qnli_classifier=pipeline(
task="text-classification",
model="textattack/bert-base-uncased-QNLI"
) # Load the pre-trained model and tokenizer for QNLI (Question Natural Language Inference)

result=qnli_classifier(
"Where is Seattle located?, Seattle is in Washington state."
) # Classify the relationship between the question and the statement

print(result)