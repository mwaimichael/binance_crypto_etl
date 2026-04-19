import requests
from config import API_KEY
from pprint import pprint

url = f"https://api.binance.com/api/v3/ticker/24hr"

headers = {
    'X-MBX-APIKEY': API_KEY
}

def get_crypto_price():
    
    try:
        data = requests.get(url, headers=headers).json()
    except Exception as e:
        print(e)


    return data

