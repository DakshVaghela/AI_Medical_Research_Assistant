from app.services.database.qdrant_service import search_qdrant
from app.services.retrieval.reranker_service import rerank_results
from app.services.retrieval.context_expansion_service import (
    expand_neighbor_chunks
)


def retrieve_context(
    query: str,
    all_chunks: list
):

    retrieved = search_qdrant(
        query=query,
        top_k=20
    )

    reranked = rerank_results(
        query=query,
        retrieved_chunks=retrieved,
        top_k=5
    )

    expanded = expand_neighbor_chunks(
        reranked,
        all_chunks
    )

    return expanded