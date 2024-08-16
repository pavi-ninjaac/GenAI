from typing import Final

DATA_FOLDER: Final[str] = "data/"
PROMPT_TEMPLATE: Final[str] = """Your name is noso, an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
 If you don't know the answer, just say that you don't know. Explain the answer in maximum 5 sentences. Answer like talking to a close friend.
 \nQuestion: {question} \nContext: {context} \nAnswer:"""
CHROMA_FOLDER: Final[str] = "chroma_db"


# File split related constants.
CHUNK_SIZE: Final[int] = 1000
CHUNK_OVERLAP: Final[int] = 400
ADD_START_INDEX: Final[bool] = True