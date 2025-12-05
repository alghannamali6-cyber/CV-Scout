# cv_agent.py
from utils import read_pdf, chunk_text
from config import CHUNK_SIZE, CHUNK_OVERLAP

class CVAgent:
    """
    Agent responsible for processing candidate CV PDFs
    into chunks for comparison.
    """
    def __init__(self, cv_file, chunk_size=None, overlap=None):
        self.cv_file = cv_file
        self.chunk_size = chunk_size or CHUNK_SIZE   # fallback
        self.overlap = overlap or CHUNK_OVERLAP     # fallback
        self.chunks = []

    def process(self):
        """
        Read the CV PDF, clean, and chunk it.
        """
        text = read_pdf(self.cv_file)
        self.chunks = chunk_text(text, chunk_size=self.chunk_size, overlap=self.overlap)
        return self.chunks
