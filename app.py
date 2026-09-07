import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="YURIのマイノート帖",
    page_icon="🧡",
    layout="wide",
)

# Streamlit's own chrome (sidebar toggle, hamburger menu, "Made with Streamlit"
# footer, top padding) is hidden so only the note-taking tool itself is shown.
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container {padding: 0; max-width: 100%;}
    iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = pathlib.Path(__file__).parent.joinpath("template.html").read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
