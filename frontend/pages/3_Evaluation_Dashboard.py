import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📊 Evaluation Dashboard")

try:

    rag_eval = requests.get(
        f"{API_URL}/evaluate-document"
    ).json()

    retrieval_eval = requests.get(
        f"{API_URL}/evaluate-retrieval"
    ).json()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Hit Rate",
            rag_eval.get(
                "hit_rate",
                0
            )
        )

        st.metric(
            "Recall",
            rag_eval.get(
                "avg_recall",
                0
            )
        )

    with col2:
        st.metric(
            "Precision",
            rag_eval.get(
                "avg_precision",
                0
            )
        )

        st.metric(
            "MRR",
            rag_eval.get(
                "mrr",
                0
            )
        )

    st.subheader(
        "Retrieval Evaluation"
    )

    st.json(
        retrieval_eval
    )

except Exception as e:

    st.error(
        str(e)
    )