import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from llm.azure_llm import get_azure_llm
from mcpserver.filesystem_mcp import get_filesystem_mcp
from mcpserver.playwright_mcp import get_playwright_mcp


async def main():
    system_instructions = """
    You are a test automation engineer. Your goal is to execute a series of instructions 
    and generate a playwright test in python using browser_generate_playwright_test tool, then save into a python file.
    """

    azure_llm = get_azure_llm()
    openai_model = OpenAIModel(model_name="gpt-4o-mini",
                               provider=OpenAIProvider(openai_client=azure_llm))
    agent = Agent(instructions=system_instructions, model=openai_model, mcp_servers=[get_playwright_mcp(), get_filesystem_mcp()])

    async with agent.run_mcp_servers():
        result = await agent.run("""
        Generate a complete Python script using Playwright for this test scenario and save it to a file.

        Go to https://rahulshettyacademy.com/loginpagePractise/.
        Fill up Username as 'rahulshettyacademy' and Password as 'learning'
        Then click the Signin button.
        Verify that you can see the home page
        
        """)
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
