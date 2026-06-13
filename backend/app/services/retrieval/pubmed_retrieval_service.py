from app.services.database.qdrant_service import (
    search_pubmed_qdrant
)

from app.services.retrieval.reranker_service import (
    rerank_results
)


def retrieve_pubmed_context(
    query: str
):

    retrieved = search_pubmed_qdrant(
        query=query,
        top_k=30
    )

    reranked = rerank_results(
        query=query,
        retrieved_chunks=retrieved,
        top_k=20
    )

    unique = []
    seen_pmids = set()

    for chunk in reranked:

        pmid = str(chunk["pmid"]).strip()

        if pmid not in seen_pmids:

            unique.append(chunk)
            seen_pmids.add(pmid)

    return unique[:5]
