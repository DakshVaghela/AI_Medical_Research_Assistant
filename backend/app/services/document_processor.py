import fitz

from app.services.pdf_service import extract_text_from_pdf


def is_scanned_pdf(pdf_path: str):

    document = fitz.open(pdf_path)

    first_page = document[0]

    text = first_page.get_text().strip()

    return len(text) == 0


def process_document(pdf_path: str):

    scanned = is_scanned_pdf(pdf_path)

    if scanned:
        return {
            "document_type": "scanned_pdf",
            "message": "OCR required"
        }

    pages = extract_text_from_pdf(pdf_path)

    return {
        "document_type": "digital_pdf",
        "pages": pages
    }