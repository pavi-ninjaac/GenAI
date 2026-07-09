"""
Do the evironment variable setup for the API calls.
"""

import os

from core.open_ai_keys import GEMINI_LEARNING_API_KEY, LONGSMITH_LEARNING_API_KEY


def set_environmental_variable() -> None:
    """
    Set the environment variable.
    """
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = LONGSMITH_LEARNING_API_KEY

    # Setting up the API key for the gemini model.
    os.environ["GOOGLE_API_KEY"] = GEMINI_LEARNING_API_KEY
