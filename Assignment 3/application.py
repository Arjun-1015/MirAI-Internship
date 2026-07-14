import streamlit as st

st.title("WORLD OF CHATBOTS")
st.caption("Your chatbot is remembering the chats for this session!")

#personality=st.selectbox("Who do you want to talk to?", ["Virat Kohli", "Ms Dhoni", "Donald Trump", "Dr. Modi", "CustomPersonality"])
personality = st.sidebar.selectbox("Choose your multiverse personality...", ["Virat Kohli field rage mode", "An angry Ravi Shashtri", "Siddhu paaji in jolly mood", "CustomPersonality"])


personality_prompt=personality

intensity = st.sidebar.slider("Intensity", min_value=1, max_value=10, value=5)
if personality == "CustomPersonality":
    personality_prompt = st.text_area(
        "Describe the personality you want:",
        placeholder="Example: You are a friendly AI teacher who explains everything with examples and uses simple English."
    )


from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_msg := st.chat_input("Say something..."):

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_msg
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_msg)

    ai_instructions = f"""
    You are acting as {personality_prompt}
    with an intensity level of {intensity}.

    Reply to the following user message:

    {user_msg}
    """

    with st.spinner("Connecting to another world..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ai_instructions
        )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )