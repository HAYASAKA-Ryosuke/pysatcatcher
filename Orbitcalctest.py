# -*- coding: utf-8 -*-

import unittest
import Orbitcalc

class testOrbitCalc(unittest.TestCase):

    def testinputparamcheck(self):
        orbitinfo = Orbitcalc.Orbitcalc(gslat=43.131, gslon=141.253, gselev=69)
        orbitinfo.SatInfo('iss',
                      '1 39573U 14009B   14062.21627791  .00113488  00000-0  13212-2 0   165',
                      '2 39573  65.0133  48.0708 0005572 328.4023  31.6776 15.61091733   539',
                      437.150)
        satlat, satlon, satfreq,aos,los,elmax= orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq
        print str(aos.strftime("%H:%M:%S"))
        print str(los.strftime("%H:%M:%S"))
        print elmax

if __name__ == "__main__":
    unittest.main()
