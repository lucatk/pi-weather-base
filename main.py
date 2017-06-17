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

from sys import exit

from sensors import bmp180

temperatureSensor = bmp180.BMP180("temp", config["bmp180"])
pressureSensor = bmp180.BMP180("pres", config["bmp180"])

while True:
    print "".join(["\t\tTemperature (BMP180): ", str(temperatureSensor.getVal()), "\tPressure (BMP180): ", str(pressureSensor.getVal())])
    time.sleep(1)
    print "\r"