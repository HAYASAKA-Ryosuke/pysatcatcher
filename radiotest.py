# -*- coding: utf-8 -*-

import unittest
import radio

class testradio(unittest.TestCase):

    def testradioIC910(self):
        ic910 = radio.Radio("IC910","Sub","CW")
        ic910.connect("/dev/ttyUSB0")
        #print ic910.getfreq()
        #ic910.getmode()
        ic910.changefreq(437.38590)
        #print "Sub FM"
        #ic910.chengemode("Sub","FM")
        print "Sub CW"
        ic910.changemode("Sub","FM")
        #print "Main FM"
        #ic910.chengemode("Main","FM")
        #print "Main CW"
        #ic910.chengemode("Main","CW")
        ic910.close()

    #def testradioIC911(self):
    #    radio = Radio("IC910","Sub","CW")
    #    radio.connect("connect")
    #    #print radio.getfreq()
    #    #radio.getmode()
    #    radio.chengefreq(437.4801)
    #    print "Sub FM"
    #    radio.chengemode("Sub","FM")
    #    print "Sub CW"
    #    radio.chengemode("Sub","CW")
    #    print "Main FM"
    #    radio.chengemode("Main","FM")
    #    print "Main CW"
    #    radio.chengemode("Main","CW")
    #    radio.close()

unittest.main()
