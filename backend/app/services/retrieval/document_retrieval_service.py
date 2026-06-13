from app.services.database.qdrant_service import (
    search_uploaded_document
)

from app.services.retrieval.reranker_service import (
    rerank_results
)


def retrieve_document_context(
    query: str
):

    retrieved = search_uploaded_document(
        query=query,
        top_k=20
    )

    reranked = rerank_results(
        query=query,
        retrieved_chunks=retrieved,
        top_k=10
    )

    return reranked