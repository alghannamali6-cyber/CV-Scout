from utils import chunk_text
from config import CHUNK_SIZE, CHUNK_OVERLAP

class JDAgent:
    def __init__(self, jd_file=None, chunk_size=None, overlap=None):
        self.jd_file = jd_file
        self.chunk_size = chunk_size or CHUNK_SIZE
        self.overlap = overlap or CHUNK_OVERLAP
        self.chunks = []

    def process_from_text(self, text):
        """Chunk JD from pasted text"""
        self.chunks = chunk_text(
            text,
            chunk_size=self.chunk_size,
            overlap=self.overlap
        )
        return self.chunks
