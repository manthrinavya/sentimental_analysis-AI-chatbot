import streamlit as st
from chatbot import chatbot

st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Support Chatbot")
st.caption("Ask any course or customer support related question.")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your Nullclass Customer Support Assistant. Ask me anything!"
        }
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Type your question here..."):

    
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response
    answer, sentiment = chatbot(prompt)

    response = f"""
 **Sentiment:** **{sentiment}**

💬 **Answer:**

{answer}
"""

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
