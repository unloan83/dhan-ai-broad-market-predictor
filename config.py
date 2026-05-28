import os
from dotenv import load_dotenv
load_dotenv()

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Filters
MIN_PRICE = 200
MAX_PRICE = 750
MAX_CANDIDATES = 60      # Reduced for speed & reliability
TOP_PREDICTIONS = 10
