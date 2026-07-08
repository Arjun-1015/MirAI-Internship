import streamlit as st

st.title("Echo Chamber 9000")
st.write(
    "Welcome to the Identity Echo Interface. Please input your credentials "
    "and your payload below to securely transmit your data."
)

st.write("---")


user_name = st.text_input("Name", placeholder="Jane Doe")
user_message = st.text_input("Message", placeholder="You're caught!")

if st.button("Transmit"):

    if not user_name.strip():
        st.error("Please provide your name.")
        
    elif not user_message.strip():
        st.warning("Please type a message to transmit.")

    else:

        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )
        
        char_count = len(user_message)
        
        token_count = char_count / 4
        
        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count:.1f} tokens from our context window."
        )