"""Tests for ai_dlc.client"""

import pytest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_dlc.client import AIClient  # noqa: E402


class TestAIClientInit:
    def test_defaults_from_env(self, monkeypatch):
        monkeypatch.setenv("AI_API_KEY", "test-key")
        monkeypatch.setenv("AI_MODEL", "gpt-4")
        monkeypatch.setenv("AI_BASE_URL", "https://example.com/v1")

        client = AIClient()

        assert client.api_key == "test-key"
        assert client.model == "gpt-4"
        assert client.base_url == "https://example.com/v1"

    def test_explicit_values_override_env(self, monkeypatch):
        monkeypatch.setenv("AI_API_KEY", "env-key")

        client = AIClient(api_key="explicit-key", model="gpt-3.5-turbo")

        assert client.api_key == "explicit-key"
        assert client.model == "gpt-3.5-turbo"

    def test_default_model_when_env_not_set(self, monkeypatch):
        monkeypatch.delenv("AI_MODEL", raising=False)

        client = AIClient(api_key="key")

        assert client.model == AIClient.DEFAULT_MODEL

    def test_default_base_url_when_env_not_set(self, monkeypatch):
        monkeypatch.delenv("AI_BASE_URL", raising=False)

        client = AIClient(api_key="key")

        assert client.base_url == AIClient.DEFAULT_BASE_URL


class TestAIClientChat:
    def test_raises_without_api_key(self):
        client = AIClient(api_key="")

        with pytest.raises(RuntimeError, match="AI_API_KEY"):
            client.chat("hello")

    def test_chat_returns_response(self):
        client = AIClient(api_key="test-key")

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Hello!"

        mock_openai_class = MagicMock()
        mock_openai_class.return_value.chat.completions.create.return_value = mock_response

        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_class)}):
            result = client.chat("Say hello")

        assert result == "Hello!"

    def test_chat_includes_system_message(self):
        client = AIClient(api_key="test-key")

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "OK"

        mock_openai_instance = MagicMock()
        mock_openai_instance.chat.completions.create.return_value = mock_response
        mock_openai_class = MagicMock(return_value=mock_openai_instance)

        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_class)}):
            client.chat("prompt", system="You are a helpful assistant.")

        messages = mock_openai_instance.chat.completions.create.call_args[1]["messages"]
        assert messages[0] == {"role": "system", "content": "You are a helpful assistant."}
        assert messages[1] == {"role": "user", "content": "prompt"}
