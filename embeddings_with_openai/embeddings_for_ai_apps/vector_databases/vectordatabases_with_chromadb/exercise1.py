import chromadb
from openai import api_key
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="my_collection",
    embedding_function=OpenAIEmbeddingFunction(
        model_name="text-embedding-3-small",
        api_key=api_key
    )
)

collection.add(
    ids=["my-doc"],
    documents=["This is the source text"]
)