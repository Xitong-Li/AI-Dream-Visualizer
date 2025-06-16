import time
import torch
import ollama
from ai_pipeline.text_utils import extract_keywords

class AI:
    def __init__(self, sd_pipeline):
        self.sd_pipeline = sd_pipeline

    def generate_dream_story(self, dream_text, emotion_category, progress_bar):
        """Generate a dream story using Ollama with progress UI"""
        prompt = f"Complete this dream description in a {emotion_category} style: {dream_text}"
        progress_bar.progress(20)
        time.sleep(0.5)

        try:
            response = ollama.chat(model="llava:7b", messages=[
                {"role": "user", "content": prompt}
            ])
            story = response["message"]["content"]
        except Exception as e:
            story = f"[Error generating story: {e}]"

        progress_bar.progress(100)
        return story

    def generate_dream_image(self, dream_text, emotion_category, progress_bar):
        """Generate an image using Stable Diffusion based on dream text"""
        keywords = extract_keywords(dream_text)
        if not keywords:
            return None

        prompt = f"{', '.join(keywords)}, {emotion_category}, surreal, dreamlike, high detail"
        progress_bar.progress(10)
        time.sleep(0.5)

        try:
            image = self.sd_pipeline(prompt).images[0]
        except Exception as e:
            print(f"Error during image generation: {e}")
            image = None

        progress_bar.progress(100)
        return image
