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

Use ONLY information from the retrieved PubMed papers.

Rules:
- Do not invent information.
- Do not repeat the same study twice.
- Cite PMID numbers.
- Ignore papers that are not directly relevant to the question.

Format:

Summary

Key Approaches
- Approach
- Description
- PMID

Research Takeaway

Context:

{context}

Question:

{query}

Answer:
"""

    return ask_llama(prompt)