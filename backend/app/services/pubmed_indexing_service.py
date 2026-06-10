from app.services.pubmed_service import (
    search_pubmed,
    fetch_pubmed_details
)

from app.services.pubmed_parser_service import (
    parse_pubmed_xml
)

from app.services.document_chunking_service import create_chunks

from app.services.embedding_service import (
    generate_embeddings
)

from app.services.qdrant_service import (
    store_pubmed_embeddings
)


def index_pubmed_topic(
    topic: str,
    max_papers: int = 20
):

    ids = search_pubmed(
        topic,
        max_results=max_papers
    )

    xml = fetch_pubmed_details(ids)

    papers = parse_pubmed_xml(xml)

    total_chunks = 0

    for paper in papers:

        content = f"""
Title:
{paper['title']}

Abstract:
{paper['abstract']}
"""

        chunks = create_chunks(content)

        embeddings = generate_embeddings(
            chunks
        )

        store_pubmed_embeddings(
            embeddings=embeddings,
            paper=paper
        )

        total_chunks += len(chunks)

    return {
        "papers": len(papers),
        "chunks": total_chunks
    }