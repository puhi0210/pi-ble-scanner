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


# Maximalni RSSI za določanje bližine neprave
minRSSI = -70


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

# Skeniraj naprave Bluetooth 10 s
devices = scanner.scan(10.0)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Število naprav
st_naprav = len(devices)

# Inicializacija MQTT klienta
client = paho.Client()

# Povezava na MQTT broker
if client.connect(broker_address, broker_port, broker_keepalive) != 0:
    print(f"Ni se bilo mogoče povezati na broker!")
    sys.exit(1)
else:
    print(f"Povezava z brokerjem vzpostavljena")
   

# Tvorba odgovora
result = "Št. BLE naprav: " + str(st_naprav)

# Objava na MQTT broker
client.publish(pub_topic, result, Pub_QoS)
client.disconnect()


# Izpis
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Skeniranje končano.")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Vse naprave:\n")

for dev in devices:
    print("Naprava %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))
    print("\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Naprave z lokalnim imenom:\n")

for dev in devices:
    if any("Local Name" in desc for (_, desc, _) in dev.getScanData()):
        print("Naprava %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            if "Local Name" in desc:
                print("  %s = %s" % (desc, value))
        print("\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Preverjanje bližine naprav glede na moč signala
devicesNearBy = []

for dev in devices:
    if dev.rssi >= minRSSI:
        devicesNearBy.append(dev)

print("Število zaznanih naprav:", len(devices), "\n")
print("Število naprav v bližini (RSSI večji od %s dB): %s\n" % (minRSSI, len(devicesNearBy)))
