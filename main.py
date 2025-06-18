import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio


print("[DEBUG] Starting MCP server setup...")
# define mcp server
mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m", "mcp_server_fetch"]
)
print("[DEBUG] MCP server created.")

# configure groq api key
os.environ["GROQ_API_KEY"] = "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"
print("[DEBUG] GROQ_API_KEY set.")

# create the AI agent 
agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    mcp_servers=[mcp_fetch_server]
)
print("[DEBUG] Agent created.")

# main async function
async def main():
    print("[DEBUG] Entered main async function.")
    async with agent.run_mcp_servers():
        print("[DEBUG] MCP servers running.")
        result = await agent.run("extract the content and summarize it :https://en.wikipedia.org/wiki/Artificial_intelligence ")
        print("[DEBUG] Agent run completed.")
        output = result.output
        return output

if __name__ == "__main__":
    print("[DEBUG] Running main function...")
    output = asyncio.run(main())
    print("[DEBUG] Output received:")
    print(output)
    
    
