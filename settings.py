# settings.py
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os

load_dotenv()

PORT = os.getenv("PORT")
URL = os.getenv("URL")