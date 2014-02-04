# -*- coding: utf-8 -*-

import unittest
import Orbitcalc
import radio

class testmain(unittest.TestCase):

    def testradioIC910(self):
        IC910 = radio.Radio("IC910","Sub","CW")
        IC910.connect("0")
        #print radio.getfreq()
        #radio.getmode()
        IC910.chengefreq(437.4801)
        #print "Sub FM"
        #radio.chengemode("Sub","FM")
        #print "Sub CW"
        #radio.chengemode("Sub","CW")
        #print "Main FM"
        #radio.chengemode("Main","FM")
        #print "Main CW"
        #radio.chengemode("Main","CW")
        IC910.close()

    def testorbit(self):
        orbitinfo = Orbitcalc.Orbitcalc(gslat='43', gslon='141', gselev='50')
        orbitinfo.SatInfo('iss',
                      '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
                      '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
                      '437.234', 'FM')
        satlat, satlon, satfreq = orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq

unittest.main()
