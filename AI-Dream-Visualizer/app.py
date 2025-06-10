import streamlit as st
from ai_pipeline.ai import AI
from ai_pipeline.text_utils import get_emotion_category
from ai_pipeline.model_loader import load_sd_model

def main():
    st.title("🌙 AI Dream Visualization 🎭")

    # Load models
    sd_pipeline = load_sd_model()
    ai = AI(sd_pipeline)

    # User input
    st.write("✍ **Enter your dream description**")
    dream_text = st.text_area("Your Dream", "")

    # Adjust emotion
    st.write("🎭 **Adjust the dream's emotion** (X: Horror → Healing, Y: Peaceful → Intense)")
    x = st.slider("X axis (Horror → Healing)", 0.0, 1.0, 0.5)
    y = st.slider("Y axis (Peaceful → Intense)", 0.0, 1.0, 0.5)

    emotion_category = get_emotion_category(x, y)
    st.write(f"🧠 **Dream Analysis: {emotion_category} theme**")

    if st.button("🔮 Generate Dream Story & Image"):
        if dream_text:
            # Text generation
            text_progress = st.progress(0)
            st.status("⏳ AI is creating your dream story...")
            with st.spinner("📖 Generating Dream Story..."):
                dream_story = ai.generate_dream_story(dream_text, emotion_category, text_progress)
            st.write("📖 **AI Generated Dream Story**")
            st.write(dream_story)

            # Image generation
            img_progress = st.progress(0)
            st.status("🎨 AI is painting your dream image...")
            with st.spinner("🖼 Generating Dream Image..."):
                image = ai.generate_dream_image(dream_text, emotion_category, img_progress)
            if image:
                st.image(image, caption="🌌 AI Generated Dream Image")
        else:
            st.warning("Please enter a dream description!")

if __name__ == "__main__":
    main()
