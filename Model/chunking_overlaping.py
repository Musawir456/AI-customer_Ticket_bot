from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import logger
def chunk_documents(documents):
    """Breaks log  documents into overlapping chunks.
    This is CRITICAL for good semantic search. """
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )
    chunks=splitter.split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks from documents")
    return chunks