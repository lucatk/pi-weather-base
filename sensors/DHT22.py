import dhtreader
import time

class DHT22(object):

    def __init__(self,pinnum):
        dhtreader.init()
        dhtreader.lastDataTime = 0
        dhtreader.lastData = (None,None)
        self.pinNum = pinnum
        return

    def read_temperature(self):
        tm = dhtreader.lastDataTime
        if (time.time() - tm) < 2:
            t, h = dhtreader.lastData
        else:
            tim = time.time()
            try:
                t, h = dhtreader.read(22, self.pinNum)
            except Exception:
                t, h = dhtreader.lastData
            dhtreader.lastData = (t, h)
            dhtreader.lastDataTime = tim
        temp = t
        return temp

    def read_humidity(self):
        tm = dhtreader.lastDataTime
        if (time.time() - tm) < 2:
            t, h = dhtreader.lastData
        else:
            tim = time.time()
            try:
                t, h = dhtreader.read(22, self.pinNum)
            except Exception:
                t, h = dhtreader.lastData
            dhtreader.lastData = (t, h)
            dhtreader.lastDataTime = tim
        return h
