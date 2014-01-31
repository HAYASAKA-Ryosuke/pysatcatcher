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
        sendeaddress = "E0"
        command = "01"
        subcommand = ""
        if mode == "LSB":
            subcommand = "00"
        elif mode == "USB":
            subcommand = "01"
        elif mode == "CW":
            receiveaddress = "60"
            subcommand = "03"
        elif mode == "FM":
            subcommand = "04"
            receiveaddress = "2E"

        data = ""
        postansumble = "FD"
        sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print "changemode"
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
        print "getmode"
        print sendcommand
        #self._ser.sendvalue(sendcommand)


class IC910:
    _receiveaddress=bytes(0x00)
    _data=bytes(0x00)

    def connect(self, radioport):
        print radioport
        #self._ser=serial.Serial(radioport,38400)

    def changeSUB(self):
        sendcommand=[]
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0x60))
        sendcommand.append(bytes(0xE0))
        sendcommand.append(bytes(0x07))
        sendcommand.append(bytes(0xD1))
        sendcommand.append(bytes(0xFD))
        #sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+postansumble
        print sendcommand

    def chengefreq(self, freqvalue):
        sendcommand=[]
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0xFE))
        #あとでFMな??2E
        sendcommand.append(self._receiveaddress)
        sendcommand.append(bytes(0x60))
        sendcommand.append(bytes(0xE0))
        sendcommand.append(bytes(0x05))
        #437.485900 なら [0x00 0x59 0x48 0x37 0x04]
        #data = str(freqvalue)
        #[data.append(x) for x in freqvalue[-1:]
        freqvalue=str(freqvalue)
        freqvalue=freqvalue.replace('.',"")
        freqvalue=(freqvalue+"000000000")[:9]
        sendcommand.extend([freqvalue[x]+freqvalue[x-1] for x in range(len(freqvalue)-1,-1,-2)])
        print [freqvalue[x]+freqvalue[x-1] for x in range(len(freqvalue)-1,-1,-2)]
        #data = str("0059483704")
        sendcommand.append(bytes(0xFD))
        #sendcommand =[priansumble[0],priansumble[1],receiveaddress,sendeaddress,command,data,postansumble]
        print "changefreq"
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def getfreq(self):
        sendcommand=[]
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0xFE))
        sendcommand.append(self._receiveaddress)
        sendcommand.append(bytes(0xE0))
        sendcommand.append(bytes(0x03))
        sendcommand.append(bytes(0xFD))
        print "getfreq"
        print sendcommand
        #self._ser.sendvalue(sendcommand)

    def changeband(self):
        sendcommand=[]
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0xFE))
        sendcommand.append(self._receiveaddress)
        sendcommand.append(bytes(0xE0))
        sendcommand.append(bytes(0x07))
        sendcommand.append(self._data)
        sendcommand.append(bytes(0xFD))
        #priansumble="FE"*2
        #sendeaddress=""
        #command="E0"
        #sendcommand.append(bytes(0x07))
        #if(mode=="Sub" and freqmode=="FM"):
        #    receiveaddress="60"
        #    data="D1"
        #if(mode=="Main" and freqmode=="FM"):
        #    receiveaddress="60"
        #    data="D0"
        #if(mode=="Sub" and freqmode=="CW"):
        #    receiveaddress="2E"
        #    data="D1"
        #if(mode=="Main" and freqmode=="CW"):
        #    receiveaddress="2E"
        #    data="D0"

        #postansumble="FD"
        print "changeSubMain"
        #sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand

    def chengemode(self):
        sendcommand=[]
        if self.modeCWFM == "CW":
            subcommand = bytes(0x03)
        elif self.modeCWFM == "FM":
            subcommand = bytes(0x05)
        sendcommand.append(bytes(0xFE))
        sendcommand.append(bytes(0xFE))
        sendcommand.append(self._receiveaddress)
        sendcommand.append(bytes(0xE0))
        sendcommand.append(bytes(0x01))
        sendcommand.append(subcommand)
        sendcommand.append(bytes(0xFD))
        #freqmodecommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print "changeFMCW"
        print sendcommand
        #self._ser.sendvalue(sendcommand)
        self.changeband()

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
    def close(self):
        pass
        #self._ser.close()


class Radio(object):
    def __init__(self, radiomodel,modeSubMain,modeCWFM):
        if radiomodel == "IC910":
            self._radio = IC910()
            self._radio.modeSubMain=modeSubMain
            self._radio.modeCWFM=modeCWFM
        if radiomodel == "IC911":
            self._radio = IC911()
            self._radio.modeSubMain=modeSubMain
            self._radio.modeCWFM=modeCWFM
        if(modeSubMain=="Sub" and modeCWFM=="FM"):
            self._radio._receiveaddress=bytes(0x60)
            self._radio._data=bytes(0xD1)
        if(modeSubMain=="Main" and modeCWFM=="FM"):
            self._radio._receiveaddress=bytes(0x60)
            self._radio._data=bytes(0xD0)
        if(modeSubMain=="Sub" and modeCWFM=="CW"):
            self._radio._receiveaddress=bytes(0x2E)
            self._radio._data=bytes(0xD1)
        if(modeSubMain=="Main" and modeCWFM=="CW"):
            self._radio._receiveaddress=bytes(0x2E)
            self._radio._data=bytes(0xD0)

    def connect(self, radioport):
        self._radio.connect(radioport)

    def chengefreq(self, freqvalue):
        self._radio.chengefreq(freqvalue)

    def getfreq(self):
        return self._radio.getfreq()

    def chengemode(self, modeSubMain,modeCWFM):
        self._radio.modeSubMain=modeSubMain
        self._radio.modeCWFM=modeCWFM
        if(modeSubMain=="Sub" and modeCWFM=="FM"):
            self._radio._receiveaddress=bytes(0x60)
            self._radio._data=bytes(0xD1)
        if(modeSubMain=="Main" and modeCWFM=="FM"):
            self._radio._receiveaddress=bytes(0x60)
            self._radio._data=bytes(0xD0)
        if(modeSubMain=="Sub" and modeCWFM=="CW"):
            self._radio._receiveaddress=bytes(0x2E)
            self._radio._data=bytes(0xD1)
        if(modeSubMain=="Main" and modeCWFM=="CW"):
            self._radio._receiveaddress=bytes(0x2E)
            self._radio._data=bytes(0xD0)
        self._radio.chengemode()

    def getmode(self):
        return self._radio.getmode()


class testradio(unittest.TestCase):

    def testradioIC910(self):
        radio = Radio("IC910","Sub","CW")
        radio.connect("connect")
        #print radio.getfreq()
        #radio.getmode()
        radio.chengefreq(437.4801)
        print "Sub FM"
        radio.chengemode("Sub","FM")
        print "Sub CW"
        radio.chengemode("Sub","CW")
        print "Main FM"
        radio.chengemode("Main","FM")
        print "Main CW"
        radio.chengemode("Main","CW")

    #def testradioIC911(self):
    #    radio = Radio("IC911")
    #    radio.connect("connect")
    #    print radio.getfreq()
    #    radio.chengefreq(430.36)
    #    radio.chengemode("FM")


unittest.main()
