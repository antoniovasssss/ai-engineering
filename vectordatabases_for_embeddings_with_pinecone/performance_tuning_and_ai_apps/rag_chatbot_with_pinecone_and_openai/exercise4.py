""" 
- Initialize the Pinecone client with your API key (the OpenAI client is available as `client`).
- Define the function `retrieve` that takes four parameters: `query`, `top_k`, `namespace`, and `emb_model`.
- Embed the input `query` using the `emb_model` argument.
- Retrieve the `top_k` similar vectors to `query_emb` with metadata, specifying the `namespace` provided to the function as an argument.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv(override=True)

# Initialized the Pinecone client with API key (the OpenAI client is available as client
openai_api_key = os.getenv('OPENAI_API_KEY')

pinecone_api_key = os.getenv("PINECONE_API_KEY")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)

index = pc.Index('pinecone-datacamp')

def retrieve(
    query,
    top_k=5,
    namespace="youtube_rag_dataset",
    emb_model="text-embedding-3-small",
    score_threshold=0.0
):
    """
    Retrieve top-k relevant documents from Pinecone.

    Returns:
        docs: list of text chunks
        sources: list of (title, url)
    """

    try:
        # 🔹 Step 1: Create query embedding
        response = client.embeddings.create(
            input=query,
            model=emb_model
        )

        query_emb = list(response.data[0].embedding)

        # 🔹 Step 2: Query Pinecone
        results = index.query(
            vector=query_emb,
            top_k=top_k,
            namespace=namespace,
            include_metadata=True
        )

        matches = results.get("matches", [])

        # 🔹 Step 3: Extract data safely
        docs = []
        sources = []

        for match in matches:
            score = match.get("score", 0)

            # Optional: filter low-quality results
            if score < score_threshold:
                continue

            metadata = match.get("metadata", {})

            text = metadata.get("text", "")
            title = metadata.get("title", "Unknown Title")
            url = metadata.get("url", "No URL")

            if text:
                docs.append(text)
                sources.append((title, url))

        # 🔹 Step 4: Handle empty results
        if not docs:
            print("⚠️ No relevant documents found.")

        return docs, sources          # ← indented inside try (and inside function)

    except Exception as e:            # ← indented inside function
        print(f"❌ Retrieval error: {e}")
        return [], []

docs, sources = retrieve("how to use Pinecone for vector search?")
print(docs)
print(sources)