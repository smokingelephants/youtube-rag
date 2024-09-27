import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# This is the YouTube video we're going to use.
YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=cdiD-9MMpb0"