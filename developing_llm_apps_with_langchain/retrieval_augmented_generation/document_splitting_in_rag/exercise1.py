from langchain_text_splitters import CharacterTextSplitter

text = "Do not take life too seriously. You will never get out of it alive."

splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=24,
    chunk_overlap=3
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
