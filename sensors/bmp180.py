import sensor
import bmpBackend

class BMP180(sensor.Sensor):
    bmpClass = None

    def __init__(self, measurement, config):
        self.measurement = measurement
        if (BMP180.bmpClass == None):
            BMP180.bmpClass = bmpBackend.BMP180(bus=int(config["i2cbus"]))
        return

    def getVal(self):
        if "temp" in self.measurement:
            return BMP180.bmpClass.readTemperature()
        elif "pres" in self.measurement:
            return BMP180.bmpClass.readPressure() * 0.01  # to convert to Hectopascals
