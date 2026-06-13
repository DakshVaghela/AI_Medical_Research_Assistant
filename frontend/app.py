# import streamlit as st

# from services.api_client import (
#     upload_document,
#     chat_document,
#     pubmed_chat,
#     collection_info
# )

# # --------------------------------------------------
# # Page Config
# # --------------------------------------------------

# st.set_page_config(
#     page_title="DocIntel.AI",
#     layout="wide"
# )

# # --------------------------------------------------
# # Styling
# # --------------------------------------------------

# st.markdown("""
# <style>

# Primary Background  : #030712
# Sidebar             : #0B1220
# Card                : #111827
# Card Hover          : #1F2937

# Accent Cyan         : #06B6D4
# Accent Purple       : #8B5CF6
# Accent Green        : #10B981

# Text Primary        : #F8FAFC
# Text Secondary      : #94A3B8
# Border              : #1E293B
            
# .stApp{
#     background:#030712;
# }

# [data-testid="stSidebar"]{
#     background:#071224;
# }

# [data-testid="stChatMessage"]{
#     background:#0f172a;
#     border:1px solid #1e293b;
#     border-radius:16px;
#     padding:16px;
#     margin-bottom:12px;
# }

# .stChatInput{
#     border-radius:20px;
# }

# .stButton button{
#     border-radius:12px;
#     width:100%;
# }

# .stMetric{
#     background:#111827;
#     padding:10px;
#     border-radius:12px;
# }
# [data-testid="stChatMessage"] {
#     border-radius: 18px;
#     padding: 16px;
#     margin-bottom: 10px;
# }

# [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
#     background: #1e293b;
# }

# [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
#     background: #0f172a;
# }
            
# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # Session State
# # --------------------------------------------------

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "uploaded_docs" not in st.session_state:
#     st.session_state.uploaded_docs = []

# if "active_document" not in st.session_state:
#     st.session_state.active_document = None
# # --------------------------------------------------
# # Helper Function
# # --------------------------------------------------

# def render_sources(sources):

#     if not sources:
#         return

#     with st.expander(
#         f"📚 Sources ({len(sources)})"
#     ):

#         for source in sources:

#             # Document RAG Sources
#             if "source_file" in source:

#                 st.markdown(
#                     f"""
#                     <div style="
#                     background:#0f172a;
#                     padding:12px;
#                     border-radius:10px;
#                     margin-bottom:10px;
#                     ">

#                     📄 <b>{source['source_file']}</b><br>

#                     Chunk ID: {source['chunk_id']}

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#             # PubMed Sources
#             elif "pmid" in source:

#                 st.markdown(
#                     f"""
#                     <div style="
#                     background:#0f172a;
#                     padding:12px;
#                     border-radius:10px;
#                     margin-bottom:10px;
#                     ">

#                     🧬 PMID: {source.get('pmid')}<br>

#                     <b>{source.get('title','N/A')}</b><br>

#                     {source.get('journal','N/A')}

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#             else:

#                 st.json(source)

# # --------------------------------------------------
# # Sidebar
# # --------------------------------------------------

# # --------------------------------------------------
# # Sidebar
# # --------------------------------------------------

# with st.sidebar:

#     # =========================
#     # Logo / Header
#     # =========================

#     st.markdown("""
# <div style="
# background:linear-gradient(
# 135deg,
# #0f172a,
# #111827
# );
# padding:20px;
# border-radius:20px;
# border:1px solid #1e293b;
# text-align:center;
# ">

# <h2 style="margin:0;">
# 🚀 DocIntel.AI
# </h2>

# <p style="
# color:#94a3b8;
# margin-top:8px;
# ">
# AI Document Intelligence
# </p>

# </div>
# """, unsafe_allow_html=True)
#     # =========================
#     # Mode Selection
#     # =========================

#     st.markdown("### 🧠 Knowledge Source")

#     chat_mode = st.radio(
#         "",
#         [
#             "📄 Document RAG",
#             "🧬 PubMed Research"
#         ]
#     )

#     st.divider()

#     # =========================
#     # Document Mode
#     # =========================

#     if "Document" in chat_mode:

#         st.markdown("### 📤 Upload Document")

#         uploaded_file = st.file_uploader(
#             "Choose PDF",
#             type=["pdf"]
#         )

#         if uploaded_file:

#             st.markdown("### 📚 Selected Document")

#             st.markdown(
#                 f"""
#                 <div style="
#                 background:#111827;
#                 padding:12px;
#                 border-radius:12px;
#                 margin-bottom:10px;
#                 ">
#                 📄 {uploaded_file.name}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             # Auto Index
#             if (
#                 st.session_state.active_document
#                 != uploaded_file.name
#             ):

#                 with st.spinner(
#                     "Indexing document..."
#                 ):

#                     upload_document(
#                         uploaded_file
#                     )

#                 st.session_state.active_document = (
#                     uploaded_file.name
#                 )

#                 st.session_state.messages = []

#                 st.success(
#                     "Document indexed successfully"
#                 )

#                 st.rerun()

#         # Active Document

#         if st.session_state.active_document:

#             st.markdown(
#                 "### 📄 Active Document"
#             )

#             st.markdown(
#                 f"""
#                 <div style="
#                 background:#0f172a;
#                 padding:12px;
#                 border-radius:12px;
#                 margin-bottom:10px;
#                 ">
#                 {st.session_state.active_document}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#     # =========================
#     # PubMed Mode
#     # =========================

#     else:

#         st.markdown("""
#         <div style="
#         background:#0f172a;
#         padding:12px;
#         border-radius:12px;
#         margin-bottom:10px;
#         color:white;
#         ">

#         🧬 PubMed Research Mode

#         Searches indexed medical
#         research papers.

#         No document upload required.

#         </div>
#         """, unsafe_allow_html=True)

#     st.divider()

#     # =========================
#     # Features
#     # =========================

#     st.markdown("""
#     ### 🎯 Features

#     ✅ Document RAG

#     ✅ PubMed RAG

#     ✅ Source Citation

#     ✅ Semantic Search

#     ✅ Qdrant Vector DB
#     """)

#     st.divider()

#     # =========================
#     # System Status
#     # =========================

#     try:

#         info = collection_info()

#         st.markdown("""
#         <div style="                      
#         background:#14532d;
#         padding:12px;
#         border-radius:12px;
#         color:white;
#         text-align:center;
#         margin-bottom:10px;
#         ">
#         🟢 Backend Online
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("### 📊 Statistics")

#         st.metric(
#             "Chunks Indexed",
#             info.get("points_count", 0)
#         )

#         st.metric(
#             "Messages",
#             len(
#                 st.session_state.messages
#             )
#         )

#     except Exception:

#         st.error(
#             "Backend Offline"
#         )

# # --------------------------------------------------
# # Welcome Screen
# # --------------------------------------------------

# if not st.session_state.messages:

#     st.markdown("""
# <div style="text-align:center;padding-top:120px;">

# <h1>🚀 DocIntel.AI</h1>
# <h2>AI-Powered Document Intelligence</h2>
# <h3>Ask Questions.</h3>
# <h3>Analyze Documents.</h3>
# <h3>Search Medical Research.</h3>
                
# <h3>Powered by RAG + Qdrant + PubMed</h3>
# <p style="font-size:20px;color:#94a3b8;">
# AI-Powered Document Intelligence Platform
# </p>

# <br>

# <p style="font-size:16px;color:#64748b;">
# Upload documents, search medical literature,
# and get grounded answers with citations.
# </p>

# </div>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # Chat History
# # --------------------------------------------------

# for message in st.session_state.messages:

#     with st.chat_message(
#         message["role"]
#     ):

#         st.markdown(
#             message["content"]
#         )

#         if (
#             message["role"] == "assistant"
#             and "sources" in message
#         ):

#             render_sources(
#                 message["sources"]
#             )


# # --------------------------------------------------
# # Chat Input
# # --------------------------------------------------

# question = st.chat_input(
#     "Ask your document anything..."
# )

# if question:

#     # User Message
#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": question
#         }
#     )

#     with st.chat_message("user"):

#         st.markdown(question)

#     # Assistant Placeholder
#     assistant_placeholder = st.empty()

#     import time

#     stages = [
#         "🔍 Searching relevant chunks...",
#         "🧠 Re-ranking retrieved results...",
#         "🤖 Generating grounded answer..."
#     ]

#     for stage in stages:

#         assistant_placeholder.markdown(
#             f"""
#             <div style="
#             background:#0f172a;
#             border:1px solid #1e293b;
#             padding:15px;
#             border-radius:15px;
#             margin-bottom:10px;
#             color:white;
#             ">
#             {stage}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         time.sleep(1.0)

#     try:

#         if "Document" in chat_mode:

#             result = chat_document(
#                 question
#             )

#         else:

#             result = pubmed_chat(
#                 question
#             )

#         answer = result.get(
#             "answer",
#             "No answer found."
#         )

#         sources = result.get(
#             "sources",
#             []
#         )

#     except Exception as e:

#         answer = f"Error: {e}"
#         sources = []

#     assistant_placeholder.empty()

#     # Save Assistant Message
#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": answer,
#             "sources": sources
#         }
#     )

#     with st.chat_message("assistant"):

#         st.markdown(answer)

#         render_sources(
#             sources
#         )

#     st.rerun()
        
#         # col1, col2, col3 = st.columns(3)

#         # with col1:
#         #     st.metric(
#         #         "Mode",
#         #         "Document"
#         #         if "Document" in chat_mode
#         #         else "PubMed"
#         #     )

#         # with col2:
#         #     st.metric(
#         #         "Sources",
#         #         len(sources)
#         #     )

#         # with col3:
#         #     st.metric(
#         #         "Status",
#         #         "Success"
#         #     )

import streamlit as st

from services.api_client import (
    upload_document,
    chat_document,
    pubmed_chat,
    collection_info
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="DocIntel.AI",
    page_icon="🛰️",
    layout="wide"
)

# --------------------------------------------------
# Styling
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ============================================
   DESIGN TOKENS
   Primary Background  : #030712
   Sidebar             : #060B16
   Card                : #0F172A
   Card Border         : #1E293B
   Card Border Active  : rgba(6,182,212,0.45)
   Accent Cyan         : #06B6D4
   Accent Violet       : #8B5CF6
   Accent Green        : #10B981
   Text Primary        : #F8FAFC
   Text Secondary      : #94A3B8
   ============================================ */

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at 12% 0%, rgba(6,182,212,0.10), transparent 35%),
        radial-gradient(circle at 88% 12%, rgba(139,92,246,0.10), transparent 40%),
        #030712;
}

/* Hide default chrome clutter */
#MainMenu, footer {visibility:hidden;}

/* ============================================
   SIDEBAR
   ============================================ */

[data-testid="stSidebar"]{
    background:#060B16;
    border-right:1px solid #141d2e;
}

[data-testid="stSidebar"] h3{
    font-family:'Space Grotesk', sans-serif;
    font-weight:600;
    letter-spacing:0.06em;
    text-transform:uppercase;
    font-size:0.75rem;
    color:#94A3B8;
    margin-top:1.5rem;
    margin-bottom:0.6rem;
}

/* Radio buttons -> segmented pill control */
[data-testid="stSidebar"] [role="radiogroup"]{
    background:#0B1220;
    border:1px solid #1E293B;
    border-radius:14px;
    padding:6px;
    gap:4px;
}

[data-testid="stSidebar"] [role="radiogroup"] label{
    border-radius:10px;
    padding:8px 10px;
    transition:all 0.15s ease;
    font-family:'Space Grotesk', sans-serif;
    font-weight:500;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover{
    background:#141d2e;
}

/* Divider */
[data-testid="stSidebar"] hr{
    border-color:#141d2e;
    margin:1.4rem 0;
}

/* File uploader */
[data-testid="stFileUploaderDropzone"]{
    background:#0B1220 !important;
    border:1.5px dashed #2a3a52 !important;
    border-radius:14px !important;
    transition:border-color 0.2s ease;
}

[data-testid="stFileUploaderDropzone"]:hover{
    border-color:#06B6D4 !important;
}

/* ============================================
   BUTTONS
   ============================================ */

.stButton button{
    border-radius:12px;
    width:100%;
    background:linear-gradient(135deg, #06B6D4, #8B5CF6);
    color:#F8FAFC;
    border:none;
    font-family:'Space Grotesk', sans-serif;
    font-weight:600;
    letter-spacing:0.01em;
    transition:filter 0.15s ease, transform 0.1s ease;
}

.stButton button:hover{
    filter:brightness(1.12);
    transform:translateY(-1px);
}

/* ============================================
   METRICS
   ============================================ */

[data-testid="stMetric"]{
    background:#0B1220;
    border:1px solid #1E293B;
    padding:14px 16px;
    border-radius:14px;
}

[data-testid="stMetricLabel"]{
    color:#94A3B8 !important;
    font-family:'Space Grotesk', sans-serif;
    font-size:0.72rem !important;
    text-transform:uppercase;
    letter-spacing:0.08em;
}

[data-testid="stMetricValue"]{
    font-family:'JetBrains Mono', monospace;
    background:linear-gradient(135deg,#06B6D4,#8B5CF6);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* ============================================
   CHAT MESSAGES
   ============================================ */

[data-testid="stChatMessage"]{
    border-radius:18px;
    padding:16px 18px;
    margin-bottom:12px;
    border:1px solid #1E293B;
    box-shadow:0 4px 24px -10px rgba(0,0,0,0.7);
    animation:fade-in-up 0.35s ease;
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){
    background:#101a30;
    border-color:rgba(139,92,246,0.35);
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){
    background:#0B1220;
    border-color:rgba(6,182,212,0.30);
}

/* ============================================
   CHAT INPUT
   ============================================ */

[data-testid="stChatInput"]{
    justify-content:center;
    position:sticky;
    margin: 5px auto;
    width:50%;
    display:center;
    border-radius:18px;
    border:1px solid #1E293B;
    background:#0B1220;
}

[data-testid="stChatInput"]:focus-within{
    border-color:#06B6D4;
    box-shadow:0 0 0 1px rgba(6,182,212,0.35), 0 0 28px -6px rgba(6,182,212,0.45);
}

/* ============================================
   EXPANDER (sources)
   ============================================ */

[data-testid="stExpander"]{
    border:1px solid #1E293B;
    border-radius:14px;
    background:#0B1220;
    overflow:hidden;
}

/* ============================================
   SCROLLBAR
   ============================================ */

::-webkit-scrollbar{ width:8px; height:8px; }
::-webkit-scrollbar-track{ background:#030712; }
::-webkit-scrollbar-thumb{ background:#1E293B; border-radius:8px; }
::-webkit-scrollbar-thumb:hover{ background:#334155; }

/* ============================================
   ANIMATIONS
   ============================================ */

@keyframes fade-in-up{
    from { opacity:0; transform:translateY(8px); }
    to { opacity:1; transform:translateY(0); }
}

@keyframes pulse-dot{
    0%, 100% { box-shadow:0 0 0 0 rgba(16,185,129,0.55); }
    50% { box-shadow:0 0 0 6px rgba(16,185,129,0); }
}

@keyframes shimmer{
    0% { background-position:-200% 0; }
    100% { background-position:200% 0; }
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_docs" not in st.session_state:
    st.session_state.uploaded_docs = []

if "active_document" not in st.session_state:
    st.session_state.active_document = None
# --------------------------------------------------
# Helper Function
# --------------------------------------------------

def render_sources(sources):

    if not sources:
        return

    with st.expander(
        f"📚 Sources · {len(sources)} referenced"
    ):

        for source in sources:

            # Document RAG Sources
            if "source_file" in source:

                st.markdown(
                    f"""
                    <div style="
                    background:linear-gradient(135deg, #0f172a, #111c33);
                    border:1px solid #1e293b;
                    border-left:3px solid #06B6D4;
                    padding:12px 14px;
                    border-radius:10px;
                    margin-bottom:10px;
                    ">

                    <span style="font-size:1.1em;">📄</span>
                    <b style="color:#F8FAFC;">{source['source_file']}</b>

                    <div style="
                    margin-top:4px;
                    font-family:'JetBrains Mono', monospace;
                    font-size:0.78em;
                    color:#94A3B8;
                    ">
                    Chunk ID&nbsp;·&nbsp;{source['chunk_id']}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # PubMed Sources
            elif "pmid" in source:

                st.markdown(
                    f"""
                    <div style="
                    background:linear-gradient(135deg, #0f172a, #1a1330);
                    border:1px solid #1e293b;
                    border-left:3px solid #8B5CF6;
                    padding:12px 14px;
                    border-radius:10px;
                    margin-bottom:10px;
                    ">

                    <span style="
                    font-family:'JetBrains Mono', monospace;
                    font-size:0.78em;
                    color:#94A3B8;
                    ">🧬 PMID&nbsp;{source.get('pmid')}</span>

                    <div style="margin-top:4px;color:#F8FAFC;font-weight:600;">
                    {source.get('title','N/A')}
                    </div>

                    <div style="margin-top:2px;color:#94A3B8;font-size:0.85em;">
                    {source.get('journal','N/A')}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.json(source)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    # =========================
    # Logo / Header
    # =========================

    st.markdown("""
<div style="
background:linear-gradient(135deg, rgba(6,182,212,0.12), rgba(139,92,246,0.12));
padding:22px 18px;
border-radius:18px;
border:1px solid #1e293b;
text-align:center;
">

<div style="font-size:2rem; line-height:1;">🛰️</div>

<h2 style="
margin:8px 0 0 0;
font-family:'Space Grotesk', sans-serif;
font-weight:700;
letter-spacing:-0.01em;
background:linear-gradient(135deg, #06B6D4, #8B5CF6);
-webkit-background-clip:text;
background-clip:text;
-webkit-text-fill-color:transparent;
">
DocIntel
</h2>

<p style="
color:#94A3B8;
margin-top:6px;
font-size:0.8rem;
letter-spacing:0.04em;
text-transform:uppercase;
">
AI Document Intelligence
</p>

</div>
""", unsafe_allow_html=True)

    # =========================
    # Mode Selection
    # =========================

    st.markdown("### 🧠 Knowledge Source")

    chat_mode = st.radio(
        "",
        [
            "📄 Document RAG",
            "🧬 PubMed Research"
        ]
    )

    st.divider()

    # =========================
    # Document Mode
    # =========================

    if "Document" in chat_mode:

        st.markdown("### 📤 Upload Document")

        uploaded_file = st.file_uploader(
            "Choose PDF",
            type=["pdf"]
        )

        if uploaded_file:

            st.markdown("### 📚 Selected Document")

            st.markdown(
                f"""
                <div style="
                background:#111827;
                border:1px solid #1e293b;
                padding:12px 14px;
                border-radius:12px;
                margin-bottom:10px;
                color:#F8FAFC;
                font-size:0.9rem;
                ">
                📄 {uploaded_file.name}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Auto Index
            if (
                st.session_state.active_document
                != uploaded_file.name
            ):

                with st.spinner(
                    "Indexing document..."
                ):

                    upload_document(
                        uploaded_file
                    )

                st.session_state.active_document = (
                    uploaded_file.name
                )

                st.session_state.messages = []

                st.success(
                    "Document indexed successfully"
                )

                st.rerun()

        # Active Document

        if st.session_state.active_document:

            st.markdown(
                "### 📄 Active Document"
            )

            st.markdown(
                f"""
                <div style="
                background:linear-gradient(135deg, rgba(16,185,129,0.10), rgba(16,185,129,0.02));
                border:1px solid rgba(16,185,129,0.35);
                padding:12px 14px;
                border-radius:12px;
                margin-bottom:10px;
                color:#F8FAFC;
                font-size:0.9rem;
                display:flex;
                align-items:center;
                gap:8px;
                ">
                <span style="
                width:8px; height:8px; border-radius:50%;
                background:#10B981;
                animation:pulse-dot 2s infinite;
                display:inline-block;
                "></span>
                {st.session_state.active_document}
                </div>
                """,
                unsafe_allow_html=True
            )

    # =========================
    # PubMed Mode
    # =========================

    else:

        st.markdown("""
        <div style="
        background:linear-gradient(135deg, rgba(139,92,246,0.12), rgba(139,92,246,0.02));
        border:1px solid rgba(139,92,246,0.35);
        padding:14px 16px;
        border-radius:14px;
        margin-bottom:10px;
        color:#F8FAFC;
        ">

        <div style="font-size:1.4rem;">🧬</div>

        <div style="
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        margin-top:6px;
        ">
        PubMed Research Mode
        </div>

        <div style="color:#94A3B8; font-size:0.85rem; margin-top:6px; line-height:1.5;">
        Searches indexed medical research papers.
        No document upload required.
        </div>

        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =========================
    # Features
    # =========================

    st.markdown("### 🎯 Capabilities")

    features = [
        ("📄", "Document RAG"),
        ("🧬", "PubMed RAG"),
        ("🔗", "Source Citation"),
        ("🔍", "Semantic Search"),
        ("🗂️", "Qdrant Vector DB"),
    ]

    features_html = "".join(
        f"""
        <div style="
        display:flex;
        align-items:center;
        gap:10px;
        padding:8px 12px;
        border-radius:10px;
        background:#0B1220;
        border:1px solid #1E293B;
        margin-bottom:6px;
        font-size:0.85rem;
        color:#F8FAFC;
        ">
        <span style="
        color:#10B981;
        font-family:'JetBrains Mono', monospace;
        ">✓</span>
        <span>{icon} {label}</span>
        </div>
        """
        for icon, label in features
    )

    st.markdown(features_html, unsafe_allow_html=True)

    st.divider()

    # =========================
    # System Status
    # =========================

    try:

        info = collection_info()

        st.markdown("""
        <div style="
        background:linear-gradient(135deg, rgba(16,185,129,0.16), rgba(16,185,129,0.04));
        border:1px solid rgba(16,185,129,0.4);
        padding:12px;
        border-radius:12px;
        color:#F8FAFC;
        text-align:center;
        margin-bottom:14px;
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.85rem;
        display:flex;
        align-items:center;
        justify-content:center;
        gap:8px;
        ">
        <span style="
        width:8px; height:8px; border-radius:50%;
        background:#10B981;
        animation:pulse-dot 2s infinite;
        display:inline-block;
        "></span>
        Backend Online
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📊 Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Chunks Indexed",
                info.get("points_count", 0)
            )

        with col2:
            st.metric(
                "Messages",
                len(
                    st.session_state.messages
                )
            )

    except Exception:

        st.markdown("""
        <div style="
        background:linear-gradient(135deg, rgba(239,68,68,0.16), rgba(239,68,68,0.04));
        border:1px solid rgba(239,68,68,0.4);
        padding:12px;
        border-radius:12px;
        color:#F8FAFC;
        text-align:center;
        margin-bottom:14px;
        font-family:'Space Grotesk', sans-serif;
        font-weight:600;
        font-size:0.85rem;
        display:flex;
        align-items:center;
        justify-content:center;
        gap:8px;
        ">
        <span style="
        width:8px; height:8px; border-radius:50%;
        background:#EF4444;
        display:inline-block;
        "></span>
        Backend Offline
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Screen
# --------------------------------------------------

if not st.session_state.messages:

    st.markdown("""
<div style="text-align:center; padding-top:90px;">

<div style="font-size:3.2rem; line-height:1;">🛰️</div>

<h1 style="
font-family:'Space Grotesk', sans-serif;
font-weight:700;
font-size:3rem;
letter-spacing:-0.02em;
margin:14px 0 4px 0;
background:linear-gradient(135deg, #06B6D4, #8B5CF6);
-webkit-background-clip:text;
background-clip:text;
-webkit-text-fill-color:transparent;
">
DocIntel
</h1>

<p style="
font-family:'Space Grotesk', sans-serif;
font-size:1.15rem;
color:#F8FAFC;
font-weight:500;
margin-bottom:28px;
">
AI-Powered Document Intelligence
</p>

<div style="
display:flex;
justify-content:center;
gap:14px;
flex-wrap:wrap;
margin-bottom:28px;
">

<div style="
background:#0B1220;
border:1px solid #1E293B;
border-radius:14px;
padding:16px 22px;
min-width:160px;
">
<div style="font-size:1.4rem;">💬</div>
<div style="font-family:'Space Grotesk', sans-serif; font-weight:600; color:#F8FAFC; margin-top:6px;">Ask Questions</div>
</div>

<div style="
background:#0B1220;
border:1px solid #1E293B;
border-radius:14px;
padding:16px 22px;
min-width:160px;
">
<div style="font-size:1.4rem;">📄</div>
<div style="font-family:'Space Grotesk', sans-serif; font-weight:600; color:#F8FAFC; margin-top:6px;">Analyze Documents</div>
</div>

<div style="
background:#0B1220;
border:1px solid #1E293B;
border-radius:14px;
padding:16px 22px;
min-width:160px;
">
<div style="font-size:1.4rem;">🧬</div>
<div style="font-family:'Space Grotesk', sans-serif; font-weight:600; color:#F8FAFC; margin-top:6px;">Search Medical Research</div>
</div>

</div>

<p style="
font-family:'JetBrains Mono', monospace;
font-size:0.8rem;
color:#64748b;
letter-spacing:0.08em;
text-transform:uppercase;
margin-bottom:6px;
">
Powered by RAG · Qdrant · PubMed
</p>

<p style="font-size:0.95rem; color:#94A3B8; max-width:480px; margin:0 auto;">
Upload documents, search medical literature, and get grounded answers with citations.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            render_sources(
                message["sources"]
            )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask your document anything..."
)

if question:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Assistant Placeholder
    assistant_placeholder = st.empty()

    import time

    stages = [
        "🔍 Searching relevant chunks...",
        "🧠 Re-ranking retrieved results...",
        "🤖 Generating grounded answer..."
    ]

    for stage in stages:

        assistant_placeholder.markdown(
            f"""
            <div style="
            background:linear-gradient(90deg, #0f172a 25%, #16223d 50%, #0f172a 75%);
            background-size:200% 100%;
            animation:shimmer 1.4s linear infinite;
            border:1px solid #1e293b;
            border-left:3px solid #06B6D4;
            padding:15px 18px;
            border-radius:14px;
            margin-bottom:10px;
            color:#F8FAFC;
            font-family:'Space Grotesk', sans-serif;
            font-size:0.92rem;
            ">
            {stage}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(1.0)

    try:

        if "Document" in chat_mode:

            result = chat_document(
                question
            )

        else:

            result = pubmed_chat(
                question
            )

        answer = result.get(
            "answer",
            "No answer found."
        )

        sources = result.get(
            "sources",
            []
        )

    except Exception as e:

        answer = f"Error: {e}"
        sources = []

    assistant_placeholder.empty()

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )

    with st.chat_message("assistant"):

        st.markdown(answer)

        render_sources(
            sources
        )

    st.rerun()