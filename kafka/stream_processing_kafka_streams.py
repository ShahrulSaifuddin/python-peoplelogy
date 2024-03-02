from confluent_kafka import Consumer, Producer, KafkaError, SerializingProducer
from confluent_kafka.serialization import StringDeserializer, StringSerializer
import json
import time

# Configure your Kafka consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest',
}

# Create a Kafka consumer
consumer = Consumer(consumer_conf)
topic = 'stock_prices'
consumer.subscribe([topic])
print(f"Subscribed to topic: {topic}")

# Configure your producer
producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    # Other configuration options
}

# Create a SerializingProducer
producer = SerializingProducer(producer_conf)

# Example state store
stock_state_store = {}

# Function to calculate price change percentage
def calculate_price_change_percentage(previous_price, current_price):
    return ((current_price - previous_price) / previous_price) * 100

# Main loop for consuming messages
while True:
    msg = consumer.poll(timeout=1000)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Consumer error: {msg.error()}")
            break

    # Deserialize the message
    try:
        message = json.loads(msg.value().decode('utf-8'))
        stock_symbol = message['symbol']
        current_price = float(message['price'])
        print(f"Received message: {message}")
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        continue

    # State store operations
    if stock_symbol in stock_state_store:
        previous_price = stock_state_store[stock_symbol]
        price_change_percentage = calculate_price_change_percentage(previous_price, current_price)

        # Check against threshold and trigger alert
        threshold = 5.0
        if abs(price_change_percentage) > threshold:
            print(f"ALERT: Stock {stock_symbol} has a price change of {price_change_percentage}%")

    # Update state store with current price
    stock_state_store[stock_symbol] = current_price

    # Produce the message to another topic
    output_topic = 'price_change_alerts'
    producer.produce(
        topic=output_topic,
        key=stock_symbol,
        value=json.dumps({'symbol': stock_symbol, 'price_change_percentage': price_change_percentage}),
        on_delivery=lambda err, msg: print(f'Message delivered to {msg.topic()} [{msg.partition()}], error: {err}' if err is not None else f'Message delivered to {msg.topic()} [{msg.partition()}]'),
    )

    producer.flush()

# Close consumer and producer
consumer.close()
producer.close()