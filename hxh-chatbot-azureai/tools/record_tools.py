import json

from notif.pushover_notif import notify


def record_user_details(email, name="Name not provided", notes="Notes not provided"):
    notify(f"Recording interest from {name} <{email}> with notes: {notes}")
    return {
        "recorded": "ok"
    }


def record_unknown_question(question):
    notify(f"Recording unknown question: {question}")
    return {
        "recorded": "ok"
    }


def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool call received: {tool_name} with arguments: {arguments}")

        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else {}
        results.append({"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id})
    return results
