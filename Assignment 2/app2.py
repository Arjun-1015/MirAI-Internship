import streamlit as st

st.title("WORLD OF CHATBOTS")

personality=st.selectbox("Who do you want to talk to?", ["Virat Kohli", "Ms Dhoni", "Donald Trump", "Dr. Modi", "CustomPersonality"])

personality_prompt=personality

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

user_msg=st.text_input("Say something")
if st.button("SEND"):
    if user_msg:
        ai_instructions= f"you are acting as {personality_prompt}, Respond to the message that is send byt user which is {user_msg}"
        with st.spinner("connecting to another world"):
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

            st.success("Message Received!")
            st.write(response.text)

    else:
        st.warning("Please type a message")