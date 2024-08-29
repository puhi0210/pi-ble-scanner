
# Testni program za preverjanje povezave z MQTT brokerjem

import sys
# Knjižnica za MQTT
import paho.mqtt.client as paho
# Knjižnice za okolske spremenljivke
from dotenv import load_dotenv
import os

# Za izpis časa
import time

# MQTT Publish QoS
Pub_QoS = 1

# Naloži okoljske spremenljivke
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

result = "Paho mqtt deluje pravilno. Trenutni čas: " + trenutni_cas

client.publish("puhi0210/test_topic", result, Pub_QoS)
client.disconnect()