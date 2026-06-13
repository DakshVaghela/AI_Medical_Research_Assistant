from app.services.generation.llm_service import ask_llama


def generate_rag_answer(
    query: str,
    retrieved_chunks: list
):

    retrieved_chunks = sorted(
        retrieved_chunks,
        key=lambda x: x.get(
            "chunk_id",
            0
        )
    )

    context = ""

    for chunk in retrieved_chunks:

        context += (
            f"{chunk['text']}\n\n"
        )

        prompt = f"""
You are an AI document assistant.

Your task is to answer the user's question using ONLY the provided context.

Rules:

- Use information only from the context.
- Include every relevant fact needed to answer the question.
- If multiple relevant items exist, include all of them.
- Preserve important names, numbers, dates, and technical terms.
- Do not invent information.
- Do not assume facts not present in the context.
- If the answer cannot be found, respond exactly:

I could not find that information in the document.

Context:
{context}

Question:
{query}

Answer:
"""

    answer = ask_llama(
        prompt
    )

    return answer