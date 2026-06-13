from app.services.indexing.pdf_service import extract_text_from_pdf
from app.services.indexing.document_chunking_service import create_chunks
from app.services.indexing.embedding_service import generate_embeddings
from app.services.database.qdrant_service import (
    clear_uploaded_document_collection,
    store_uploaded_document_embeddings
)
from app.services.database.qdrant_service import (
    clear_uploaded_document_collection
)

def index_document(
    file_path: str,
    source_file: str
):

    print(
        f"Indexing document: {source_file}"
    )

    pages = extract_text_from_pdf(
        file_path
    )

    full_text = ""

    for page in pages:

        full_text += page["text"] + "\n"

    chunks = create_chunks(
        pages
    )

    embeddings = generate_embeddings(
        chunks
    )

    clear_uploaded_document_collection()

    store_uploaded_document_embeddings(
        embeddings,
        source_file
    )

    return {
        "source_file": source_file,
        "total_pages": len(pages),
        "total_chunks": len(chunks),
        "status": "indexed"
    }