""" 
- Initialize the Pinecone client with your API key (the OpenAI client is available as `client`).
- Retrieve the three most similar documents to the `query` text from the `'youtube_rag_dataset'` namespace.
- Generate a response to the provided `prompt` and `sys_prompt` using OpenAI's `'gpt-4o-mini'` model, specified using the `chat_model` function argument.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv(override=True)

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
    try:
        response = client.embeddings.create(input=query, model=emb_model)
        query_emb = list(response.data[0].embedding)

        results = index.query(
            vector=query_emb,
            top_k=top_k,
            namespace=namespace,
            include_metadata=True
        )

        matches = results.get("matches", [])
        docs, sources = [], []

        for match in matches:
            if match.get("score", 0) < score_threshold:
                continue
            metadata = match.get("metadata", {})
            text = metadata.get("text", "")
            title = metadata.get("title", "Unknown Title")
            url = metadata.get("url", "No URL")
            if text:
                docs.append(text)
                sources.append((title, url))

        if not docs:
            print("⚠️ No relevant documents found.")

        return docs, sources

    except Exception as e:
        print(f"❌ Retrieval error: {e}")
        return [], []


def prompt_with_context_builder(query, documents, sources):
    context = "\n\n".join(documents) if documents else ""
    prompt = f"Context:\n\n{context}\n\nQuestion: {query}"
    return prompt


def question_answering(prompt, sources, chat_model):
    system_prompt = """
You are a precise and reliable AI assistant.

Rules:
- Answer ONLY using the provided context
- If the answer is not in the context, say:
  "I don't know based on the provided context."
- Do NOT make up information
- Keep answers concise and clear
"""
    if not prompt or "Context:\n\n" in prompt:
        return "⚠️ No relevant context found to answer the question."

    res = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = res.choices[0].message.content.strip()

    if sources:
        source_text = "\n\n📚 Sources:\n"
        for i, (title, url) in enumerate(sources):
            source_text += f"{i+1}. {title}\n   {url}\n"
        answer += source_text

    return answer


# --- Run ---
query = "How to build next-level Q&A with OpenAI"

documents, sources = retrieve(
    query,
    top_k=3,
    namespace='youtube_rag_dataset',
    emb_model="text-embedding-3-small"
)

prompt = prompt_with_context_builder(query, documents, sources)

answer = question_answering(
    prompt=prompt,
    sources=sources,
    chat_model='gpt-4o-mini'
)

print(answer)
