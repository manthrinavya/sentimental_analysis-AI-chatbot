import streamlit as st
from chatbot import chatbot

st.set_page_config(page_title="Nullclass Chatbot", page_icon="🤖")

st.title("🤖 sentimental analyis Customer Support Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get chatbot response
    answer, sentiment = chatbot(prompt)

    bot_response = f"""**Sentiment:** {sentiment}

**Answer:**
{answer}
"""

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
