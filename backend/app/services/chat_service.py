from app.services.retrieval_service import (
    retrieve_context
)

from app.services.rag_service import (
    generate_rag_answer
)

def chat_with_documents(
    query: str
):

    context_chunks = retrieve_context(
        query=query,
        all_chunks=[]
    )

    answer = generate_rag_answer(
        query=query,
        retrieved_chunks=context_chunks
    )

    return {
        "query": query,
        "answer": answer,
        "sources": [
            {
                "chunk_id":
                    chunk["chunk_id"],
                "source_file":
                    chunk["source_file"]
            }
            for chunk in context_chunks
        ]
    }