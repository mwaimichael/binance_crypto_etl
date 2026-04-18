import requests
from pprint import pprint
import pandas as pd

def get_crypto_price(symbol, api_key):
    url = f"https://api.binance.com/api/v3/ticker/24hr"
    
    # The API key goes in the headers dictionary
    headers = {
        'X-MBX-APIKEY': api_key
    }
    
    response = requests.get(url, headers=headers)
    
    data = response.json()
    return data



# Usage
MY_API_KEY = "Y4XPiIHHu1ujSaDFF0uYAL6yJG8YPFLoQGsGIaWWUaIL9eOjaYU227YAlF4AwsyL"
btc_price = get_crypto_price("BTCUSDT", MY_API_KEY)
#pprint(f"Current BTC Price: {btc_price}")
print(len(btc_price))


prices = []

for each in btc_price:
    price = {
        "crypto": each.get("symbol"),
        "price": each.get("weightedAvgPrice")
    }
    prices.append(price)

#print(prices, sep="\n")

df = pd.DataFrame(prices)
df['price'] = df['price'].astype(float).round(2)
pd.set_option('display.float_format', '{:,.2f}'.format)
df = df[df['crypto'].isin(['BTCUSDT', 'WBTCUSDT', 'USDTIDR', 'USDTBIDR', 'USDTIDRT', 'XAUTUSDT', 'PAXGUSDT', 'USDTCOP', 'YFIUSDT', 'WBETHUSDT'])]
#df = df[df['crypto'].isin(['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'MKRUSDT', 'TAOUSDT', 'LTCUSDT', 'QNTUSDT', 'YFIBUSD', 'XAUTUSDT', 'BNBUSDT'])]
df.sort_values(by='price', ascending=False, inplace=True)

#df.info(verbose=False)
print("-"*20)

print(df.head(10))


