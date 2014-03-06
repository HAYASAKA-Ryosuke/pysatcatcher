# -*- coding: utf-8 -*-

import ConfigParser


class ConfigRead(object):
    __lat = ''
    __lon = ''
    __height = ''
    __radio = ''
    __antennaport = ''
    __antennabaudrate = ''
    __radioport = ''
    __radiobaudrate = ''

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read('config.ini')
        self.__lat = config.get('GroundStation', 'Lat')
        self.__lon = config.get('GroundStation', 'Lon')
        self.__height = config.get('GroundStation', 'Height')
        self.__radio = config.get('GroundStation', 'Radio')
        self.__antenna = config.get('GroundStation', 'Antenna')
        self.__antennaport = config.get('GroundStation', 'AntenaPort')
        self.__antennabaudrate = config.get('GroundStation', 'AntenaBaudRate')
        self.__radioport = config.get('GroundStation', 'RadioPort')
        self.__radiobaudrate = config.get('GroundStation', 'RadioBaudRate')

    def read(self, param=None):
        if param == 'lat':
            return self.__lat
        if param == 'lon':
            return self.__lon
        if param == 'height':
            return self.__height
        if param == 'antenna':
            return self.__antenna
        if param == 'radio':
            return self.__radio
        if param == 'antennaport':
            return self.__antennaport
        if param == 'antennabaudrate':
            return self.__antennabaudrate
        if param == 'radioport':
            return self.__radioport
        if param == 'radiobaudrate':
            return self.__radiobaudrate
        if param is None:
            return {'lat': self.__lat, 'lon': self.__lon, 'height': self.__height, 'antenna': self.__antenna,  'radio': self.__radio, 'antennaport': self.__antennaport, 'antennabaudrate': self.__antennabaudrate, 'radioport': self.__radioport, 'radiobaudrate': self.__radiobaudrate}
