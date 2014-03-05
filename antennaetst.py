
import unittest
import antenna

class testAntenna(unittest.TestCase):
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

