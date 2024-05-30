from flask import Flask, render_template, jsonify, request
import paho.mqtt.client as mqtt_client
import json
import time

app = Flask(__name__)

mqtt_data = None

settings = {}
actuator_data = {}
status = {
    "1": {
        "deviceId": 1,
        "turnOn": False
    },
    "2": {
        "deviceId": 2,
        "turnOn": False
    },
    "3": {
        "deviceId": 3,
        "turnOn": False
    },
    "4": {
        "deviceId": 4,
        "turnOn": False
    },
    "5": {
        "deviceId": 5,
        "turnOn": False
    },
    "6": {
        "deviceId": 6,
        "turnOn": False
    },
}

broker = "0661a98ef5224ee5980218c5b4f368fe.s1.eu.hivemq.cloud"
port = 8883

username = 'at170310'
password = 'at170310'

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe("house")
    print("[+] Subscribe topic house!")
    client.subscribe("actuator")
    print("[+] Subscribe topic actuator!")

def on_message(client, userdata, msg):
    current_time = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    if msg.topic == "house":
        global mqtt_data
        mqtt_data = json.loads(msg.payload)
        
        print(f"[",current_time,"] INFO: topic house changed!")

        for key, item in settings.items():
            if item["mode"]=="auto":
                auto(item['deviceId'], float(item['min']), float(item['max']))
    elif msg.topic == "actuator":
        actuator_payloads = json.loads(msg.payload)

        for key, item in actuator_payloads.items():
            actuator_data[key] = item
        print(f"[", current_time,"] INFO: topic actuator changed!")

client = mqtt_client.Client(protocol=mqtt_client.MQTTv5)
client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(mqtt_data)

@app.route('/se')
def get_settings():
    return jsonify(settings)

@app.route('/status')
def get_status():
    return jsonify(status)

@app.route('/actuator')
def get_ac():
    return jsonify(actuator_data)

@app.route("/save-settings", methods = ['POST'] )
def save_settings():
    try:
        device_settings = request.json
        device_id = device_settings["deviceId"]

        if (device_settings['mode'] == "manual"):
            toggle(device_id, device_settings["turnOn"])

        settings[device_id] = device_settings
        return jsonify({"message": "Settings saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def toggle(device_id, turn_on):
    global status
    status[device_id]["turnOn"] = turn_on

    client.publish("status", json.dumps(status))

def auto(device_id, min, max):
    if device_id=="1":
        value = mqtt_data["room_data"]["temperature"]["value"]
    elif device_id=="2":
        value = mqtt_data["room_data"]["humidity"]["value"]
    elif device_id=="3":
        value = mqtt_data["room_data"]["temperature"]["value"]
    elif device_id=="4":
        value = mqtt_data["room_data"]["smoke"]["value"]
    elif device_id=="5":
        value = mqtt_data["room_data"]["gas"]["value"]
    elif device_id=="6":
        value = mqtt_data["outdoor_data"]["light"]["value"]
    turn_on = (value >= min and value <= max)

    toggle(device_id, turn_on)

if __name__ == '__main__':
    app.run(debug=True)
