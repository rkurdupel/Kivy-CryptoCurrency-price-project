import json
import requests



def Count(crypto, label):
    
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price"

    parameters = {
        "symbol": crypto
    }

    # requesting data from url
    if len(crypto) > 6:
        data = requests.get(url = key, params = parameters)
        data = data.json()
        print(f"{data['symbol']} price is {data['price']}")

        split_symbol = data['symbol'].split('USDT') # розділити слово на дві частини перед USDT та після USDT, результат в вигляді списку
        # SOLUSDT -> ['SOL', '']
        symbol = split_symbol[0]    # отримати першу частину з розділеного слова (SOL) 

        #data['symbol']

        return f"{symbol} {round(float(data['price']), 4)}$ USD/USDT"
   
