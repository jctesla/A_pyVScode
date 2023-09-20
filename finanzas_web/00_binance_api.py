'''
Where can I find specific documentation for https://api.binance.com/api/v3 how to use it?  or    Binance API documentation

RESPTA:
Here's the link to the official Binance API documentation:
Binance API Documentation: https://binance-docs.github.io/apidocs/spot/en/

one of the tutoriasl : 
https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md
https://algotrading101.com/learn/auto-gpt-finance-guide/
https://www.google.com/search?q=simple+Binance+API+documentation+exercises&rlz=1C1GGGE_esPE1023PE1023&oq=simple+Binance+API+documentation+exercises&aqs=chrome..69i57j33i160.8192j0j15&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:34da3dd5,vid:ZiBBVYB5PuU

'''

import requests
def get_ticker_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': symbol}
    
    response = requests.get(url, params=params)
    data = response.json()

    if 'price' in data:
        return float(data['price'])
    else:
        return None

# Example usage
symbol = 'BTCUSDT'  # Replace with the symbol of the cryptocurrency you want to get the price for
price = get_ticker_price(symbol)
if price is not None:
    print(f'The current price of {symbol} is ${price:.2f}')
else:
    print(f'Error fetching price for {symbol}')
