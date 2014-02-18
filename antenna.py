# -*- coding: utf-8 -*-
import unittest
import serial
import threading
import time

class RAC805:
    def __init__(self):
        self._ser = serial.Serial('/dev/ttyUSB1',9600)

    def moveazel(self,az,el):
        command = "AZ"+str(az)+" EL"+str(el)+"\r"
        self._ser.write(command)
        return True

    def stop(self):
        command = "\r"
        self._ser.write(command+"\r")
        return True

    def recieve(self):
        result=""
        while not(">>" in result):
            time.sleep(0.05)
            result=self._ser.read(self._ser.inWaiting())
            print result
        return True

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
        
    def recieve(self):
        self._radio.recieve()
        #t=threading.Thread(target=self._radio.recieve())
        #t.setDaemon(True)
        #t.start()
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
        az=0.0
        el=0.0
        self.assertTrue(ant.moveazel(az,el))
        self.assertEqual(None,ant.recieve())
        az=10.0
        el=0.0
        self.assertTrue(ant.moveazel(az,el))
        self.assertEqual(None,ant.recieve())
        az=30.0
        el=0.0
        self.assertTrue(ant.moveazel(az,el))
        self.assertEqual(None,ant.recieve())
        self.assertTrue(ant.close())
        
unittest.main()
