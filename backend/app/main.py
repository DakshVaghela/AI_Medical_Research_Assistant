from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.services.evaluation_service import (
    evaluate_document_rag
)
from app.services.document_indexing_service import (
    index_document
)
from app.services.retrieval_evaluation_service import (
    evaluate_retrieval
)
from app.services.document_chat_service import (
    chat_with_document
)

from app.services.pubmed_chat_service import (
    chat_with_pubmed
)

from app.services.qdrant_service import (
    search_uploaded_document,
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
    return chat_with_document(
        query=query
    )


# @app.get("/pubmed-chat")
# def pubmed_chat(
#     query: str
# ):

#     return chat_with_pubmed(
#         query=query
#     )


# @app.get("/debug-search")
# def debug_search(
#     query: str
# ):

#     return search_uploaded_document(
#         query=query,
#         top_k=20
#     )

# @app.get("/evaluate-document")
# def evaluate_document():

#     return evaluate_document_rag()

# @app.get("/evaluate-retrieval")
# def retrieval_eval():

#     return evaluate_retrieval()

@app.get("/collection-info")
def get_collection_info():

    return collection_info()