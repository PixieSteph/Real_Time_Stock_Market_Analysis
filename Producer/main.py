from extract import connect_to_api, extract_json


def main():
    response = connect_to_api()

    data = extract_json(response)

    for stock in data:
        result = {
            'date': stock['date'],
            'symbol': stock['symbol'],
            'open': stock['open'],
            'low': stock['low'],
            'high': stock['high'],
            'close': stock['close']
        }

        print(result)


if __name__ == '__main__':
    main()
       
               


