from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class IntentType(str, Enum):
    SINGLE_STOCK = "single_stock"
    MULTI_STOCK = "multi_stock"
    SECTOR = "sector"
    UNKNOWN = "unknown"


@dataclass
class ParsedQuery:
    intent: IntentType
    tickers: List[str] = field(default_factory=list)
    company_names: List[str] = field(default_factory=list)
    sector: Optional[str] = None
    timeframe: Optional[str] = None