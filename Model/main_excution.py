from Data_injestion import load_data
from config import logger
from chunking_overlaping import chunk_documents
from embeding_vectorstore import get_vectorstore
from Retrieval_metadata import get_qa_chain

if __name__ == "__main__":

    try:
        logger.info("Loading dataset...")
        raw_docs = load_data("data/customer_support_ticket_cleaned.csv")
        logger.info(f"Loaded {len(raw_docs)} documents")

        chunked_docs = chunk_documents(raw_docs)
        logger.info(f"Created {len(chunked_docs)} chunks")

        vectordb = get_vectorstore(chunked_docs)

        # Build QA chain (NO metadata filter for now)
        qa = get_qa_chain(vectordb)

        query = "Why are customers unhappy with high priority tickets?"
        logger.info(f"User Question: {query}")

        print("\nRunning QA...\n")

        response = qa.invoke({"query": query})

        print("\n========== RESPONSE ==========\n")

        # Handle different response types safely
        if isinstance(response, dict):
            print(response.get("result", response))
        else:
            print(response)

    except Exception as e:
        print("\nERROR OCCURRED:")
        print(str(e))
        print(response)
