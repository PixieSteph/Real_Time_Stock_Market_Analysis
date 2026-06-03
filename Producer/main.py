from extract import connect_to_api, extract_json
from producer_setup import init_producer, topic
import time

def main():
    response = connect_to_api()
    
    data = extract_json(response)

    producer = init_producer()
    

    for stock in data:
        result = {
            "date": stock["date"],
            "symbol": stock["symbol"],
            "open": float(stock["open"]),
            "low": float(stock["low"]),
            "high": float(stock["high"]),
            "close": float(stock["close"])
        }
        
        producer.send(topic, result)
        producer.flush()
        
        print(f'Data sent to {topic} topic')
        
        time.sleep(2)
        
    
    producer.close()    


if __name__ == "__main__":
    main()