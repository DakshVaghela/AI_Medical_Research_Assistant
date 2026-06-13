from sentence_transformers import CrossEncoder


reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_results(
    query: str,
    retrieved_chunks: list,
    top_k: int = 5
):

    pairs = []

    for chunk in retrieved_chunks:

        pairs.append(
            [query, chunk["text"]]
        )

    scores = reranker.predict(
        pairs
    )

    reranked = []

    for chunk, score in zip(
        retrieved_chunks,
        scores
    ):

        chunk["rerank_score"] = float(score)

        reranked.append(
            chunk
        )

    reranked.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked[:top_k]