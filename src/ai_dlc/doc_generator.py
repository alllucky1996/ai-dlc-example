"""
Doc Generator - AI-powered documentation generator.
"""

from .client import AIClient

SYSTEM_PROMPT = (
    "You are a technical writer who creates clear, concise documentation. "
    "Generate docstrings and documentation in the style appropriate for the language. "
    "Include parameter descriptions, return values, and a short usage example."
)


class DocGenerator:
    """
    Uses an AI model to generate documentation for functions and classes.

    Example::

        generator = DocGenerator()
        docs = generator.generate(code, language="python")
        print(docs)
    """

    def __init__(self, client: AIClient | None = None):
        self.client = client or AIClient()

    def generate(self, code: str, language: str = "python") -> str:
        """
        Generate documentation for the given source code.

        Args:
            code: The source code to document.
            language: Programming language of the code.

        Returns:
            A string containing the generated documentation.
        """
        prompt = (
            f"Generate documentation for the following {language} code. "
            f"Include docstrings for all public functions and classes:\n\n"
            f"```{language}\n{code}\n```"
        )
        return self.client.chat(prompt, system=SYSTEM_PROMPT)
