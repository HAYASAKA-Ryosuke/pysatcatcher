# -*- coding: utf-8 -*-
import unittest
import serial

class IC911:

    def connect(self, radioport):
        print "IC911"
        #self._ser=serial.Serial(radioport,38400)

    def chengefreq(self,freqvalue):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="05"
        subcommand="00"
        data = str(freqvalue)
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def getfreq(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="03"
        subcommand="00"
        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def changemode(self,mode):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="06"
        subcommand=""
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

        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def getmode(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="04"
        subcommand="00"
        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

class IC910:

    def connect(self, radioport):
        print radioport
        #self._ser=serial.Serial(radioport,38400)

    def chengefreq(self,freqvalue):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="05"
        subcommand="00"
        data = str(freqvalue)
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def getfreq(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="03"
        subcommand="00"
        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def changemode(self,mode):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="06"
        subcommand=""
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

        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

    def getmode(self):
        priansumble = "FE"*2
        receiveaddress = "60"
        sendeaddress = "E0"
        command="04"
        subcommand="00"
        data=""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        self._ser.sendvalue(sendcommand)

class Radio(object):
    def __init__(self,radiomodel):
        if radiomodel == "IC910":
            self._radio = IC910()
        if radiomodel == "IC911":
            self._radio = IC911()

    def connect(self,radioport):
        self._radio.connect(radioport)

class testradio(unittest.TestCase):

    def testradioconnect(self):
        radio = Radio("IC910")
        radio.connect("connect")

unittest.main()
