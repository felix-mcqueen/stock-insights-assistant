import json
import os

from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def interpret_query(question: str) -> dict:
    prompt = f"""
You are parsing stock questions into JSON.

Return only valid JSON with this schema:
{{
  "intent": "single_stock" | "multi_stock" | "unknown",
  "tickers": ["..."],
  "timeframe": "today" | "week" | "month" | null
}}

Question: {question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    content = response.choices[0].message.content
    return json.loads(content)