from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text: str):

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

    raw_chunks = splitter.split_text(text)

    chunks = []

    for index, chunk in enumerate(raw_chunks):

        chunks.append({
            "chunk_id": index + 1,
            "chunk_position": index + 1,
            "character_count": len(chunk),
            "text": chunk
        })

    return chunks