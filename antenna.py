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

    def _receive(self):
        self.data = ""
        while self.closing:
            self.data = str(self.ser.readline())
            time.sleep(0.0001)

    def recieve(self):
        result = ""
        while not(">>" in result):
            time.sleep(0.00001)
            result = self.ser.readline()
        return True

    def stop(self):
        command = "\r"
        self._ser.write(command+"\r")
        if self.recieve():
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
