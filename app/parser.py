from __future__ import annotations

import re
from typing import List

from models import IntentType, ParsedQuery


COMMON_WORDS = {
    "HOW", "IS", "DOING", "TODAY", "WHAT", "THE", "A", "AN", "OF",
    "AND", "OR", "TO", "IN", "ON", "FOR", "WITH", "BY", "AT",
    "PERFORMING", "PERFORMANCE", "STOCK", "PRICE"
}


TICKER_PATTERN = r"\b[A-Z]{1,5}\b"


def extract_tickers(question: str) -> List[str]:
    candidates = re.findall(TICKER_PATTERN, question.upper())
    return [word for word in candidates if word not in COMMON_WORDS]


def extract_timeframe(question: str) -> str | None:
    q = question.lower()

    if "today" in q:
        return "today"
    if "this week" in q:
        return "week"
    if "this month" in q:
        return "month"

    return None


def parse_user_query(question: str) -> ParsedQuery:
    tickers = extract_tickers(question)
    timeframe = extract_timeframe(question)

    if len(tickers) == 1:
        intent = IntentType.SINGLE_STOCK
    elif len(tickers) > 1:
        intent = IntentType.MULTI_STOCK
    else:
        intent = IntentType.UNKNOWN

    return ParsedQuery(
        intent=intent,
        tickers=tickers,
        company_names=[],
        sector=None,
        timeframe=timeframe,
    )