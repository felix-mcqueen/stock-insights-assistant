import json

from app.domain.models import IntentType, ParsedQuery
from app.services.openai_client import OpenAIClient


class QueryParserError(Exception):
    pass


QUERY_PARSER_SYSTEM_PROMPT = """
You are a financial query parser for a stock insights application.

Your job is to convert a user's natural language stock question into JSON.

Return only valid JSON.
Do not include markdown fences.
Do not explain anything.

Supported intents:
- single_stock
- compare_stocks
- top_movers_sector
- unsupported

Rules:
- If the user asks about one stock/company, use "single_stock".
- If the user asks to compare two or more stocks/companies, use "compare_stocks".
- If the user asks for top gainers, top movers, best performers in a sector, use "top_movers_sector".
- If the question is outside stock/company performance, use "unsupported".
- Extract ticker symbols when explicitly present.
- Extract company names when a company is mentioned without ticker.
- Default timeframe to "today" unless user clearly asks otherwise.
- Sector should be a lowercase string like "tech" if present.

Return JSON with exactly these keys:
{
  "intent": "single_stock|compare_stocks|top_movers_sector|unsupported",
  "tickers": [],
  "company_names": [],
  "sector": null,
  "timeframe": "today",
  "clarification_message": null
}

If unsupported, set a short clarification_message explaining what kind of questions are supported.
"""


class QueryParser:
    def __init__(self, openai_client: OpenAIClient, model: str = "gpt-4.1-mini") -> None:
        self.openai_client = openai_client
        self.model = model

    def parse(self, question: str) -> ParsedQuery:
        raw_output = self.openai_client.create_response(
            model=self.model,
            input_text=question,
            system_prompt=QUERY_PARSER_SYSTEM_PROMPT,
            temperature=0.0,
        )

        try:
            parsed_dict = json.loads(raw_output)
            return ParsedQuery(**parsed_dict)
        except (json.JSONDecodeError, ValueError) as exc:
            raise QueryParserError("Failed to parse user query.") from exc

    @staticmethod
    def fallback_unsupported() -> ParsedQuery:
        return ParsedQuery(
            intent=IntentType.UNSUPPORTED,
            clarification_message=(
                "I can help with stock questions like single-stock performance, "
                "company comparisons, and top movers by sector."
            ),
        )