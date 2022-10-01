import json
import requests

# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price"


def Count(crypto):
    parameters = {
        "symbol": crypto
    }
    # requesting data from url
    if len(crypto) > 6:
        response = requests.get(url=key, params=parameters)
        data = response.json()
        # print(f"{data['symbol']} price is {data['price']}")

        split_symbol = data['symbol'].split(
            'USDT')  # розділити слово на дві частини перед USDT та після USDT, результат в вигляді списку
        # SOLUSDT -> ['SOL', '']
        symbol = split_symbol[0]  # отримати першу частину з розділеного слова (SOL)

        # data['symbol']

        return f"{symbol} {round(float(data['price']), 4)}$ USD/USDT"
    # else:
    # label.text = "Price:"

print(Count("SOLUSDT"))

def cryptoget(cryptoname, usd):
    parameters = {
        "symbol": cryptoname
    }

    if len(cryptoname) > 6:

        response = requests.get(url=key, params=parameters)
        data = response.json()
        print(data)

        crypto_price = float(data['price'])
        get_symbol = data["symbol"]
        # print(type(get_price))
        # print(get_price)

        # print(get_price)
        # print(type(get_price))
        count = round(usd / crypto_price, 4)    # округлити число, 4 - кількість знаків після коми

        return f"{count} {get_symbol}"


#print(cryptoget("BTCUSDT"))
