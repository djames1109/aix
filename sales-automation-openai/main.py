import asyncio

from agents import Agent, Runner, enable_verbose_stdout_logging

from agent.email_agent import get_email_sender_agent
from agent.sales_agent import get_sales_agents_as_tools
from guardrail.phone_number_guardrail import guardrail_against_phone_number
from llm.azure_llm import set_azure_as_default_llm

enable_verbose_stdout_logging()


async def main():
    """
    This script initializes an agent designated as a Sales Manager, designed to generate cold sales emails
    by leveraging multiple pre-defined tools. The tools offer different methods for email generation.
    The Sales Manager agent follows specific instructions to utilize all three tools at least once,
    chooses the best outcome, and hands off the chosen email to an Email Manager agent for formatting
    and sending. The execution process is managed asynchronously.

    :async run: The Sales Manager executes the email generation workflow based on the provided tools and
        hands over the finalized email to the designated Email Manager agent.

    :raises: Any exceptions encountered during asynchronous function execution or tool execution errors
        would propagate to the runner's execution flow.
    :return: None, as the script prints the result of the generated email to standard output.
    """

    sales_manager_instructions = "You are a sales manager working for AIX Lab. You use the tools given to you to generate cold sales emails. \
    You never generate sales emails yourself; you always use the tools. \
    You try all 3 sales agent tools at least once before choosing the best one. \
    You can use the tools multiple times if you're not satisfied with the results from the first try. \
    You select the single best email using your own judgement of which email will be most effective. \
    After picking the email, you handoff to the Email Manager agent to format and send the email."

    set_azure_as_default_llm()
    sales_manager = Agent(
        name="Sales Manager",
        instructions=sales_manager_instructions,
        tools=get_sales_agents_as_tools(),
        handoffs=[get_email_sender_agent()],
        input_guardrails=[guardrail_against_phone_number],
        model="gpt-4o-mini")

    # message = "Send a cold sales email addressed to 'ICaughtDBomber' from +63912-1214. " # This triggers the guardrail tripwire
    message = "Send a cold sales email addressed to 'ICaughtDBomber' from DJames "
    result = await Runner.run(sales_manager, message)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
