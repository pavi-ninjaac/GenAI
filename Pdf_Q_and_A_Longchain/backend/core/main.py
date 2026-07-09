from core.long_chain import PdfQAChain


def generate_answer(question: str) -> str:
    """
    Generate answer for the user asked question.
    """
    pdf_qa_chain = PdfQAChain()
    # TODO: Implement a mechanism to check the chain's validity.
    # TODO: Add a timeout mechanism for the chain to avoid infinite loops.
    # TODO: Add logging and error handling.
    pdf_qa_chain.generate_chain()
    answer = pdf_qa_chain.rag_chain.invoke(question)
    return answer
