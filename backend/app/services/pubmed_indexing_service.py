from app.services.pubmed_service import (
    search_pubmed,
    fetch_pubmed_details
)

from app.services.pubmed_parser_service import (
    parse_pubmed_xml
)

from app.services.document_chunking_service import (
    create_chunks
)

from app.services.embedding_service import (
    generate_embeddings
)

from app.services.qdrant_service import (
    store_pubmed_embeddings
)


def index_pubmed_topic(
    topic: str,
    max_papers: int = 100
):

    print(
        f"Searching PubMed for: {topic}"
    )

    pmids = search_pubmed(
        query=topic,
        max_results=max_papers
    )

    print(
        f"Found {len(pmids)} papers"
    )

    xml_data = fetch_pubmed_details(
        pmids
    )

    papers = parse_pubmed_xml(
        xml_data
    )

    total_chunks = 0

    for paper in papers:

        text = f"""
Title:
{paper['title']}

Abstract:
{paper['abstract']}
"""

        chunks = create_chunks(
            text
        )

        embeddings = generate_embeddings(
            chunks
        )

        store_pubmed_embeddings(
            embeddings=embeddings,
            paper=paper
        )

        total_chunks += len(chunks)

    return {
        "topic": topic,
        "papers_indexed": len(papers),
        "chunks_indexed": total_chunks
    }