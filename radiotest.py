# -*- coding: utf-8 -*-

import unittest
import radio

class testradio(unittest.TestCase):

    def testradioIC910(self):
        ic910 = radio.Radio("IC910","Sub","CW")
        ic910.connect("/dev/ttyUSB0")
        ic910.changefreq(437.38590)
        print "Sub FM"
        ic910.changemode("Sub","FM")
        print "Sub CW"
        ic910.changemode("Sub","CW")
        ic910.close()

unittest.main()
