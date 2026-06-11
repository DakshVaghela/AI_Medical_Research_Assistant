import streamlit as st
import requests

from components.source_viewer import show_sources

if "messages" not in st.session_state:
    st.session_state.messages = []

API_URL = "http://localhost:8000"

st.title("💬 Chat With Documents")

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )
question = st.chat_input(
    "Ask a question"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    response = requests.post(
        "http://localhost:8000/chat-document",
        params={
            "query": question
        }
    )

    data = response.json()

    answer = data.get(
        "answer",
        str(data)
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message(
        "assistant"
    ):
        st.write(answer)

        show_sources(
            data.get(
                "sources",
                []
            )
        )