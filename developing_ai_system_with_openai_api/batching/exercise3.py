import tiktoken # Import the tiktoken library for tokenization

encoding=tiktoken.encoding_for_model("gpt-4.1-mini")

text="Artificial intelligence is transforming modern technology."

tokens=encoding.encode(text) # Encode the text into tokens

print("Number of tokens:",len(tokens)) # Print the number of tokens