from agents.mcp import MCPServerStdio

playwright_params = {"command": "npx", "args": ["@playwright/mcp@latest", "--headless"]}


async def get_playwright_mcp():
    return MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60)
