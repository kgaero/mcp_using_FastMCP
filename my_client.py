import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greetHola", {"name": name})
        print(result)

asyncio.run(call_tool("Kunal"))