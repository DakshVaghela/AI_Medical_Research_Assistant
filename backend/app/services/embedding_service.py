from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)


def generate_embeddings(chunks):

    embeddings = []

    for chunk in chunks:
        vector = model.encode(
            chunk["text"],
            normalize_embeddings=True
        )

        embeddings.append({
            "chunk_id": chunk["chunk_id"],
            "page": chunk["page"],
            "character_count": chunk["character_count"],
            "text": chunk["text"],
            "embedding": vector.tolist()
        })  

    return embeddings