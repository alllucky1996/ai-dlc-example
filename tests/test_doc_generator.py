"""Tests for ai_dlc.doc_generator"""

import sys
import os
from unittest.mock import MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_dlc.doc_generator import DocGenerator  # noqa: E402
from ai_dlc.client import AIClient  # noqa: E402


class TestDocGenerator:
    def _make_generator(self, response: str = "Generated docs") -> DocGenerator:
        mock_client = MagicMock(spec=AIClient)
        mock_client.chat.return_value = response
        return DocGenerator(client=mock_client)

    def test_generate_returns_documentation(self):
        generator = self._make_generator("def foo():\n    \"\"\"Foo function.\"\"\"\n")
        docs = generator.generate("def foo(): pass")
        assert "foo" in docs

    def test_generate_passes_language_in_prompt(self):
        mock_client = MagicMock(spec=AIClient)
        mock_client.chat.return_value = "ok"
        generator = DocGenerator(client=mock_client)

        generator.generate("function greet() {}", language="javascript")

        call_args = mock_client.chat.call_args
        prompt = call_args[0][0]
        assert "javascript" in prompt.lower()

    def test_uses_default_client_when_none_provided(self, monkeypatch):
        monkeypatch.setenv("AI_API_KEY", "key")
        generator = DocGenerator()
        assert isinstance(generator.client, AIClient)
