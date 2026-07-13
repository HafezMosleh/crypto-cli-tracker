import urllib.request, json

def get_prices():
    url = "https://api.binance.com/api/v3/ticker/price?symbols=[\"BTCUSDT\",\"ETHUSDT\",\"SOLUSDT\"]"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read())
        print("📈 Crypto CLI Tracker")
        for item in data:
            print(f"{item['symbol']}: ${float(item['price']):.2f}")
    except Exception as e:
        print("Error fetching prices:", e)

get_prices()
