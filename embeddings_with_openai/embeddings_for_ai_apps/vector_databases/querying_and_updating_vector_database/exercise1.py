"""
- Retrieve the netflix_titles collection, specifying the OpenAI embedding function so the query is embedded using the same function as the documents.
- Query the collection for "films about dogs" and return three results.
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    import chromadb
    from chromadb.errors import NotFoundError
    from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
except ImportError as exc:
    raise ImportError(
        "chromadb is not installed. Install it with `pip install chromadb` and try again."
    ) from exc

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to your .env file or environment variables."
    )


def main() -> None:
    # -----------------------------
    # Step 1: Create Client
    # -----------------------------
    client = chromadb.PersistentClient()

    # Retrieve the netflix_titles collection
    try:
        collection = client.get_collection(
            name="netflix_titles",
            embedding_function=OpenAIEmbeddingFunction(
                model_name="text-embedding-3-small",
                api_key=api_key,
            ),
        )
    except NotFoundError as exc:
        raise RuntimeError(
            "The netflix_titles collection does not exist in the current Chroma store. "
            "Run the collection creation/setup script first, or use the same PersistentClient path."
        ) from exc
    except Exception as exc:
        raise RuntimeError(
            "Could not retrieve the netflix_titles collection. "
            "Make sure it exists and was created with the same embedding function."
        ) from exc

    # Query the collection for "films about dogs"
    result = collection.query(
        query_texts=["films about dogs"],
        n_results=3,
    )

    print(result)


if __name__ == "__main__":
    main()