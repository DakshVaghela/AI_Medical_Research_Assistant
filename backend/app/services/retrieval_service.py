# from app.services.qdrant_service import (
#     search_qdrant
# )

# from app.services.reranker_service import (
#     rerank_results
# )


# def retrieve_context(
#     query: str
# ):

#     retrieved_chunks = search_qdrant(
#         query=query,
#         top_k=20
#     )

#     reranked_chunks = rerank_results(
#         query=query,
#         retrieved_chunks=retrieved_chunks,
#         top_k=5
#     )

#     unique_chunks = []

#     seen = set()
#     print("====================\n")
#     print("\nFINAL RETRIEVED CHUNKS")
#     print("====================\n")
#     for chunk in reranked_chunks:
#         print(
#             f"Chunk: {chunk['chunk_id']} | File: {chunk['source_file']}"
#         )
#         print("====================\n")
#         key = (
#             chunk["chunk_id"],
#             chunk["source_file"]
#         )

#         if key not in seen:

#             unique_chunks.append(
#                 chunk
#             )

#             seen.add(
#                 key
#             )

#     return unique_chunks
from app.services.qdrant_service import search_qdrant
from app.services.reranker_service import rerank_results
from app.services.context_expansion_service import expand_neighbor_chunks


def retrieve_context(
    query: str,
    all_chunks: list
):

    retrieved_chunks = search_qdrant(
        query=query,
        top_k=50
    )
    print("\nQDRANT RESULTS\n")

    for chunk in retrieved_chunks:
        print(
            chunk["chunk_id"],
            chunk["score"]
        )

    reranked_chunks = rerank_results(
        query=query,
        retrieved_chunks=retrieved_chunks,
        top_k=10
    )

    print("\nRERANKED CHUNKS\n")

    for chunk in reranked_chunks:
        print(
            chunk["chunk_id"],
            chunk["rerank_score"]
        )

    expanded_chunks = expand_neighbor_chunks(
        reranked_chunks,
        all_chunks
    )

    return expanded_chunks