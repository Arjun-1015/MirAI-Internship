#14/07/2026

import streamlit as st
import requests
import random

st.title("The AI Image Studio")
st.caption("Your thinking our recreation")

mp = st.text_input("Describe your masterpiece")

st.sidebar.title("Generation Settings")
artstyle = st.sidebar.selectbox("Select Art Style", ["Pixelated", "Oil Paint", "ColourPenSketch", "Pencil Sketch"])
width = st.sidebar.slider("Image Width", min_value=512, max_value=3000, value=700, step=5)
height = st.sidebar.slider("Image Height", min_value=512, max_value=3000, value=700, step=5)

# Task 3: Magic Enhance toggle
magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")

# Task 4: Surprise Me prompt list
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon made entirely of stained glass",
    "A tiny robot gardening on the moon",
    "A steampunk octopus playing violin underwater"
]


def generate_image(prompt_text, artstyle, width, height, magic_enhance):
    """Builds the prompt, calls the API, and renders/downloads the result."""
    full_prompt = f"{prompt_text}, make the art as the prescribed artstyle that is the {artstyle} style"

    # Task 3: append magic enhance boost words if enabled
    if magic_enhance:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    # Task 1: append width and height as URL parameters
    url = f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"

    with st.spinner("Generating your masterpiece..."):
        response = requests.get(url)

        if response.status_code == 200:
            st.success("Image Generated")
            st.image(response.content, caption=full_prompt)

            # Task 2: dynamic, correct file extension
            st.download_button(
                label="Download",
                data=response.content,
                file_name=f"{artstyle}_image.png",
                mime="image/png"
            )
        else:
            st.error("API is not working")


col1, col2 = st.columns(2)

with col1:
    generate_clicked = st.button("Generate")

with col2:
    surprise_clicked = st.sidebar.button("🎲 Surprise Me!")

if generate_clicked:
    if mp:
        generate_image(mp, artstyle, width, height, magic_enhance)
    else:
        st.warning("Please add an image description")

if surprise_clicked:
    random_prompt = random.choice(surprise_prompts)
    st.info(f"Surprise prompt: {random_prompt}")
    generate_image(random_prompt, artstyle, width, height, magic_enhance)
