# -*- coding: utf-8 -*-

import unittest
import config


class testconfig(unittest.TestCase):
    def testconfig(self):
        conf = config.ConfigRead()
        self.assertEqual('43.134694', conf.read('lat'))
        self.assertEqual('141.248194', conf.read('lon'))
        self.assertEqual('50', conf.read('height'))
        self.assertEqual('RAC805', conf.read('antenna'))
        self.assertEqual('IC910', conf.read('radio'))
        self.assertEqual('/dev/tty.USB2', conf.read('antennaport'))
        self.assertEqual('9600', conf.read('antennabaudrate'))
        self.assertEqual('/dev/tty.USB1', conf.read('radioport'))
        self.assertEqual('19200', conf.read('radiobaudrate'))
        data = conf.read()
        self.assertEqual('43.134694', data['lat'])
        self.assertEqual('141.248194', data['lon'])
        self.assertEqual('RAC805', data['antenna'])
        self.assertEqual('50', data['height'])
        self.assertEqual('IC910', data['radio'])
        self.assertEqual('/dev/tty.USB2', data['antennaport'])
        self.assertEqual('9600', data['antennabaudrate'])
        self.assertEqual('/dev/tty.USB1', data['radioport'])
        self.assertEqual('19200', data['radiobaudrate'])

unittest.main()
