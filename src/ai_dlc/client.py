"""
AI Client - Core interface for interacting with AI APIs.
"""

import os
from typing import Optional


class AIClient:
    """
    A client for interacting with AI language model APIs.

    Supports OpenAI-compatible APIs. Configure via environment variables:
      - AI_API_KEY: Your API key
      - AI_MODEL: Model name (default: gpt-3.5-turbo)
      - AI_BASE_URL: API base URL (default: https://api.openai.com/v1)

    Supports OpenAI-compatible APIs only. Configure via environment variables.
    """

    DEFAULT_MODEL = "gpt-3.5-turbo"
    DEFAULT_BASE_URL = "https://api.openai.com/v1"

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        self.api_key = api_key or os.getenv("AI_API_KEY", "")
        self.model = model or os.getenv("AI_MODEL", self.DEFAULT_MODEL)
        self.base_url = base_url or os.getenv("AI_BASE_URL", self.DEFAULT_BASE_URL)

    def chat(self, prompt: str, system: Optional[str] = None) -> str:
        """
        Send a chat prompt to the AI model and return the response text.

        Args:
            prompt: The user message to send.
            system: Optional system instruction to guide the model's behavior.

        Returns:
            The model's response as a string.

        Raises:
            RuntimeError: If the API key is not configured.
            ImportError: If the `openai` package is not installed.
        """
        if not self.api_key:
            raise RuntimeError(
                "AI_API_KEY is not set. "
                "Set the AI_API_KEY environment variable or pass api_key to AIClient."
            )

        try:
            from openai import OpenAI  # type: ignore
        except ImportError as exc:
            raise ImportError(
                "openai package is required. Install it with: pip install openai"
            ) from exc

        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content or ""
