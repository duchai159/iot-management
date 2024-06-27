import Simulator
import paho.mqtt.client as mqtt_client
import time, json

broker = "37bed9790dc74f54be13974aa7b03429.s1.eu.hivemq.cloud"
port = 8883

username = 'duchai159'
password = 'Haikun159@'

def connect_broker():
    client = mqtt_client.Client(protocol=mqtt_client.MQTTv5)
    client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)
    result = client.connect(broker, port)
    return client
 
def main():
    publisher = connect_broker()
    publisher.loop_start()

    try:
        while True:
            temperature = Simulator.simulate_temperature_sensor()
            humidity = Simulator.simulate_humidity_sensor()
            smoke = Simulator.simulate_smoke_sensor()
            gas = Simulator.simulate_gas_sensor()
            light = Simulator.simulate_light_sensor()

            current_time = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
            
            house_data = {
                "room_data": {
                    "temperature": {
                        "value": temperature,
                        "unit": "°C"
                    },
                    "humidity": {
                        "value": humidity,
                        "unit": "%"
                    }
                },
                "timestamp": current_time
            }

            house_payload = json.dumps(house_data)
            publisher.publish("house", house_payload)
            print("[", current_time,"] Published: house data to topic house!")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("Publisher interrupted by user")
    finally:
        publisher.loop_stop()
        publisher.disconnect()
        print("Disconnected publisher from broker safely")

if __name__ == "__main__":
    main()