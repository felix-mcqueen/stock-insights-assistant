import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from app.config import settings
from app.services.openai_client import OpenAIClient
from app.services.query_parser import QueryParser

openai_client = OpenAIClient(api_key=settings.openai_api_key)
parser = QueryParser(openai_client=openai_client)

questions = [
    "How is AAPL doing today?",
    "Compare Tesla and Ford",
    "What are the top gainers in tech?",
    "What's the weather in London?",
]

for question in questions:
    print(f"\nQUESTION: {question}")
    parsed = parser.parse(question)
    print(parsed.model_dump())