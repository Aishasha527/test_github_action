# python3.8

import random
import logging
import time

from paho.mqtt import client as mqtt_client


broker = 'o0e292ed.ala.cn-hangzhou.emqxsl.cn'
port = 8883
topic = "testtopicaishasha"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-tls-pub-sub-{random.randint(0, 1000)}'
username = 'emqx_online_test_f8fa40d7'
password = '0c]0f_6f93edJ38>e03E94c5700Z9M9R'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # client = mqtt_client.Client(client_id)
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.tls_set(ca_certs='./emqxsl-ca.crt')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()