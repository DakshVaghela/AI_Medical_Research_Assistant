import xml.etree.ElementTree as ET


def parse_pubmed_xml(xml_text):

    root = ET.fromstring(xml_text)

    papers = []

    for article in root.findall(".//PubmedArticle"):

        pmid = ""

        title = ""

        abstract = ""

        journal = ""

        year = ""

        pmid_node = article.find(".//PMID")

        if pmid_node is not None:
            pmid = pmid_node.text

        title_node = article.find(".//ArticleTitle")

        if title_node is not None:
            title = "".join(
                title_node.itertext()
            )

        abstract_nodes = article.findall(
            ".//AbstractText"
        )

        abstract_parts = []

        for node in abstract_nodes:

            text = "".join(
                node.itertext()
            )

            abstract_parts.append(text)

        abstract = "\n".join(
            abstract_parts
        )

        journal_node = article.find(
            ".//Journal/Title"
        )

        if journal_node is not None:
            journal = journal_node.text

        year_node = article.find(
            ".//PubDate/Year"
        )

        if year_node is not None:
            year = year_node.text

        papers.append({
            "pmid": pmid,
            "title": title,
            "abstract": abstract,
            "journal": journal,
            "year": year
        })

    return papers