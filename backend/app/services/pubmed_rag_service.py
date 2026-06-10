from app.services.llm_service import ask_llama


def generate_pubmed_answer(
    query: str,
    retrieved_papers: list
):

    context = ""

    for paper in retrieved_papers:

        context += f"""
PMID: {paper['pmid']}
Title: {paper['title']}
Journal: {paper['journal']}
Year: {paper['year']}

Abstract:
{paper['text']}

--------------------------------
"""

    prompt = f"""
You are a medical research assistant.

Answer ONLY using information found in the provided PubMed papers.

If multiple studies discuss the topic:
- Compare findings
- Highlight agreements/disagreements
- Mention limitations when present

If the answer cannot be found in the papers,
say:
"I could not find sufficient evidence in the retrieved PubMed papers."

Context:

{context}

Question:

{query}

Answer:
"""

    return ask_llama(prompt)