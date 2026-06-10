from app.services.document_retrieval_service import (
    retrieve_document_context
)

from app.services.rag_service import (
    generate_rag_answer
)


def chat_with_document(
    query: str
):

    chunks = retrieve_document_context(
        query=query
    )

    answer = generate_rag_answer(
        query=query,
        retrieved_chunks=chunks
    )

    return {
        "query": query,
        "answer": answer,
        "sources": [
            {
                "chunk_id": chunk["chunk_id"],
                "source_file": chunk["source_file"]
            }
            for chunk in chunks
        ]
    }