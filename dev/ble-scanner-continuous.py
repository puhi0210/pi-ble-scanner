# Knjižnice za Bluetooth scanner
from bluepy.btle import Scanner, DefaultDelegate
# Knjižnica za MQTT
import sys
import paho.mqtt.client as paho
# Knjižnice za okolske spremenljivke
from dotenv import load_dotenv
import os
# Knjižnica za zakasnitve
import time

# Čas skeniranja naprav v sekundah
scan_time=10

# Čas med posameznimi skeni v sekundah
scan_delay=60

'''
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
'''
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

try:
    while True:
        # Skeniranje naprav Bluetooth
        devices = scanner.scan(scan_time)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        
        print("Število zaznanih naprav:", len(devices), "\n")

        # Počakaj pred ponovnim skeniranjem
        time.sleep(scan_delay)

except KeyboardInterrupt:
    print(f"\nPrekinjeno s strani uporabnika. Zapiranje...")
    
finally:
    #client.disconnect()
    #print("MQTT klient odklopljen.")
    print(f"\nZaključek programa\n")