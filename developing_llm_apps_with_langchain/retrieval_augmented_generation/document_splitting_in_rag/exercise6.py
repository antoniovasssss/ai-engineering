""" 
- Create an `UnstructuredHTMLLoader` for `white_house_executive_order_nov_2023.html`, and load it into memory.
- Set a `chunk_size` of `300` and a `chunk_overlap` of `100`.
- Create a `RecursiveCharacterTextSplitter` splitting on the `'.'` character, and use the `.split_documents()` method to split `data` and print the chunks.
"""
# Import the HTML loader and recursive character splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredHTMLLoader   
# Load the HTML document into memory
loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")
data = loader.load()

# Define variables
chunk_size = 300
chunk_overlap = 100

# Split the HTML
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=['.'])

docs = splitter.split_documents(data) 
print(docs)