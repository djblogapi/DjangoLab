import json
from datetime import datetime

import paho.mqtt.client as mqtt

from mongo import MQTT

# Set the MQTT broker's address and port
BROCKER_ADDRESS = "0.0.0.0"
BROCKER_ADDRESS = "recognition_mosquitto"
BROCKER_PORT = 1883

# Set the topic to subscribe to
TOPIC = "face_recognition"


# Callback when a message is received

def on_message(client, userdata, msg):
    encoding = json.loads(msg.payload.decode())
    created = datetime.now()
    data = {"created": created, "encoding": encoding}
    MQTT(**data).save()
    print("Message saved")

# Create an MQTT client
client = mqtt.Client()

# Set the callback for message reception
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROCKER_ADDRESS, BROCKER_PORT, 60)

# Subscribe to the topic
client.subscribe(TOPIC)

# Loop to continuously listen for messages
client.loop_forever()
