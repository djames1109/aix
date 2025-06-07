import asyncio

from agents import Agent, Runner
from dotenv import load_dotenv

from llm.azure_llm import set_azure_as_default_llm
from mcpserver.filesystem_mcp import get_filesystem_mcp
from mcpserver.playwright_mcp import get_playwright_mcp

load_dotenv()


async def main():
    filesystem_mcp = await get_filesystem_mcp()
    playwright_mcp = await get_playwright_mcp()

    # Ensure servers are connected before passing them to Agent
    await filesystem_mcp.connect()
    print("Connected to filesystem MCP")

    await playwright_mcp.connect()
    print("Connected to playwright MCP")

    instructions = """
    You browse the internet in headless mode to accomplish your instructions.
    You are highly capable at browsing the internet independently to accomplish your task,
    including accepting all cookies and clicking 'not now' as
    appropriate to get to the content you need. If one website isn't fruitful, try another.
    Be persistent until you have solved your assignment,
    trying different options and sites as needed.
    """

    set_azure_as_default_llm()
    agent = Agent(
        name="Investigator",
        instructions=instructions,
        model="gpt-4o-mini",
        mcp_servers=[filesystem_mcp, playwright_mcp]
    )

    result = await Runner.run(agent,
                              "Find a great recipe for Banoffee Pie, then summarize it in markdown to banofee-recipe.md")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
