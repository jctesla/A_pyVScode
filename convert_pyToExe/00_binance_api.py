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
