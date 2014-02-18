
import unittest
import antenna

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
        ant = antenna.Antenna("RAC805")
        ant.connect("/dev/ttyUSB1")
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

