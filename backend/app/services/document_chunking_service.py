from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = []

    chunk_counter = 1

    for page in pages:

        page_number = page["page"]

        page_chunks = splitter.split_text(
            page["text"]
        )

        for chunk in page_chunks:

            chunks.append(
                {
                    "chunk_id": chunk_counter,
                    "chunk_position": chunk_counter,
                    "page": page_number,
                    "character_count": len(chunk),
                    "text": chunk
                }
            )

            chunk_counter += 1

    return chunks