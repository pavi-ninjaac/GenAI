"""
Contains all the schemas.
"""

from fastapi import File, UploadFile
from pydantic import BaseModel


class UploadPdfRequest(BaseModel):
    """
    Schema for the upload PDF request.
    """
    file: UploadFile = File(...)


class QuestionRequest(BaseModel):
    """
    Schema for the question request.
    """
    question: str
