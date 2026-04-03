"""
Example: AI-powered documentation generation.

Usage:
    AI_API_KEY=<your-key> python examples/doc_generation_example.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_dlc import AIClient, DocGenerator  # noqa: E402

SAMPLE_CODE = '''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
'''


def main():
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        print("Set the AI_API_KEY environment variable to run this example.")
        print("\nSample code that would be documented:")
        print(SAMPLE_CODE)
        return

    client = AIClient(api_key=api_key)
    generator = DocGenerator(client=client)

    print("Generating documentation for sample Python code with AI...\n")
    docs = generator.generate(SAMPLE_CODE, language="python")
    print("=== AI Generated Documentation ===")
    print(docs)


if __name__ == "__main__":
    main()
