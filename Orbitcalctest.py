# -*- coding: utf-8 -*-

import unittest
import Orbitcalc
import math
import ephem
import datetime


class testOrbitCalc(unittest.TestCase):

    def testOrbitcalc(self):
        orbitinfo = Orbitcalc.Orbitcalc(gslat='43', gslon='141', gselev='50')
        orbitinfo.SatInfo('iss',
                      '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
                      '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
                      '437.234')
        satlat, satlon, satfreq,aos,los,elmax = orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq

    def testinputparamcheck(self):
        orbitinfo = Orbitcalc.Orbitcalc(gslat=43, gslon=141, gselev=50)
        orbitinfo.SatInfo('iss',
                      '1 25544U 98067A   14055.57109976  .00016176  00000-0  28381-3 0  7454',
                      '2 25544  51.6505 297.8534 0003858 169.6570 271.9103 15.50692173873853',
                      437.234)
        satlat, satlon, satfreq,aos,los,elmax= orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq
        print str(aos.strftime("%H:%M:%S"))
        print str(los.strftime("%H:%M:%S"))
        print elmax
    def testcalcrateAOS(self):
        orbitinfo = Orbitcalc.Orbitcalc(gslat=43,gslon=141,gselev=50)
        orbitinfo.SatInfo('iss',
                      '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
                      '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
                      437.234)

if __name__ == "__main__":
    unittest.main()
