# -*- coding: utf-8 -*-
import unittest
import serial

class RAC805:
    def __init__(self):
        self._ser = serial.Serial('/dev/ttyUSB0',9600)

    def moveazel(self,az,el):
        command = "AZ"+str(az)+" EL"+str(el)+"\r"
        self._ser.write(command)
        return True

    def stop(self):
        command = "\r"
        self._ser.write(command+"\r")
        return True

    def recieveenable(self):
        result=self._ser.readline()
        print result
        readdata=">> "
        return ">>" in readdata

    def close(self):
        self._ser.close()
        return True

class Antenna(object):
    def __init__(self,rotatormodel):
        if rotatormodel == "RAC805":
            self._radio = RAC805()
    def moveazel(self,az,el):
        return self._radio.moveazel(az,el)
    def stop(self):
        return self._radio.stop()
    def recieveenable(self):
        return self._radio.recieveenable()
    def close(self):
        return self._radio.close()

class testAntenna(unittest.TestCase):
    #def testcommand(self):
    #    ant = Antenna("RAC805")
    #    az=0.0
    #    el=0.0
    #    self.assertTrue(ant.moveazel(az,el))
    #    self.assertTrue(ant.stop())
    #    self.assertTrue(ant.recieveenable())
    #    self.assertTrue(ant.close())
    #def testmoveantenna(self):
    #    ant = Antenna("RAC805")
    #    az=0.0
    #    el=0.0
    #    self.assertTrue(ant.moveazel(az,el))
    #    self.assertTrue(ant.stop())
    #    self.assertTrue(ant.close())
    def testmoveanetnna(self):
        ant = Antenna("RAC805")
        az=10.0
        el=0.0
        self.assertTrue(ant.moveazel(az,el))
        self.assertTrue(ant.recieveenable())
        self.assertTrue(ant.close())
        
unittest.main()
