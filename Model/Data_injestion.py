from config import logger
import pandas as pd
from langchain_core.documents import Document
def load_data(file_path="data/customer_support_ticket_cleaned.csv"):
    """
    Load CSV and converts row into Langchain Documents with metadata
    for filtering & tracking
    """
    logger.info("Loading dataset ....")

    # load
    df = pd.read_csv(file_path, encoding="latin1")

    documents=[]
    for idx , row in df.iterrows():
        text = (
            f"Ticket Type: {row['Ticket Type']}\n"
            f"Subject: {row['Ticket Subject']}\n"
            f"Description: {row['Ticket Description']}\n"
            f"Resolution: {row['Resolution']}\n"
            f"Priority: {row['Ticket Priority']}\n"
            f"Satisfaction: {row['Customer Satisfaction Rating']}"
        )
        documents.append(
            Document(
                page_content=text.strip(),
                metadata={
                    "row_id":idx,
                    "priority":row["Ticket Priority"],
                    "ticket_type":row["Ticket Type"]
                }
            )
        )
    logger.info(f"Loaded {len(documents)} raw documents")
    return documents