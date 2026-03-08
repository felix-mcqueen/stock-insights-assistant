from app.parser import parse_user_query
from app.models import IntentType


def test_parse_single_stock():
    result = parse_user_query("How is MSFT doing today?")
    assert result.intent == IntentType.SINGLE_STOCK
    assert "MSFT" in result.tickers
    assert result.timeframe == "today"