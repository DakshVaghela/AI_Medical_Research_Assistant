from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.services.qdrant_service import search_qdrant
from app.services.document_indexing_service import (
    index_document
)

from app.services.chat_service import (
    chat_with_documents
)

from app.services.qdrant_service import (
    collection_info
)

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@app.get("/")
def root():

    return {
        "status": "running",
        "project": "AI Document Intelligence System"
    }


@app.post("/upload-document")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = index_document(
        file_path=file_path,
        source_file=file.filename
    )

    return result


@app.post("/chat-document")
async def chat_document(
    query: str
):

    result = chat_with_documents(
        query=query,
    )

    return result


@app.get("/collection-info")
def get_collection_info():

    return collection_info()


@app.get("/debug-search")
def debug_search(query: str):

    results = search_qdrant(
        query=query,
        top_k=20
    )

    return results