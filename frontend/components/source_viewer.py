import streamlit as st

def show_sources(sources):

    if not sources:
        return

    st.divider()

    st.subheader("📚 Sources")

    for idx, source in enumerate(sources, start=1):

        with st.expander(f"Source {idx}"):

            if isinstance(source, dict):

                if "text" in source:
                    st.write(source["text"])

                if "score" in source:
                    st.caption(
                        f"Score: {source['score']}"
                    )

            else:
                st.write(source)