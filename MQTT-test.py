import sys

import paho.mqtt.client as paho

class mqttBrok:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port


client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.publish("test_topic", "Hi, paho mqtt client works fine!", 0)
client.disconnect()