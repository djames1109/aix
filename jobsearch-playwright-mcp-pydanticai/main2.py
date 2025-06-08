import asyncio

from agent.query_craft_agent import get_query_crafter_agent


async def main():
    query_crafter_agent = get_query_crafter_agent()
    query_result = await query_crafter_agent.run("Using this CV from 'resources/David_Castillo_Resume.pdf', create a query for a Java Developer job in Singapore.")
    print(query_result.output)

    


asyncio.run(main())
