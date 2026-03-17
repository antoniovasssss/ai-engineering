# %%
from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
Data science is widely used in industry to solve complex problems and make data-driven decisions.
"""

inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs["input_ids"], max_length=50, min_length=20, do_sample=False)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Summary:")
print(summary)
