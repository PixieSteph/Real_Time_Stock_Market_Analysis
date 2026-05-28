from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'stock_analysis',
    bootstrap_servers=['127.0.0.1:9094'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Starting Kafka consumer. Waiting for messages on topic 'stock_analysis'...")

for message in consumer:
    
    data = message.value
    
    print(f"  Value (Deserialized): {data}")
    
consumer.close()
print("Kafka consumer closed.")
    