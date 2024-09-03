# Knjižnice za Bluetooth scanner
from bluepy.btle import Scanner, DefaultDelegate

# Knjižnica za MQTT
import sys
import paho.mqtt.client as paho
# Knjižnice za okolske spremenljivke
from dotenv import load_dotenv
import os

# MQTT Publish QoS
Pub_QoS = 1


# Naloži okoljske spremenljivke
load_dotenv('.env')
broker_address: str = os.getenv('BROKER_ADDR')
broker_port: int = int(os.getenv('BROKER_PORT'))
broker_keepalive: int = int(os.getenv('BROKER_KA'))
topic_prefix: str = os.getenv('TOPIC_PRFX')

pub_topic = topic_prefix + "/BLE-scanner/numOfDev"

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("MQTT")
print(f"Broker ADDRESS: {broker_address}")
print(f"Broker PORT: {broker_port}")
print(f"Publish topic: {pub_topic}\n")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Class za skeniranje
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Najdena naprava", dev.addr)
        elif isNewData:
            print("Sprejeti novi podatki iz", dev.addr)

# Inicializacija skenerja
scanner = Scanner().withDelegate(ScanDelegate())

