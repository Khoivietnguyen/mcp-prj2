import asyncio
from pathlib import Path
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


ROOT_FOLDER = Path(__file__).parent.absolute()
MCP_PATH  = ROOT_FOLDER / "binance_mcp_ref_impl" / "binance_mcp.py"
mcp_config = {
    "binance": {
        "command": "uv",
        "args": [
        "--directory",
        "C:\\Users\\ENGUYEKHF\\projects\\mcp-prj2\\binance_mcp",
        "run",
        "binance_mcp.py"
        ],
        "transport": "stdio",
    }   
}

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


async def get_crypto_prices():
    client = MultiServerMCPClient(mcp_config)
    async with client.session("binance") as session:
        tools = await client.get_tools()
        agent = create_agent(model, tools)
        query = "What are the current prices of Bitcoin and Ethereum?"
        message = HumanMessage(content=query)
        response = await agent.ainvoke({"messages": [message]})
        answer = response["messages"][-1].content
        return answer
    

if __name__ == "__main__":
    # Run the main async function
    response = asyncio.run(get_crypto_prices())
    print(response)
