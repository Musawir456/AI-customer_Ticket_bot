from fastapi import FastAPI
from pydantic import BaseModel
from embeding_vectorstore import get_vectorstore
from Retrieval_metadata import get_qa_chain
from Data_injestion import load_data
from chunking_overlaping import chunk_documents
app= FastAPI()

raw_docs=load_data("data/customer_support_ticket_cleaned.csv")
chunk_doc=chunk_documents(raw_docs)
vectordb=get_vectorstore(chunk_doc)
qa=get_qa_chain(vectordb)

class Query(BaseModel):
    question:str

@app.post("/ask")
def ask_question(q:Query):
    response=qa.invoke({"query":q.question})
    #Return string if response dict
    if isinstance(response,dict):
        return{"answer":response.get("result",response)}
    return{"answer":response}