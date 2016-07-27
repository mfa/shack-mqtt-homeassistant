import paho.mqtt.client as mqtt
import yaml


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("hass.shack", 1883, 60)

client.loop_start()

data = yaml.load(open("/root/.homeassistant/configuration.yaml"))
for sensor in data.get('sensor'):
    name = sensor.get('name').strip().split(' ')[0]
    topic = sensor.get('state_topic').split('/')[1]
    msg = client.publish('/home-assistant/{}/name'.format(topic), name)
    print(topic)
    print(name)
    msg.wait_for_publish()

