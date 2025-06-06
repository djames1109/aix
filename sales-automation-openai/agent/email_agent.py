from agents import Agent

from tool.email import send_email


def get_email_sender_agent():
    email_agent_instructions = "You are an email formatter and sender. You receive the body of an email to be sent. \
    You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. \
    Finally, you use the send_html_email tool to send the email with the subject and HTML body."
    tools = [get_subject_writer_tool(), get_html_converter_tool(), send_email]

    return Agent(
        name="Email Manager",
        instructions=email_agent_instructions,
        tools=tools,
        model="gpt-4o-mini",
        handoff_description="Convert an email to HTML and send it")


def get_subject_writer_tool():
    instructions = "You can write a subject for a cold sales email. \
    You are given a message and you need to write a subject for an email that is likely to get a response."

    subject_writer = Agent(name="Email subject writer", instructions=instructions, model="gpt-4o-mini")
    return subject_writer.as_tool(tool_name="subject_writer",
                                  tool_description="Write a subject for a cold sales email")


def get_html_converter_tool():
    instructions = "You can convert a text email body to an HTML email body. \
    You are given a text email body which might have some markdown \
    and you need to convert it to an HTML email body with simple, clear, compelling layout and design."

    html_converter = Agent(name="HTML email body converter", instructions=instructions, model="gpt-4o-mini")
    return html_converter.as_tool(tool_name="html_converter",
                                  tool_description="Convert a text email body to an HTML email body")
