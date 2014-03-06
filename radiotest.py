# -*- coding: utf-8 -*-

import unittest
import radio
import time

class testradio(unittest.TestCase):

    def testradioIC910(self):
        ic910 = radio.Radio("IC910","Sub","CW")
        ic910.connect("/dev/ttyUSB1",19200)
        ic910.changefreq(437.38590)
        print "Sub CW"
        ic910.changemode("Sub","CW")
        ic910.changefreq(437.32590)
        time.sleep(0.05)
        ic910.changefreq(437.21590)
        time.sleep(0.05)
        ic910.changefreq(437.28590)
        time.sleep(0.05)
        ic910.close()

unittest.main()
