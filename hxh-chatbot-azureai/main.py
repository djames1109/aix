import os

import gradio as gr
from PyPDF2 import PdfReader
from dotenv import load_dotenv

from llm.azure_llm import get_azure_llm
from tools.record_tools import handle_tool_calls
from tools.tools_definition import get_tools

load_dotenv()


def read_pdf():
    reader = PdfReader("resources/Hunter x Hunter.pdf")
    content = ""
    for page in reader.pages:
        content += page.extract_text()

    return content


def main(message, history):
    print("Hello from hxh-chatbot-azureai!")

    system_prompt = """
        You are roleplaying as Gon Freecs from Hunter x Hunter. 
        Your primary responsibility is to answer questions related to Hunter x Hunter in an engaging yet concise and informative manner, staying true to Gon's character.
        - Provide accurate and direct answers.
        - If you're unsure about a question, politely say you don’t know the answer and use the record_unknown_question tool to log it.
        - If the user engages in a conversation, guide them toward further contact by asking for their name and email. Use the record_user_details tool to save this information.
        
        Always stay in character, and make the interaction friendly, curious, and adventurous—just like Gon!
    """

    model = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    client = get_azure_llm()

    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    tools = get_tools()
    done = False
    response = None

    while not done:
        response = client.chat.completions.create(messages=messages, model=model, tools=tools)
        finish_reason = response.choices[0].finish_reason

        if finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            print(f"Tool calls: {tool_calls}")
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
        else:
            done = True

    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(main, type="messages").launch()
