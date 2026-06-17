import os

import streamlit as st

import validators

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from utils.youtube_loader import (
    extract_video_id,
    get_transcript
)

from utils.website_loader import (
    get_website_text
)

from utils.rag import (
    create_retriever
)

from utils.helpers import (
    run_chain
)

from utils.prompts import *


load_dotenv()

import os

groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠"
)

st.title("🧠 AI Research Assistant")


url = st.text_input(
    "Enter YouTube or Website URL"
)

if st.button("Analyze"):
    
    if not groq_api_key:
       st.error("GROQ_API_KEY not found...")
       st.stop()

    if not validators.url(url):
        st.error("Invalid URL")
        st.stop()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=groq_api_key,
        temperature=0.3
    )

    with st.spinner("Loading Content..."):

        if (
            "youtube.com" in url
            or
            "youtu.be" in url
        ):

            video_id = extract_video_id(url)

            text = get_transcript(
                video_id
            )

        else:

            text = get_website_text(
                url
            )

        text = text[:15000]

        retriever = create_retriever(
            text
        )

        st.session_state["text"] = text
        st.session_state["retriever"] = retriever
        st.session_state["llm"] = llm

        summary = run_chain(
            llm,
            SUMMARY_PROMPT,
            text
        )

        st.session_state["summary"] = summary

if "summary" in st.session_state:

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📄 Summary",
            "❓ Questions",
            "📝 Notes",
            "🎯 Flashcards",
            "💬 Chat"
        ]
    )

    with tab1:
        st.write(
            st.session_state["summary"]
        )

    with tab2:

        if st.button("Generate Questions"):

            st.write(
                run_chain(
                    st.session_state["llm"],
                    QUESTIONS_PROMPT,
                    st.session_state["text"]
                )
            )

    with tab3:

        if st.button("Generate Notes"):

            st.write(
                run_chain(
                    st.session_state["llm"],
                    NOTES_PROMPT,
                    st.session_state["text"]
                )
            )

    with tab4:

        if st.button("Generate Flashcards"):

            st.write(
                run_chain(
                    st.session_state["llm"],
                    FLASHCARD_PROMPT,
                    st.session_state["text"]
                )
            )

    with tab5:

        question = st.text_input(
            "Ask a question"
        )

        if question:

            docs = (
                st.session_state[
                    "retriever"
                ].invoke(question)
            )

            context = "\n\n".join(
                d.page_content
                for d in docs
            )

            answer = (
                st.session_state["llm"]
                .invoke(
                    RAG_PROMPT.format(
                        context=context,
                        question=question
                    )
                )
            )

            st.write(
                answer.content
            )