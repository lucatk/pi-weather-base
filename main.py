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
import sensors.DHT22 as DHT22

sensor_bmp180 = BMP085.BMP085(busnum=config["bmp180"]["i2cbus"])
sensor_dht22 = DHT22.DHT22(pinnum=config["dht22"]["pinnum"])

# scr = curses.initscr()
# curses.noecho()
# curses.cbreak()

# try:
while True:
    print "".join(["\t\tTemperature (BMP180): ", str(sensor_bmp180.read_temperature()), "\tPressure (BMP180): ", str(sensor_bmp180.read_pressure()), "\tTemperature (DHT22): ", str(sensor_dht22.read_temperature(), "\tHumidity (DHT22): ", str(sensor_dht22.read_humidity()), "%\r")]) ,
    stdout.flush()
    # scr.addstr(0, 0, "".join(["\t\tTemperature (BMP180): ", str(sensor_bmp180.read_temperature()), "\tPressure (BMP180): ", str(sensor_bmp180.read_pressure())]))
    # scr.addstr(1, 0, "".join(["\t\tTemperature (DHT22): ", str(sensor_dht22.read_temperature()), "\tHumidity (DHT22): ", str(sensor_dht22.read_humidity()), "%"]))
    # scr.refresh()
    time.sleep(1)
# finally:
#     curses.echo()
#     curses.nocbreak()
#     curses.endwin()