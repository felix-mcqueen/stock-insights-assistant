from typing import Dict
import requests
import certifi


def fetch_single_stock_data(ticker: str) -> Dict[str, object]:
    ticker = ticker.upper()

    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {
        "interval": "1d",
        "range": "5d",
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
            verify=certifi.where(),
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()
        data = response.json()

        chart = data.get("chart", {})
        results = chart.get("result")

        if not results:
            return {
                "ticker": ticker,
                "company_name": ticker,
                "current_price": None,
                "previous_close": None,
                "change": None,
                "pct_change": None,
                "currency": "USD",
            }

        result = results[0]
        meta = result.get("meta", {})
        quote = result.get("indicators", {}).get("quote", [{}])[0]
        closes = quote.get("close", [])

        valid_closes = [c for c in closes if c is not None]

        current_price = meta.get("regularMarketPrice")
        if current_price is None and valid_closes:
            current_price = float(valid_closes[-1])

        previous_close = meta.get("previousClose")
        if previous_close is None and len(valid_closes) >= 2:
            previous_close = float(valid_closes[-2])

        change = None
        pct_change = None

        if current_price is not None and previous_close not in (None, 0):
            change = float(current_price) - float(previous_close)
            pct_change = (change / float(previous_close)) * 100

        return {
            "ticker": ticker,
            "company_name": meta.get("longName", ticker),
            "current_price": float(current_price) if current_price is not None else None,
            "previous_close": float(previous_close) if previous_close is not None else None,
            "change": change,
            "pct_change": pct_change,
            "currency": meta.get("currency", "USD"),
        }

    except Exception:
        return {
            "ticker": ticker,
            "company_name": ticker,
            "current_price": None,
            "previous_close": None,
            "change": None,
            "pct_change": None,
            "currency": "USD",
        }