# -*- coding: utf-8 -*-

import unittest
import Orbitcalc
import math
import ephem
import datetime


class testOrbitCalc(unittest.TestCase):

    #def testOrbitcalc(self):
    #    orbitinfo = Orbitcalc.Orbitcalc(gslat='43', gslon='141', gselev='50')
    #    orbitinfo.SatInfo('iss',
    #                  '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
    #                  '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
    #                  '437.234')
    #    satlat, satlon, satfreq,aos,los,elmax = orbitinfo.CalcObserve()
    #    print satlat
    #    print satlon
    #    print satfreq

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
    #def testcalcrateAOS(self):
    #    orbitinfo = Orbitcalc.Orbitcalc(gslat=43,gslon=141,gselev=50)
    #    orbitinfo.SatInfo('iss',
    #                  '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
    #                  '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
    #                  437.234)

if __name__ == "__main__":
    unittest.main()
