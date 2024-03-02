from confluent_kafka import Consumer, KafkaException
import json

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'my-topic'

# Create Kafka consumer
consumer_conf = {'bootstrap.servers': bootstrap_servers, 'group.id': 'my_consumer_group', 'auto.offset.reset': 'earliest'}
consumer = Consumer(consumer_conf)
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages with a timeout
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print('Error: {}'.format(msg.error()))
                break

        # Deserialize and process the received data
        try:
            data = json.loads(msg.value().decode('utf-8'))
            print('Received message: {}'.format(data))
            # Perform your processing or calculations here based on the scenario
        except json.JSONDecodeError as e:
            print('Error decoding JSON: {}'.format(e))

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
