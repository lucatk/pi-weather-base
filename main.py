####     CONFIG     ####

config = {
    "bmp180": {
        "i2cbus": 1
    }
}

####   END CONFIG   ####


import sys
import RPi.GPIO as GPIO

from sys import exit

from sensors import bmp180

temperatureSensor = bmp180.BMP180("temp", config["bmp180"])
print temperatureSensor.getVal()