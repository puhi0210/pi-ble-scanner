
# Testni program za preverjanje povezave z MQTT brokerjem

import sys
import paho.mqtt.client as paho

from dotenv import load_dotenv
import os

# Za izpis časa
import time

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

trenutni_cas = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

result = "Paho mqtt client works fine. Current time is: " + trenutni_cas

client.publish("puhi0210/test_topic", result, 1)
client.disconnect()