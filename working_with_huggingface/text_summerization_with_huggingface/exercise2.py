# Abstractive Summarization in Action
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
Data science is widely used in industry to solve complex problems and make data-driven decisions.
"""

inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(
    inputs["input_ids"],
    max_length=130,
    min_length=30,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)
result = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(result)
