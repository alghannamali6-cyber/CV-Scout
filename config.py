# config.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------
# Load environment variables
# ---------------------------------------
load_dotenv()

# ---------------------------------------
# OpenAI / LLM Config
# ---------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.0))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1500))

# Initialize client (NEW API)
client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(prompt: str, model: str = LLM_MODEL, temperature: float = TEMPERATURE, max_tokens: int = MAX_TOKENS):
    """
    A unified helper to call the LLM using the NEW OpenAI API.
    Used across all agents.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a reliable NLP reasoning engine."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

# ---------------------------------------
# File / Storage Config
# ---------------------------------------
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads/")
CV_FOLDER = f"{UPLOAD_FOLDER}/cvs/"
JD_FOLDER = f"{UPLOAD_FOLDER}/jds/"

# ---------------------------------------
# Chunking / Parsing Config
# ---------------------------------------
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

# ---------------------------------------
# Scoring / Comparison Config
# ---------------------------------------
SCORE_SCALE = int(os.getenv("SCORE_SCALE", 100))

# Example: "skills,experience,education,fit"
SECTIONS = os.getenv("SECTIONS", "skills,experience,education,projects,Open Source").split(",")

# ---------------------------------------
# Streamlit Config
# ---------------------------------------
MAX_CVS_UPLOAD = int(os.getenv("MAX_CVS_UPLOAD", 100))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))
