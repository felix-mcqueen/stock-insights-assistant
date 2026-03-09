from __future__ import annotations

import requests

from app.domain.models import CompanyProfile, QuoteData, StockSnapshot


class FinnhubClientError(Exception):
    pass


class FinnhubClient:
    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self, api_key: str, timeout: int = 10) -> None:
        self.api_key = api_key
        self.timeout = timeout

    def _get(self, path: str, params: dict[str, str]) -> dict:
        request_params = {**params, "token": self.api_key}
        response = requests.get(
            f"{self.BASE_URL}{path}",
            params=request_params,
            timeout=self.timeout,
            verify=False
        )

        if response.status_code == 429:
            raise FinnhubClientError("Finnhub rate limit exceeded.")

        if not response.ok:
            raise FinnhubClientError(
                f"Finnhub request failed with status {response.status_code}."
            )

        return response.json()

    def get_quote(self, symbol: str) -> QuoteData:
        data = self._get("/quote", {"symbol": symbol.upper()})

        if not data or data.get("c") in (None, 0):
            raise FinnhubClientError(f"No quote data found for symbol '{symbol}'.")

        return QuoteData(
            symbol=symbol.upper(),
            current_price=float(data["c"]),
            change=float(data["d"]),
            percent_change=float(data["dp"]),
            high=float(data["h"]),
            low=float(data["l"]),
            open_price=float(data["o"]),
            previous_close=float(data["pc"]),
        )

    def get_company_profile(self, symbol: str) -> CompanyProfile:
        data = self._get("/stock/profile2", {"symbol": symbol.upper()})

        if not data or not data.get("ticker"):
            raise FinnhubClientError(f"No company profile found for symbol '{symbol}'.")

        return CompanyProfile(
            symbol=data["ticker"],
            name=data.get("name", data["ticker"]),
            finnhub_industry=data.get("finnhubIndustry"),
            market_capitalization=data.get("marketCapitalization"),
            currency=data.get("currency"),
        )

    def get_stock_snapshot(self, symbol: str) -> StockSnapshot:
        quote = self.get_quote(symbol)
        profile = self.get_company_profile(symbol)
        return StockSnapshot(quote=quote, profile=profile)

    def search_symbol(self, query: str) -> list[dict]:
        data = self._get("/search", {"q": query})

        results = data.get("result", [])
        return [
            item
            for item in results
            if item.get("symbol") and item.get("type") == "Common Stock"
        ]