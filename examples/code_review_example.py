"""
Example: AI-powered code review.

Usage:
    AI_API_KEY=<your-key> python examples/code_review_example.py
"""

import sys
import os

# Allow running from repo root without installing the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ai_dlc import AIClient, CodeReviewer  # noqa: E402

SAMPLE_CODE = '''
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)
    return avg
'''


def main():
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        print("Set the AI_API_KEY environment variable to run this example.")
        print("\nSample code that would be reviewed:")
        print(SAMPLE_CODE)
        return

    client = AIClient(api_key=api_key)
    reviewer = CodeReviewer(client=client)

    print("Reviewing sample Python code with AI...\n")
    feedback = reviewer.review(SAMPLE_CODE, language="python")
    print("=== AI Code Review Feedback ===")
    print(feedback)


if __name__ == "__main__":
    main()
