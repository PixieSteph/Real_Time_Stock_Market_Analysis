import time
import requests
from config import logger, headers, url


def connect_to_api():
    stocks = ["TSLA", "MSFT", "GOOGL"]

    json_response = []

    for stock in range(0, len(stocks)):

        querystring = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": f"{stocks[stock]}",
            "outputsize": "compact",
            "interval": "5min",
            "datatype": "json",
            "apikey": "API_KEY"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()

            data = response.json()
            json_response.append(data)

            logger.info(f"{stocks[stock]} successfully loaded")

            time.sleep(1)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error on stock {stocks}: {e}")

    return json_response


def extract_json(response):
    records = []

    for data in response:

        if "Meta Data" not in data or "Time Series (5min)" not in data:
            print("API did not return valid stock data:")
            print(data)
            continue

        symbol = data["Meta Data"]["2. Symbol"]

        for date_str, metrics in data["Time Series (5min)"].items():
            record = {
                "symbol": symbol,
                "date": date_str,
                "open": metrics["1. open"],
                "low": metrics["3. low"],
                "high": metrics["2. high"],
                "close": metrics["4. close"]
            }

            records.append(record)

    return records