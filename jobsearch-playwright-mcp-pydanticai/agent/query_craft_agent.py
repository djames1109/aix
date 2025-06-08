from PyPDF2 import PdfReader
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from llm.azure_llm import get_azure_llm
from model.search_prompt import JobSearchPrompt


def get_query_crafter_agent():
    """
    Creates and returns a reusable query_crafter_agent.
    """
    llm = get_azure_llm()
    instructions = """
        Use the tool to read the provided document. 
        Then, based on its content, create a browser search query that helps find the most suitable job based on the person's CV and location.
    """

    openai_model = OpenAIModel(model_name="gpt-4o-mini", provider=OpenAIProvider(openai_client=llm))
    query_crafter_agent = Agent(instructions=instructions, model=openai_model, result_type=JobSearchPrompt)

    @query_crafter_agent.tool
    async def read_cv(ctx: RunContext[int], file_path: str):
        print(f"Reading CV: {file_path}")
        reader = PdfReader(file_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        return content

    return query_crafter_agent
