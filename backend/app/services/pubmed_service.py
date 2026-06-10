import requests


def search_pubmed(
    query: str,
    max_results: int = 20
):

    url = (
        "https://eutils.ncbi.nlm.nih.gov"
        "/entrez/eutils/esearch.fcgi"
    )

    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()

    return data["esearchresult"]["idlist"]


def fetch_pubmed_details(pmids):

    ids = ",".join(pmids)

    url = (
        "https://eutils.ncbi.nlm.nih.gov"
        "/entrez/eutils/efetch.fcgi"
    )

    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }

    response = requests.get(
        url,
        params=params
    )

    return response.text