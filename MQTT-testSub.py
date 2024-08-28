import sys
import paho.mqtt.client as paho

from dotenv import load_dotenv
import os

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# uvoz spremenljivk
load_dotenv('.env')
broker_address: str = os.getenv('BROKER_ADDR')
broker_port: int = os.getenv('BROKER_PORT')
broker_keepalive: int = os.getenv('BROKER_KA')


client = paho.Client()
client.on_message = message_handling


if client.connect(broker_address, broker_port, broker_keepalive) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)



client.subscribe("puhi0210/test_topic")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()