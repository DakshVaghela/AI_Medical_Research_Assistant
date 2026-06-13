import numpy as np
from app.services.indexing.embedding_service import model


def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1)
        * np.linalg.norm(vec2)
    )

def semantic_search(
    query: str,
    embeddings: list,
    top_k: int = 3
):

    query_embedding = model.encode(
        f"Represent this sentence for searching relevant passages: {query}",
        normalize_embeddings=True
    )

    results = []

    for item in embeddings:

        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        results.append({
            "chunk_id": item["chunk_id"],
            "text": item["text"],
            "score": float(score)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # return results[:top_k]
    return results