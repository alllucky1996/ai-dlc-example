"""
Code Reviewer - AI-powered code review helper.
"""

from .client import AIClient

SYSTEM_PROMPT = (
    "You are an expert software engineer performing a code review. "
    "Identify bugs, security issues, performance problems, and style improvements. "
    "Be concise and specific. Format your feedback as a numbered list."
)


class CodeReviewer:
    """
    Uses an AI model to review source code and provide feedback.

    Example::

        reviewer = CodeReviewer()
        feedback = reviewer.review(code, language="python")
        print(feedback)
    """

    def __init__(self, client: AIClient | None = None):
        self.client = client or AIClient()

    def review(self, code: str, language: str = "python") -> str:
        """
        Review the given source code and return AI-generated feedback.

        Args:
            code: The source code to review.
            language: Programming language of the code (used for context).

        Returns:
            A string containing the review feedback.
        """
        prompt = (
            f"Please review the following {language} code and provide feedback:\n\n"
            f"```{language}\n{code}\n```"
        )
        return self.client.chat(prompt, system=SYSTEM_PROMPT)
