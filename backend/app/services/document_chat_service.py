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
    primary_page = None

    if chunks:
        primary_page = chunks[0].get("page")

    if primary_page:

        answer += (
            f"\n\n📍 Primary Source Page: {primary_page}"
        )
    # top_pages = []

    # for chunk in chunks[:2]:

    #     page = chunk.get("page")

    #     if page and page not in top_pages:

    #         top_pages.append(page)
    
    # if len(top_pages) == 1:

    #     answer += (
    #         f"\n\n📍 Primary Source Page: {top_pages[0]}"
    #     )

    # elif len(top_pages) > 1:

    #     answer += (
    #         f"\n\n📍 Primary Source Pages: "
    #         f"{', '.join(map(str, top_pages))}"
    #     )
        
    return {
        "query": query,
        "answer": answer,
        "sources": [
            {
                "chunk_id": chunk["chunk_id"],
                "source_file": chunk["source_file"],
                "page": chunk.get("page")
            }
            for chunk in chunks
        ]
    }