from transformers import pipeline

generator=pipeline(
task="text-generation",
model="openai-community/gpt2"
)

results=generator(
"What if AI",
max_new_tokens=10,
num_return_sequences=2
)

for res in results:
    print(res["generated_text"])