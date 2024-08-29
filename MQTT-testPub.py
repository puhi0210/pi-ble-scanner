
# Testni program za preverjanje povezave z MQTT brokerjem

import sys
import paho.mqtt.client as paho

from dotenv import load_dotenv
import os

load_dotenv('.env')

broker_address: str = os.getenv('BROKER_ADDR')
broker_port: int = int(os.getenv('BROKER_PORT'))
broker_keepalive: int = int(os.getenv('BROKER_KA'))

print(f"Broker ADDRESS: {broker_address}")
print(f"Broker PORT: {broker_port}")

client = paho.Client()

if client.connect(broker_address, broker_port, broker_keepalive) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.publish("puhi0210/test_topic", "Hi, paho mqtt client works fine!", 1)
client.disconnect()