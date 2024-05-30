from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt_client
import json
import time

app = Flask(__name__)

status = {}

actuator = {
        "1": {
            "deviceId": "1",
            "status": False,
            "timestamp": ""
        },
        "2": {
            "deviceId": "2",
            "status": False,
            "timestamp": ""
        },
        "3": {
            "deviceId": "3",
            "status": False,
            "timestamp": ""
        },
        "4": {
            "deviceId": "4",
            "status": False,
            "timestamp": ""
        },
        "5": {
            "deviceId": "5",
            "status": False,
            "timestamp": ""
        },
        "6": {
            "deviceId": "6",
            "status": False,
            "timestamp": ""
        },
    }

broker = "0661a98ef5224ee5980218c5b4f368fe.s1.eu.hivemq.cloud"
port = 8883

username = 'at170310'
password = 'at170310'

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe("status")
    print("[+] Subscribe topic status!")

def on_message(client, userdata, msg):
    current_time = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    if msg.topic == "status":
        status_payload = json.loads(msg.payload)
        for key, item in status_payload.items():
            status[key] = item
            actuator[key]['status'] = item['turnOn']
            actuator[key]['timestamp'] = current_time
        
        client.publish("actuator", json.dumps(actuator))
        print(f"[",current_time,"] INFO: topic status changed!")

client = mqtt_client.Client(protocol=mqtt_client.MQTTv5)
client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_start()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def sta():
    return jsonify(status)

@app.route('/ac')
def ac():
    return jsonify(actuator)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
