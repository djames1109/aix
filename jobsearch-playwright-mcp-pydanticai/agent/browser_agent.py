from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from llm.azure_llm import get_azure_llm
from mcpserver.playwright_mcp import get_playwright_mcp
from model.job_listing import JobListing


def get_browser_agent() -> Agent:
    """
    Creates and returns an instance of a browser-enabled agent.
    """
    instructions = """
    You browse the internet to accomplish your instructions.
    You are highly capable at browsing the internet independently to accomplish your task,
    including accepting all cookies and clicking 'not now' as 
    appropriate to get to the content you need. If one website isn't fruitful, try another. 
    Be persistent until you have solved your assignment, trying different options and sites as needed.
    """
    azure_llm = get_azure_llm()
    openai_model = OpenAIModel(
        model_name="gpt-4o-mini",
        provider=OpenAIProvider(openai_client=azure_llm),
    )
    agent = Agent(
        instructions=instructions,
        model=openai_model,
        mcp_servers=[get_playwright_mcp()],
        output_type=JobListing
    )
    return agent
