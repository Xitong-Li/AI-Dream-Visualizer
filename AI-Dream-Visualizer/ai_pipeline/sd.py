import torch
from diffusers import StableDiffusionPipeline
from config import MODEL_ID
import streamlit as st

@st.cache_resource
def load_sd_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID).to(device)
    return pipe
