from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance
)

from app.services.embedding_service import model

import hashlib


client = QdrantClient(
    host="localhost",
    port=6333
)


def create_collection():

    collections = client.get_collections()

    existing = [
        c.name
        for c in collections.collections
    ]

    if "documents" not in existing:

        client.create_collection(
            collection_name="documents",
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )

        print(
            "documents collection created"
        )


def create_pubmed_collection():

    collections = client.get_collections()

    existing = [
        c.name
        for c in collections.collections
    ]

    if "pubmed_documents" not in existing:

        client.create_collection(
            collection_name="pubmed_documents",
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )

        print(
            "pubmed_documents collection created"
        )


def search_qdrant(
    query: str,
    top_k: int = 5
):

    query_vector = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    response = client.query_points(
        collection_name="documents",
        query=query_vector,
        limit=top_k
    )

    matches = []

    for point in response.points:

        matches.append({
            "score": point.score,
            "chunk_id": point.payload["chunk_id"],
            "text": point.payload["text"],
            "source_file": point.payload["source_file"]
        })

    return matches


def store_embeddings(
    embeddings,
    source_file
):

    points = []

    for item in embeddings:

        point_id = int(
            hashlib.md5(
                f"{source_file}_{item['chunk_id']}".encode()
            ).hexdigest()[:8],
            16
        )

        points.append(
            PointStruct(
                id=point_id,
                vector=item["embedding"],
                payload={
                    "chunk_id": item["chunk_id"],
                    "text": item["text"],
                    "source_file": source_file,
                    "character_count": item["character_count"]
                }
            )
        )

    client.upsert(
        collection_name="documents",
        points=points
    )

    print(
        f"{len(points)} vectors stored"
    )


def store_pubmed_embeddings(
    embeddings,
    paper
):

    points = []

    for item in embeddings:

        point_id = int(
            hashlib.md5(
                f"{paper['pmid']}_{item['chunk_id']}".encode()
            ).hexdigest()[:8],
            16
        )

        points.append(
            PointStruct(
                id=point_id,
                vector=item["embedding"],
                payload={
                    "pmid": paper["pmid"],
                    "title": paper["title"],
                    "journal": paper["journal"],
                    "year": paper["year"],
                    "chunk_id": item["chunk_id"],
                    "text": item["text"]
                }
            )
        )

    client.upsert(
        collection_name="pubmed_documents",
        points=points
    )

    print(
        f"{len(points)} PubMed vectors stored"
    )

def search_pubmed_qdrant(
    query: str,
    top_k: int = 5
):

    query_vector = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    response = client.query_points(
        collection_name="pubmed_documents",
        query=query_vector,
        limit=top_k
    )

    results = []

    for point in response.points:

        results.append({
            "score": point.score,
            "pmid": point.payload["pmid"],
            "title": point.payload["title"],
            "journal": point.payload["journal"],
            "year": point.payload["year"],
            "text": point.payload["text"]
        })

    return results

def collection_info():

    return client.get_collection(
        "documents"
    )


def delete_collection():

    client.delete_collection(
        collection_name="documents"
    )

    print(
        "documents deleted"
    )