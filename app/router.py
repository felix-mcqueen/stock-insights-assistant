from __future__ import annotations

from app.data_fetcher import fetch_single_stock_data
from app.response_generator import format_single_stock_response


def handle_query(parsed_query) -> str:

    if parsed_query.intent.value == "single_stock":
        ticker = parsed_query.tickers[0]

        stock_data = fetch_single_stock_data(ticker)

        return format_single_stock_response(
            stock_data,
            parsed_query.timeframe
        )

    return "I can parse that question, but I don't support that intent yet."