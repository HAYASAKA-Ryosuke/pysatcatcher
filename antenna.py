# -*- coding: utf-8 -*-

import serial
import time


class RAC805:
    def connect(self, port, baudrate):
        self._ser = serial.Serial(port, int(baudrate))

    def moveazel(self, az, el):
        if(el >= 0.0):
            command = "AZ"+str(az)+" EL"+str(el)+"\r"
            self._ser.write(command)
        return True

    def stop(self):
        command = "\r"
        self._ser.write(command+"\r")
        return True

    def recieve(self):
        result = ""
        while not(">>" in result):
            time.sleep(0.05)
            result = self._ser.read(self._ser.inWaiting())
        return True

    def close(self):
        self._ser.close()
        return True


class Antenna(object):

    def __init__(self, rotatormodel):
        if rotatormodel == "RAC805":
            self._radio = RAC805()

    def connect(self, port, baudrate):
            self._radio.connect(port)

    def moveazel(self, az, el):
        return self._radio.moveazel(az, el)

    def stop(self):
        return self._radio.stop()

    def recieve(self):
        self._radio.recieve()

    def close(self):
        return self._radio.close()
