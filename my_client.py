import asyncio
from fastmcp import Client

client = Client("https://mcp-server-298838101629.us-central1.run.app/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greetHola", {"name": name})
        print(result)

asyncio.run(call_tool("Kunal"))