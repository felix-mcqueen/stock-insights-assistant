from typing import Any, Dict


def format_single_stock_response(stock_data: Dict[str, Any], timeframe: str | None = None) -> str:
    ticker = stock_data["ticker"]
    company_name = stock_data["company_name"]
    price = stock_data["current_price"]
    change = stock_data["change"]
    pct_change = stock_data["pct_change"]
    currency = stock_data["currency"]

    if price is None:
        return f"I couldn't retrieve live price data for {ticker}."

    if change is None or pct_change is None:
        return f"{company_name} ({ticker}) is trading at {price:.2f} {currency}."

    direction = "up" if change >= 0 else "down"
    time_phrase = "today" if timeframe == "today" else "right now"

    return (
        f"{company_name} ({ticker}) is trading at {price:.2f} {currency} {time_phrase}, "
        f"{direction} {abs(change):.2f} ({abs(pct_change):.2f}%)."
    )