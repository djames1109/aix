import os

from pydantic_ai.mcp import MCPServerStdio


def get_filesystem_mcp():
    generated_tests_path = os.path.abspath(os.path.join(os.getcwd(), "generated_tests"))
    return MCPServerStdio(command="npx", args=["-y", "@modelcontextprotocol/server-filesystem", generated_tests_path])
