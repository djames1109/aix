import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from llm.azure_llm import get_azure_llm


async def main():
    azure_llm = get_azure_llm()
    openai_model = OpenAIModel(model_name="gpt-4o-mini",
                               provider=OpenAIProvider(openai_client=azure_llm))
    agent = Agent(model=openai_model)
    result = await agent.run("Tell me a joke about tigers.")
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
