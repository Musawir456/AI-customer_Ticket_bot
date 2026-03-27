from langchain_openai import OpenAIEmbeddings
from Data_injestion import Document
from load_env import VECTORSTORE_DIR 
from langchain_community.vectorstores import Chroma
from config import logger
import os
import shutil
from dotenv import load_dotenv
load_dotenv()
Qwen_api_key=os.getenv("OPENROUTER_API_KEY")
Qwen_base_url=os.getenv("OPENROUTER_API_BASE")
def  get_vectorstore(documents=None):
    """
    Creates or  loads a persistent Chorma vector store.
    Uses cosine similarity internally.
    """
    embeddings=OpenAIEmbeddings(
        model="qwen/qwen3-embedding-8b",
         api_key=Qwen_api_key,
        base_url=Qwen_base_url

    )
     # If exists and no new docs → load
    if os.path.exists(VECTORSTORE_DIR) and documents is None:
        return Chroma(
            persist_directory=VECTORSTORE_DIR,
            embedding_function=embeddings
        )

    # If not exists → create
    if not os.path.exists(VECTORSTORE_DIR):
        vectordb = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=VECTORSTORE_DIR
        )
        vectordb.persist()
        return vectordb

    # If exists AND documents provided → DON'T delete automatically
    print("Vectorstore already exists. Delete manually if you want rebuild.")
    return Chroma(
        persist_directory=VECTORSTORE_DIR,
        embedding_function=embeddings
    )