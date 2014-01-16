# -*- coding: utf-8 -*-

import ConfigParser
import unittest

class ConfigRead(object):
    __lat = ''
    __lon = ''
    __height = ''
    __radio = ''
    __antenaport = ''
    __antenabaudrate = ''
    __radioport = ''
    __radiobaudrate = ''
    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read('config.ini')
        self.__lat = config.get('GroundStation','Lat')
        self.__lon = config.get('GroundStation','Lon')
        self.__height = config.get('GroundStation','Height')
        self.__radio = config.get('GroundStation','Radio')
        self.__antenaport = config.get('GroundStation','AntenaPort')
        self.__antenabaudrate = config.get('GroundStation','AntenaBaudRate')
        self.__radioport = config.get('GroundStation','RadioPort')
        self.__radiobaudrate = config.get('GroundStation','RadioBaudRate')
        
    def read(self,param=None):
        if param == 'lat':
            return self.__lat
        if param == 'lon':
            return self.__lon
        if param == 'height':
            return self.__height
        if param == 'radio':
            return self.__radio
        if param == 'antenaport':
            return self.__antenaport
        if param == 'antenabaudrate':
            return self.__antenabaudrate
        if param == 'radioport':
            return self.__radioport
        if param == 'radiobaudrate':
            return self.__radiobaudrate
        if param == None:
            return {'lat':self.__lat,'lon':self.__lon,'height':self.__height,'radio':self.__radio,'antenaport':self.__antenaport,'antenabaudrate':self.__antenabaudrate,'radioport':self.__radioport,'radiobaudrate':self.__radiobaudrate}

class testconfig(unittest.TestCase):
    def testconfig(self):
        config = ConfigRead()
        self.assertEqual('43.134694',config.read('lat'))
        self.assertEqual('141.248194',config.read('lon'))
        self.assertEqual('50',config.read('height'))
        self.assertEqual('IC910',config.read('radio'))
        self.assertEqual('/dev/tty.USB',config.read('antenaport'))
        self.assertEqual('9600',config.read('antenabaudrate'))
        self.assertEqual('/dev/tty.USB2',config.read('radioport'))
        self.assertEqual('38400',config.read('radiobaudrate'))
        data = config.read()
        self.assertEqual('43.134694',data['lat'])
        self.assertEqual('141.248194',data['lon'])
        self.assertEqual('50',data['height'])
        self.assertEqual('IC910',data['radio'])
        self.assertEqual('/dev/tty.USB',data['antenaport'])
        self.assertEqual('9600',data['antenabaudrate'])
        self.assertEqual('/dev/tty.USB2',data['radioport'])
        self.assertEqual('38400',data['radiobaudrate'])

unittest.main()
