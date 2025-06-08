import asyncio

from agent.browser_agent import get_browser_agent
from agent.query_craft_agent import get_query_crafter_agent


async def main():
    query_crafter_agent = get_query_crafter_agent()
    query_result = await query_crafter_agent.run(
        "Using this CV from 'resources/David_Castillo_Resume.pdf', create a query for a Java Developer job in Singapore.")
    print(query_result.output)

    browser_agent = get_browser_agent()
    async with browser_agent.run_mcp_servers():
        result = await browser_agent.run(
            f"Use google to find jobs using the following details: {query_result.output}")
    print(result.output)


asyncio.run(main())
