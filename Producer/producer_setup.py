import os

from kafka import KafkaProducer
import json


topic = "stock_analysis"


def init_producer():
    producer = KafkaProducer(
        bootstrap_servers=[os.getenv("KAFKA_BOOTSTRAP_SERVER", "kafka:9092")],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    return producer