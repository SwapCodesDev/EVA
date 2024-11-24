from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# API Keys
API = [
    os.getenv('GEN_API'),      # Gemini API
    os.getenv('NEWS_API')      # News API
    ]

# Intent Identifier
intent = {
    "BASIC_STATEMENT",
    "BASIC_QUESTION",
    "COMMAND",
    "SCREEN_BASED_QUERY_WHICH_REQUIRES_CONTENT_PRESENT_ON_SCREEN",
    "TAKE_SCREENSHOT",
    "TAKE_ACTIVE_WINDOW_SCREENSHOT",
    "DATE_AND_TIME_DETAILS"
    }
