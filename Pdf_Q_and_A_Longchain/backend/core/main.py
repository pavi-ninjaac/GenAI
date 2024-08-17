from core.long_chain import PdfQAChain


def generate_answer(question: str) -> str:
    """
    Generate answer for the user asked question.
    """
    rag_chain = PdfQAChain().get_chain()
    answer = rag_chain.invoke(question)
    return answer
