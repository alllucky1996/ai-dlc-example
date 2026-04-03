"""
AI DLC (AI-assisted Development Lifecycle) Example Package
"""

from .client import AIClient
from .code_reviewer import CodeReviewer
from .doc_generator import DocGenerator

__version__ = "0.1.0"
__all__ = ["AIClient", "CodeReviewer", "DocGenerator"]
