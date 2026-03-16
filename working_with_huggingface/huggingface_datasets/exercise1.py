# Exercise 1: Loading a Dataset from Hugging Face
from datasets import Dataset

# Create a sample dataset with local data
sample_data = {
    "text": [
        "bella is learning machine learning",
        "I love programming with Python",
        "bella also enjoys natural language processing",
        "Deep learning is fascinating",
        "bella builds amazing AI applications",
        "Data science is everywhere"
    ]
}

dataset = Dataset.from_dict(sample_data)  # Create dataset from dictionary

print("Original dataset:")
print(dataset)
print()

# Filter the dataset to include only rows where the "text" column contains the word "bella"
filtered_dataset = dataset.filter(lambda row: "bella" in row["text"])
print("Filtered dataset (containing 'bella'):")
print(filtered_dataset)
print()

# Select the first 2 rows of the dataset
small_dataset = dataset.select(range(2))
print("Small dataset (first 2 rows):")
print(small_dataset)
print()

# Access the "text" column of the first row in the small dataset
print("Text from first row of small dataset:")
print(small_dataset[0]["text"])