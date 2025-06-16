import streamlit as st
from ai_pipeline.sd import load_sd_model
from ai_pipeline.ai import AI
from ai_pipeline.text_utils import get_emotion_category

st.set_page_config(page_title="🌙 AI Dream Visualizer", layout="centered")
st.title("🌙 AI Dream Visualizer 🎭")

# Load SD pipeline and AI class
sd_pipeline = load_sd_model()
ai = AI(sd_pipeline)

# Input section
st.write("✍ **Enter your dream description**")
dream_text = st.text_area("Your Dream", "")

# Emotion sliders
st.write("🎭 **Adjust the dream's emotion**")
x = st.slider("X axis (Horror → Healing)", 0.0, 1.0, 0.5)
y = st.slider("Y axis (Peaceful → Intense)", 0.0, 1.0, 0.5)
emotion_category = get_emotion_category(x, y)
st.write(f"🧠 **Dream Analysis: `{emotion_category}` theme**")

# Action button
if st.button("🔮 Generate Dream Story & Image"):
    if not dream_text.strip():
        st.warning("Please enter a dream description!")
    else:
        # Generate story
        st.status("⏳ AI is creating your dream story...")
        text_progress = st.progress(0)
        with st.spinner("📖 Generating Dream Story..."):
            story = ai.generate_dream_story(dream_text, emotion_category, text_progress)
        st.markdown("#### 📖 Dream Story")
        st.write(story)

        # Generate image
        st.status("🎨 AI is painting your dream image...")
        img_progress = st.progress(0)
        with st.spinner("🖼 Generating Dream Image..."):
            image = ai.generate_dream_image(dream_text, emotion_category, img_progress)
        if image:
            st.image(image, caption="🌌 AI Generated Dream Image")