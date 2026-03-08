import os
from dotenv import load_dotenv

load_dotenv(".env")


class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    finnhub_api_key: str = os.getenv("FINNHUB_API_KEY", "")
    app_name: str = "Stock Insights Assistant"
    

settings = Settings()

# Check if keys exist
if not settings.openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set")

if not settings.finnhub_api_key:
    raise ValueError("FINNHUB_API_KEY is not set")