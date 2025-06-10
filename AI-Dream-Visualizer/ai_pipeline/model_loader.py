from diffusers import StableDiffusionPipeline
from config import MODEL_ID, DEVICE
import streamlit as st

@st.cache_resource
def load_sd_model():
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID).to(DEVICE)
    return pipe
