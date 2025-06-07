import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from llm.azure_llm import get_azure_llm
from mcpserver.playwright_mcp import get_playwright_mcp


async def main():
    instructions = """
    You browse the internet to accomplish your instructions.
    You are highly capable at browsing the internet independently to accomplish your task,
    including accepting all cookies and clicking 'not now' as
    appropriate to get to the content you need. If one website isn't fruitful, try another.
    Be persistent until you have solved your assignment,
    trying different options and sites as needed.
    """

    azure_llm = get_azure_llm()
    openai_model = OpenAIModel(model_name="gpt-4o-mini",
                               provider=OpenAIProvider(openai_client=azure_llm))
    agent = Agent(instructions=instructions, model=openai_model, mcp_servers=[get_playwright_mcp()])

    async with agent.run_mcp_servers():
        result = await agent.run("Find Java Developer jobs in Sweden. Return the links ")
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
