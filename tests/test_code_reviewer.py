"""Tests for ai_dlc.code_reviewer"""

import sys
import os
from unittest.mock import MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_dlc.code_reviewer import CodeReviewer  # noqa: E402
from ai_dlc.client import AIClient  # noqa: E402


class TestCodeReviewer:
    def _make_reviewer(self, response: str = "Looks good") -> CodeReviewer:
        mock_client = MagicMock(spec=AIClient)
        mock_client.chat.return_value = response
        return CodeReviewer(client=mock_client)

    def test_review_returns_feedback(self):
        reviewer = self._make_reviewer("1. Consider adding error handling.")
        feedback = reviewer.review("def foo(): pass")
        assert "error handling" in feedback

    def test_review_passes_language_in_prompt(self):
        mock_client = MagicMock(spec=AIClient)
        mock_client.chat.return_value = "ok"
        reviewer = CodeReviewer(client=mock_client)

        reviewer.review("console.log('hi')", language="javascript")

        call_args = mock_client.chat.call_args
        prompt = call_args[0][0]
        assert "javascript" in prompt.lower()

    def test_uses_default_client_when_none_provided(self, monkeypatch):
        monkeypatch.setenv("AI_API_KEY", "key")
        reviewer = CodeReviewer()
        assert isinstance(reviewer.client, AIClient)
