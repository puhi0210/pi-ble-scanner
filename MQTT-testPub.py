
# Testni program za preverjanje povezave z MQTT brokerjem

# Knjižnica za MQTT
import sys
import paho.mqtt.client as paho
# Knjižnice za okolske spremenljivke
from dotenv import load_dotenv
import os

# Za izpis časa
import time

# MQTT Publish QoS
Pub_QoS = 1
# Publish topic
Pub_Topic = "puhi0210/test_topic"

# Naloži okoljske spremenljivke
load_dotenv('.env')
broker_address: str = os.getenv('BROKER_ADDR')
broker_port: int = int(os.getenv('BROKER_PORT'))
broker_keepalive: int = int(os.getenv('BROKER_KA'))

print(f"Broker ADDRESS: {broker_address}")
print(f"Broker PORT: {broker_port}")

# Inicializacija MQTT klienta
client = paho.Client()

# Povezava na MQTT broker
if client.connect(broker_address, broker_port, broker_keepalive) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

# Pridobitev trenutnega časa
trenutni_cas = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Tvorba odgovora
result = "Paho mqtt deluje pravilno. Trenutni čas: " + trenutni_cas

# Objava na MQTT broker
client.publish(Pub_Topic, result, Pub_QoS)
client.disconnect()