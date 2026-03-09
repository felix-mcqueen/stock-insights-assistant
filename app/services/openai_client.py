import httpx
from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def create_response(
        self,
        *,
        model: str,
        input_text: str,
        system_prompt: str,
        temperature: float = 0.1,
    ) -> str:
        response = self.client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text},
            ],
            temperature=temperature,
        )

        return response.output_text