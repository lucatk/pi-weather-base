####     CONFIG     ####

config = {
    "bmp180": {
        "i2cbus": 1
    }
}

####   END CONFIG   ####


import sys
import time
import RPi.GPIO as GPIO

from sys import stdout

import sensors.BMP085 as BMP085

sensor_bmp180 = BMP085.BMP085(busnum=config["bmp180"]["i2cbus"])

while True:
    print "".join(["\t\tTemperature (BMP180): ", str(sensor_bmp180.read_temperature()), "\tPressure (BMP180): ", str(sensor_bmp180.read_pressure()), "\r"]) ,
    stdout.flush()
    time.sleep(1)