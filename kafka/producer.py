from confluent_kafka import Producer
import json
import time

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'my-topic'

# Create Kafka producer
producer_conf = {'bootstrap.servers': bootstrap_servers}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Generate and send sample sensor data
def send_sensor_data():
    for i in range(10):
        sensor_data = {'sensor_id': i, 'value': round(i * 1.5, 2), 'timestamp': int(time.time())}
        producer.produce(topic, key=str(i), value=json.dumps(sensor_data), callback=delivery_report)
        producer.poll(0.5)  # Poll for events, set a timeout for responsiveness

    producer.flush()  # Wait for any outstanding messages to be delivered and delivery reports to be received

if __name__ == '__main__':
    send_sensor_data()
