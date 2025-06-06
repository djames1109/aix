import asyncio

from agents import Agent, Runner

ai_model = "gpt-4o-mini"


def get_sales_agents_as_tools():
    description = "Write a cold sales email"
    professional_sa_tool = get_professional_sales_agent().as_tool(tool_name="professional_sales_agent",
                                                                  tool_description=description)
    engaging_sa_tool = get_engaging_sales_agent().as_tool(tool_name="engaging_sales_agent",
                                                          tool_description=description)
    busy_sa_tool = get_busy_sales_agent().as_tool(tool_name="busy_sales_agent",
                                                  tool_description=description)

    return [professional_sa_tool, engaging_sa_tool, busy_sa_tool]


async def get_sales_agents():
    message = "Write a cold sales email"
    return await asyncio.gather(
        Runner.run(get_professional_sales_agent(), message),
        Runner.run(get_engaging_sales_agent(), message),
        Runner.run(get_busy_sales_agent(), message),
    )


def get_professional_sales_agent():
    instructions = "You are a sales agent working for AIX Lab, \
    a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
    You write professional, serious cold emails."

    return Agent(name="Professional Sales Agent", instructions=instructions, model=ai_model)


def get_engaging_sales_agent():
    instructions = "You are a humorous, engaging sales agent working for ComplAI, \
    a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
    You write witty, engaging cold emails that are likely to get a response."

    return Agent(name="Engaging Sales Agent", instructions=instructions, model=ai_model)


def get_busy_sales_agent():
    instructions = "You are a busy sales agent working for ComplAI, \
    a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
    You write concise, to the point cold emails."

    return Agent(name="Busy Sales Agent", instructions=instructions, model=ai_model)
