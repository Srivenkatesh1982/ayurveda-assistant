"""
Streamlit Chat UI for AyurVeda Home Remedies Assistant
Run: streamlit run streamlit_app.py
"""

import streamlit as st
from app import ask_ayurveda

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="AyurVeda Assistant",
    page_icon="🌿",
    layout="centered",
)

# ── Title & Description ───────────────────────────────────────
st.title("🌿 AyurVeda Home Remedies Assistant")
st.markdown(
    """
    *Based on "The Complete Book of Ayurvedic Home Remedies" by Vasant Lad*

    Ask about Ayurvedic remedies, dosha balancing, herbs, and diet tips.
    > ⚠️ **This assistant is for educational purposes only. Not a substitute for medical advice.**
    """
)

# ── Sidebar: Temperature Control ──────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    temperature = st.slider(
        "Response Creativity (Temperature)",
        min_value=0.0, max_value=1.0, value=0.4, step=0.1,
        help="Lower = more precise, Higher = more creative"
    )
    st.markdown("---")
    st.markdown("**Domain:** Ayurvedic Home Remedies")
    st.markdown("**Model:** mistral-7b-instruct via OpenRouter")
    st.markdown("---")
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        st.rerun()

# ── Session State for Chat History ────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Display Chat History ───────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── User Input ─────────────────────────────────────────────────
if prompt := st.chat_input("Ask about an Ayurvedic remedy, dosha, or herb..."):
    # Store & display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get LLM response
    with st.chat_message("assistant"):
        with st.spinner("🌿 Consulting Ayurvedic wisdom..."):
            response = ask_ayurveda(prompt, temperature=temperature)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
