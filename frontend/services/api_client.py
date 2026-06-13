import requests

API_URL = "http://localhost:8000"


def upload_document(file):

    files = {
        "file": (
            file.name,
            file.getvalue(),
            file.type
        )
    }

    response = requests.post(
        f"{API_URL}/upload-document",
        files=files
    )

    return response.json()


def chat_document(question):

    response = requests.post(
        f"{API_URL}/chat-document",
        params={
            "query": question
        }
    )

    return response.json()


def pubmed_chat(question):

    response = requests.get(
        f"{API_URL}/pubmed-chat",
        params={
            "query": question
        }
    )

    return response.json()


def collection_info():

    response = requests.get(
        f"{API_URL}/collection-info"
    )

    return response.json()