import zmq
import sys
import time
import json

from sys import stdout

import Adafruit_DHT_old

sensor_DHT = Adafruit_DHT_old.DHT22
sensor_DHT_PIN = 4

zmqContext = zmq.Context()
socket = zmqContext.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")

while True:
    humid, dht_temp = Adafruit_DHT_old.read_retry(sensor_DHT, sensor_DHT_PIN)

    data = {
        "humidity": humid,
        "dht_temperature": dht_temp
    }
    socket.send_json(json.dumps(data))
    time.sleep(10)