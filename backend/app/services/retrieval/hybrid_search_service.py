from rank_bm25 import BM25Okapi
from app.services.retrieval.search_service import semantic_search
import re
STOP_WORDS = {
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "has",
    "have",
    "in",
    "of",
    "to"
}

def preprocess_text(text):

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text.lower()
    )

    tokens = []

    for word in text.split():

        if word not in STOP_WORDS:
            tokens.append(word)

    return tokens

def bm25_search(
    query: str,
    chunks: list,
    top_k: int = 3
):

    tokenized_chunks = [
        preprocess_text(chunk["text"])
        for chunk in chunks
    ]

    bm25 = BM25Okapi(
        tokenized_chunks
    )

    tokenized_query = preprocess_text(
        query
    )

    scores = bm25.get_scores(
        tokenized_query
    )

    results = []

    for chunk, score in zip(
        chunks,
        scores
    ):

        results.append({
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"],
            "bm25_score": float(score)
        })

    results.sort(
        key=lambda x: x["bm25_score"],
        reverse=True
    )

    return results[:top_k]

def hybrid_search(
    query: str,
    chunks: list,
    embeddings: list,
    top_k: int = 5
):

    bm25_results = bm25_search(
        query=query,
        chunks=chunks,
        top_k=len(chunks)
    )

    vector_results = semantic_search(
        query=query,
        embeddings=embeddings,
        top_k=len(embeddings)
    )

    bm25_scores = {
        item["chunk_id"]: item["bm25_score"]
        for item in bm25_results
    }

    vector_scores = {
        item["chunk_id"]: item["score"]
        for item in vector_results
    }

    results = []

    for chunk in chunks:

        chunk_id = chunk["chunk_id"]

        bm25_score = bm25_scores.get(
            chunk_id,
            0
        )

        vector_score = vector_scores.get(
            chunk_id,
            0
        )

        final_score = (
            0.5 * bm25_score
            +
            0.5 * vector_score
        )

        results.append({
            "chunk_id": chunk_id,
            "text": chunk["text"],
            "bm25_score": bm25_score,
            "vector_score": vector_score,
            "final_score": final_score
        })

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results[:top_k]