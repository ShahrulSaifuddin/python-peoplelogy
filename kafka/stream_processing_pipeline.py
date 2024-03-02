from confluent_kafka import Consumer, Producer, KafkaError
import json

# Configuration for Kafka consumer and producer
bootstrap_servers = 'localhost:9092'  # Replace with your actual Kafka broker addresses
group_id = 'your_consumer_group'
auto_offset_reset = 'earliest'

# Topics
stock_prices_topic = 'stock_prices'
alerts_topic = 'price_change_alerts'
average_prices_topic = 'average_prices'

# Threshold for significant price changes (5%)
price_change_threshold = 0.05

# Kafka Consumer for stock_prices topic
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': auto_offset_reset,
}

# Kafka Producer for alerts and average_prices topics
producer_conf = {
    'bootstrap.servers': bootstrap_servers
}

# Create consumers and producers
consumer = Consumer(consumer_conf)
producer = Producer(producer_conf)

# Subscribe to the stock_prices topic
consumer.subscribe([stock_prices_topic])

# In-memory state for average prices
average_prices = {}

try:
    while True:
        msg = consumer.poll(1.0)  # Adjust the timeout based on your requirements
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Consumer error: {msg.error()}")
                break

        # Process the message
        stock_symbol = msg.key()
        current_price = msg.value()['current_price']
        timestamp = msg.value()['timestamp']

        # Check for significant price change and trigger alert
        if stock_symbol in average_prices:
            average_price = average_prices[stock_symbol]
            price_change_percentage = abs((current_price - average_price) / average_price)

            if price_change_percentage >= price_change_threshold:
                # Trigger alert
                alert_message = f"Significant price change for {stock_symbol} at {timestamp}: {price_change_percentage}%"
                print(alert_message)

        # Update average price
        if stock_symbol not in average_prices:
            average_prices[stock_symbol] = current_price
        else:
            average_prices[stock_symbol] = (average_prices[stock_symbol] + current_price) / 2

        # Send message to average_prices topic
        producer.produce(
            average_prices_topic,
            key=stock_symbol,
            value=json.dumps({'average_price': average_prices[stock_symbol], 'timestamp': timestamp})
        )
        producer.flush()

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
