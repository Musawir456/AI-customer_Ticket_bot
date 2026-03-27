from embeding_vectorstore import get_vectorstore
from langchain.chains import RetrievalQA
from llm_setup import get_llm

def get_qa_chain(vectordb):
    """
    Simple stable RAG chain (no metadata filtering)
    """

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False
    )

    return qa_chain
