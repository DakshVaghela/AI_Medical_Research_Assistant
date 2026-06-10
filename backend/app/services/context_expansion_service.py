def expand_neighbor_chunks(
    retrieved_chunks,
    all_chunks
):

    chunk_lookup = {
        chunk["chunk_id"]: chunk
        for chunk in all_chunks
    }

    expanded = {}

    for chunk in retrieved_chunks:

        chunk_id = chunk["chunk_id"]

        expanded[chunk_id] = chunk

        previous_chunk = chunk_lookup.get(
            chunk_id - 1
        )

        next_chunk = chunk_lookup.get(
            chunk_id + 1
        )

        if previous_chunk:
            expanded[
                previous_chunk["chunk_id"]
            ] = previous_chunk

        if next_chunk:
            expanded[
                next_chunk["chunk_id"]
            ] = next_chunk

    return sorted(
        expanded.values(),
        key=lambda x: x["chunk_id"]
    )