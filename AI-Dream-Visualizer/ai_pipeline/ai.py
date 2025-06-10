import ollama
import time
from ai_pipeline.text_utils import extract_keywords
from config import DEVICE, OLLAMA_MODEL

class AI:
    def __init__(self, sd_pipeline):
        self.sd_pipeline = sd_pipeline

    def generate_dream_story(self, dream_text, emotion_category, progress_bar):
        prompt = f"Complete this dream description in a {emotion_category} style: {dream_text}"
        progress_bar.progress(20)
        time.sleep(0.5)
        try:
            response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}])
            progress_bar.progress(100)
            return response["message"]["content"]
        except Exception as e:
            return f"Error generating story: {str(e)}"

    def generate_dream_image(self, dream_text, emotion_category, progress_bar):
        keywords = extract_keywords(dream_text)
        if not keywords:
            return None
        prompt = f"{', '.join(keywords)}, {emotion_category}, surreal, dreamlike, high detail"
        progress_bar.progress(10)
        time.sleep(0.5)
        try:
            image = self.sd_pipeline(prompt).images[0]
            progress_bar.progress(100)
            return image
        except Exception as e:
            return None
