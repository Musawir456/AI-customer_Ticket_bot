from langchain_openai import ChatOpenAI
from load_env import OPENROUTER_api
from load_env import OPENROUTER_base_url
def get_llm():
    """Loads LLM Securely."""
    return ChatOpenAI(
       model="openai/gpt-oss-120b:free",
       api_key=OPENROUTER_api,
       base_url=OPENROUTER_base_url,
       temperature=0,
       max_tokens=500

    )
