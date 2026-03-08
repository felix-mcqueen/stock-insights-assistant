from app.config import settings
from app.services.finnhub_client import FinnhubClient

client = FinnhubClient(api_key=settings.finnhub_api_key)

quote = client.get_quote("AAPL")
print(quote)

profile = client.get_company_profile("AAPL")
print(profile)