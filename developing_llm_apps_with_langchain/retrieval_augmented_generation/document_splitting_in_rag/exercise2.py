from langchain_text_splitters import RecursiveCharacterTextSplitter

text="Do not take life too seriously. You will never get out of it alive."

splitter=RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
chunk_size=24,
chunk_overlap=3
)

chunks=splitter.split_text(text)

for chunk in chunks:
    print(chunk)