from pydantic_ai.mcp import MCPServerStdio


def get_playwright_mcp():
    return MCPServerStdio(command="npx", args=["@playwright/mcp@latest"], timeout=60)
