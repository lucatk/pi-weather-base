####     CONFIG     ####

config = {
    "bmp180": {
        "i2cbus": 1
    },
    "dht22": {
        "pinnum": 4
    }
}

####   END CONFIG   ####


import sys
import time
import curses
import RPi.GPIO as GPIO

from sys import stdout

import sensors.BMP085 as BMP085
import sensors.Adafruit_DHT as Adafruit_DHT

sensor_bmp180 = BMP085.BMP085(busnum=config["bmp180"]["i2cbus"])
sensor_dht22 = Adafruit_DHT.DHT22

scr = curses.initscr()
curses.noecho()
curses.cbreak()

try:
    while True:
        scr.addstr(0, 0, "".join(["\t\tTemperature (BMP180): ", str(sensor_bmp180.read_temperature()), "\tPressure (BMP180): ", str(sensor_bmp180.read_pressure())]))
        humidity, temperature = Adafruit_DHT.read_retry(sensor_dht22, config["dht22"]["pinnum"])
        scr.addstr(1, 0, "".join(["\t\tTemperature (DHT22): ", str(temperature), "\tHumidity (DHT22): ", str(humidity), "%"]))
        scr.refresh()
        time.sleep(1)
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()