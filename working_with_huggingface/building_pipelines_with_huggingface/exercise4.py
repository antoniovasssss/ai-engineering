from transformers import pipeline

zero_shot=pipeline(
task="zero-shot-classification",
model="facebook/bart-large-mnli"
)

result=zero_shot(
"Hey, we would like to feature your courses in our newsletter!",
candidate_labels=["Marketing","Sales","Support"]
)

print(result["labels"][0],result["scores"][0])