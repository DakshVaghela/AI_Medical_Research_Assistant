from app.services.llm_service import (
    ask_llama
)


def generate_document_answer(
    query: str,
    retrieved_chunks: list
):

    context = ""

    for chunk in retrieved_chunks:

        context += f"""
{chunk['text']}

----------------
"""

    prompt = f"""
You are a document analysis assistant.

Answer ONLY using the document context.

Rules:
- Do not invent information.
- If information is missing, say so.
- Use all relevant evidence.

Context:

{context}

Question:

{query}

Answer:
"""

    return ask_llama(
        prompt
    )