
# Testni program za sprejemanje MQTT sporočil iz brokerja

import sys
# Knjižnica za MQTT
import paho.mqtt.client as paho
# Knjižnice za okolske spremenljivke
from dotenv import load_dotenv
import os

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Naloži okoljske spremenljivke
load_dotenv('.env')
broker_address: str = os.getenv('BROKER_ADDR')
broker_port: int = int(os.getenv('BROKER_PORT'))
broker_keepalive: int = int(os.getenv('BROKER_KA'))

print(f"Broker ADDRESS: {broker_address}")
print(f"Broker PORT: {broker_port}")


# Inicializacija MQTT klienta
client = paho.Client()
client.on_message = message_handling


# Povezava na MQTT broker
if client.connect(broker_address, broker_port, broker_keepalive) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

# Naročanje na topic
client.subscribe("puhi0210/test_topic")

# Prekinitev programa
try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()