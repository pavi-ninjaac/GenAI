__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
sys.path.insert(0, "/home/pavithra/projects/GenAI/Pdf_Q_and_A_Longchain/backend/data/")

import core.constants as constants
from core.setup import set_environmental_variable
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


class PdfQAChain:
    """
    Class which represents the long chain code for the PdfQA.
    """

    def __init__(self) -> None:
        self.docs = None
        self.splits = None

    def _load_data(self):
        """
        Load the PDF files from the data folder.
        """
        # Read all the documents in the given folder.
        loader = PyPDFDirectoryLoader(constants.DATA_FOLDER)
        self.docs = loader.load()

    def _split_documents(self):
        """
        Split the PDF documents into chunks with overlapping characters.
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=constants.CHUNK_SIZE,
                                                       chunk_overlap=constants.CHUNK_OVERLAP,
                                                       add_start_index=constants.ADD_START_INDEX)
        self.splits: list = text_splitter.split_documents(self.docs)

    def _store_data(self):
        """
        Embed the document chinks and store in a Vector database.
        """
        vectorstore = Chroma.from_documents(collection_name="user_document",
                                            documents=self.splits,
                                            embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
                                            )
        return vectorstore

    def _get_llm_model(self):
        """
        Initialize the LLM model API.
        """
        set_environmental_variable()
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        return llm

    def _format_docs(self, docs) -> str:
        """
        Format the documents given.
        """
        return "\n\n".join(doc.page_content for doc in docs)

    def get_chain(self):
        """
        The RAG long chain.
        """
        # 1 | Prepare the data documents.
        self._load_data()
        self._split_documents()

        # 2 | Generate the promt.
        prompt = ChatPromptTemplate([
            ("system", "Your name is noso. You are an assistant for question-answering task from the user uploaded document"),
            ("human", constants.PROMPT_TEMPLATE)
        ])

        # 3 | Get the retriver.
        retriever = self._store_data().as_retriever()

        llm = self._get_llm_model()

        # Make the long chain to give the prompt to the retriver -> get the answer from the retriver -> give it to llm -> get the output.
        rag_chain = (
            {"context": retriever | self._format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        return rag_chain
