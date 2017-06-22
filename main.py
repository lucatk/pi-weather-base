import zmq
import sys
import time
import json

from sys import stdout

import Adafruit_DHT
import Adafruit_BMP

sensor_DHT = Adafruit_DHT.DHT22
sensor_DHT_PIN = 4

sensor_BMP = Adafruit_BMP.BMP085.BMP085()

zmqContext = zmq.Context()
socket = zmqContext.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

while True:
    humid, dht_temp = Adafruit_DHT.read_retry(sensor_DHT, sensor_DHT_PIN)
    data = {
        "dht_humidity": humid,
        "dht_temperature": dht_temp,
        "bmp_temperature": sensor_BMP.read_temperature(),
        "bmp_pressure": sensor_BMP.read_pressure(),
        "bmp_altitude": sensor_BMP.read_altitude(),
        "bmp_slpressure": sensor_BMP.read_sealevel_pressure()
    }
    socket.send_json(json.dumps(data))
    socket.recv()
    time.sleep(10)