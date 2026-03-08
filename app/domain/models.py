from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class IntentType(str, Enum):
    SINGLE_STOCK = "single_stock"
    COMPARE_STOCKS = "compare_stocks"
    TOP_MOVERS_SECTOR = "top_movers_sector"
    UNSUPPORTED = "unsupported"


class AskRequest(BaseModel):
    question: str = Field(min_length=1)


class AskResponse(BaseModel):
    answer: str
    intent: IntentType


class ParsedQuery(BaseModel):
    intent: IntentType
    tickers: list[str] = Field(default_factory=list)
    company_names: list[str] = Field(default_factory=list)
    sector: str | None = None
    timeframe: str = "today"


class QuoteData(BaseModel):
    symbol: str
    current_price: float
    change: float
    percent_change: float
    high: float
    low: float
    open_price: float
    previous_close: float


class CompanyProfile(BaseModel):
    symbol: str
    name: str
    finnhub_industry: str | None = None
    market_capitalization: float | None = None
    currency: str | None = None


class StockSnapshot(BaseModel):
    quote: QuoteData
    profile: CompanyProfile


class AssistantResult(BaseModel):
    answer: str
    intent: IntentType
    raw_data: dict[str, Any] | None = None