from app.services.retrieval.pubmed_retrieval_service import (
    retrieve_pubmed_context
)

from app.services.generation.pubmed_rag_service import (
    generate_pubmed_answer
)


def chat_with_pubmed(
    query: str
):

    papers = retrieve_pubmed_context(
        query
    )

    answer = generate_pubmed_answer(
        query=query,
        retrieved_papers=papers
    )

    return {
        "query": query,
        "answer": answer,
        "sources": [
            {
                "pmid": p["pmid"],
                "title": p["title"]
            }
            for p in papers
        ]
    }