import subprocess
import signal
import time

zk_command = "/opt/kafka/kafka_2.13-3.7.0/bin/zookeeper-server-start.sh /opt/kafka/kafka_2.13-3.7.0/config/zookeeper.properties"
zk_process = subprocess.Popen(zk_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("Zookeeper started")

kafka_command = "/opt/kafka/kafka_2.13-3.7.0/bin/kafka-server-start.sh /opt/kafka/kafka_2.13-3.7.0/config/server.properties"
kafka_process = subprocess.Popen(kafka_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("Kafka started")

try:
 while True:
  time.sleep(1)
except KeyboardInterrupt:
 print(" <<Terminating Kafka Process>>")
 kafka_process.send_signal(signal.SIGINT)
 kafka_process.wait()
 zk_process.send_signal(signal.SIGINT)
 zk_process.wait()