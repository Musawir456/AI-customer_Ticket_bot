import os
from config import logger
from dotenv import load_dotenv

 # loading api key 
load_dotenv()
OPENROUTER_api=os.getenv("OPENROUTER_API_KEY_1")
OPENROUTER_base_url=os.getenv("OPENROUTER_API_BASE")

if not OPENROUTER_api:
    raise RuntimeError("OPENROUTER_api is not found .env")

VECTORSTORE_DIR="vectorstore"
logger.info(f"Vectorstore directory set to :{VECTORSTORE_DIR}")
