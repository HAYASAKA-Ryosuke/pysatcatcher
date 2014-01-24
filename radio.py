# -*- coding: utf-8 -*-
import unittest
import serial


class IC911:

    def connect(self, radioport):
        print "IC911"
        #self._ser=serial.Serial(radioport,38400)

    def chengefreq(self, freqvalue):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "05"
        subcommand = "00"
        data = str(freqvalue)
        postansumble = "FD"
        sendcommand = priansumble + receiveaddress + sendeaddress + command + subcommand + data + postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def getfreq(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "03"
        subcommand = "00"
        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def chengemode(self, mode):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "06"
        subcommand = ""
        if mode == "LSB":
            subcommand = "00"
        elif mode == "USB":
            subcommand = "01"
        elif mode == "CW":
            subcommand = "03"
        elif mode == "FM":
            subcommand = "04"
        else:
            subcommand = "04"

        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def getmode(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "04"
        subcommand = "00"
        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)


class IC910:

    def connect(self, radioport):
        print radioport
        #self._ser=serial.Serial(radioport,38400)

    def chengefreq(self, freqvalue):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "05"
        subcommand = "00"
        data = str(freqvalue)
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def getfreq(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "03"
        subcommand = "00"
        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def chengemode(self, mode):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "06"
        subcommand = ""
        if mode == "LSB":
            subcommand = "00"
        elif mode == "USB":
            subcommand = "01"
        elif mode == "CW":
            subcommand = "03"
        elif mode == "FM":
            subcommand = "04"
        else:
            subcommand = "04"

        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def getmode(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command = "04"
        subcommand = "00"
        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #self._ser.sendvalue(sendcommand)


class Radio(object):
    def __init__(self, radiomodel):
        if radiomodel == "IC910":
            self._radio = IC910()
        if radiomodel == "IC911":
            self._radio = IC911()

    def connect(self, radioport):
        self._radio.connect(radioport)

    def chengefreq(self, freqvalue):
        self._radio.chengefreq(freqvalue)

    def getfreq(self):
        return self._radio.getfreq()

    def chengemode(self, mode):
        self._radio.chengemode(mode)

    def getmode(self):
        return self._radio.getmode()


class testradio(unittest.TestCase):

    def testradioIC910(self):
        radio = Radio("IC910")
        radio.connect("connect")
        print radio.getfreq()
        print radio.getmode()
        radio.chengefreq(430.36)
        radio.chengemode("FM")

    def testradioIC911(self):
        radio = Radio("IC911")
        radio.connect("connect")
        print radio.getfreq()
        print radio.getmode()
        radio.chengefreq(430.36)
        radio.chengemode("FM")


unittest.main()
