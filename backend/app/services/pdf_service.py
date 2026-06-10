import fitz


def extract_text_from_pdf(pdf_path: str):
    document = fitz.open(pdf_path)

    pages = []

    for page_number in range(len(document)):
        page = document[page_number]

        pages.append({
            "page": page_number + 1,
            "character_count": len(page.get_text()),
            "text": page.get_text()
        })

    return pages