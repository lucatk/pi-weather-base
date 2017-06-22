import zmq
import sys
import time
import json

from sys import stdout

import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

sensor_DHT = Adafruit_DHT.DHT22
sensor_DHT_PIN = 4

# sensor_BMP = BMP085.BMP085()

SPI_PORT = 0
SPI_DEVICE = 0
sensor_MCP3008 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

zmqContext = zmq.Context()
socket = zmqContext.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

while True:
    humid, dht_temp = Adafruit_DHT.read_retry(sensor_DHT, sensor_DHT_PIN)
    data = {
        "dht_humidity": humid,
        "dht_temperature": dht_temp,
        # "bmp_temperature": sensor_BMP.read_temperature(),
        # "bmp_pressure": sensor_BMP.read_pressure(),
        # "bmp_altitude": sensor_BMP.read_altitude(),
        # "bmp_slpressure": sensor_BMP.read_sealevel_pressure(),
        "mcp_smoke_voltage": sensor_MCP3008.read_adc(0),
        "mcp_light_voltage": sensor_MCP3008.read_adc(1)
    }
    socket.send_json(json.dumps(data))
    socket.recv()
    time.sleep(10)