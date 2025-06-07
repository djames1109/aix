import os

from agents import set_default_openai_client, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

load_dotenv()


def set_azure_as_default_llm():
    llm = AsyncAzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )
    set_default_openai_client(llm)
    set_tracing_disabled(True)

    return llm
