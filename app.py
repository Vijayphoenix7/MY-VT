import streamlit as st
import openai

# OpenAI API Key Configuration
openai.api_key = "your_openai_api_key"

# Streamlit Page Configuration
st.set_page_config(page_title="GPT Chat Interface", layout="centered")

# App Title
st.title("GPT Chat Interface")

# Chat History Management
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# User Input
with st.form("chat_form"):
    user_input = st.text_area("Your message:", key="user_input", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

# Handle User Input and Response
if submit_button and user_input:
    # Append user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Query OpenAI GPT
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or gpt-4, if you have access
            messages=st.session_state.messages
        )
        reply = response["choices"][0]["message"]["content"]

        # Append GPT reply to chat history
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        reply = f"Error: {str(e)}"

    st.text_area("GPT's response:", value=reply, height=200, disabled=True)

# Display Chat History
st.subheader("Chat History")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**GPT:** {message['content']}")
