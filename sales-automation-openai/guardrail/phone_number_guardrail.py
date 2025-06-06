from agents import Agent, GuardrailFunctionOutput, Runner, input_guardrail
from pydantic import BaseModel


class PhoneNumberCheckOutput(BaseModel):
    does_phone_number_exists: bool
    phone_number: str


def get_phone_number_guardrail_agent():
    return Agent(
        name="Phone Number Guardrail Agent",
        instructions="Check if the user is including a phone number in their message",
        output_type=PhoneNumberCheckOutput,
        model="gpt-4o-mini"
    )

@input_guardrail
async def guardrail_against_phone_number(ctx, agent, message):
    result = await Runner.run(get_phone_number_guardrail_agent(), message, context=ctx.context)
    does_phone_number_exists = result.final_output.does_phone_number_exists
    return GuardrailFunctionOutput(output_info={"found_number": result.final_output},
                                   tripwire_triggered=does_phone_number_exists)
