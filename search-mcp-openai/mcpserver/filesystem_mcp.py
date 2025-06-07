import os

from agents.mcp import MCPServerStdio

sandbox_path = os.path.abspath(os.path.join(os.getcwd(), "sandbox"))
files_params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox_path]}


async def get_filesystem_mcp():
    return MCPServerStdio(params=files_params, client_session_timeout_seconds=60)
