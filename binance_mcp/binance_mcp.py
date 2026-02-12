from mcp.server.fastmcp import FastMCP, Context
import requests



mcp = FastMCP('Binance MCP')

def get_symbol_from_name(name):
    if name.lower() in ['bitcoin', 'btc']:
        return 'BTCUSDT'
    elif name.lower() in ['ethereum', 'eth']:
        return 'ETHUSDT'
    elif name.lower() in ['solana', 'sol']:
        return 'SOLUSDT'
    else:
        return name.upper()

@mcp.tool()
def get_price(symbol, ctx: Context):
    """
    Get the current price of a crypto asset from Binance

    Args:
        symbol(str): The symbol of the crypto asset to get the price

    Returns:
        Any: The current price of crypto asset
    
    :param symbol: Description
    """
    symbol = get_symbol_from_name(symbol)
    ctx.info(f'Getting price for {symbol}')
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    try:
        resp = requests.get(url)
        data = resp.json()
        return data
    except Exception as e:
        ctx.error(e)

    # return float(data['price'])


if __name__ == '__main__':
    print('Starting Binance MCP')
    mcp.run()
