# -*- coding: utf-8 -*-

import serial


class IC910:
<<<<<<< HEAD
    def connect(self, radioport,radiobaudrate):
        self._ser=serial.Serial(port=radioport,baudrate=radiobaudrate)

    def _freqvalueparse(self,freqvalue):
        freqvalue=str(freqvalue)
        freqvalue=freqvalue.replace('.',"")
        freqvalue=(freqvalue+"000000000")[:9]
        print [freqvalue[x-1]+freqvalue[x] for x in range(len(freqvalue)-1,-1,-2)]
        return [freqvalue[x-1]+freqvalue[x] for x in range(len(freqvalue)-1,-1,-2)]

    def changefreq(self, freqvalue):
        sendcommand=""
        sendcommand+="\xFE"
        sendcommand+="\xFE"
        sendcommand+="\x00"
        sendcommand+="\x60"
        sendcommand+="\x00"

        for i in self._freqvalueparse(freqvalue):
            sendcommand+=chr(int(i,16))
        sendcommand+="\xFD"
        self._ser.write(sendcommand)

    def changemode(self):
        sendcommand=""
        sendcommand+="\xFE"
        sendcommand+="\xFE"
        sendcommand+="\x00"
        sendcommand+="\x60"
        sendcommand+="\x01"
        sendcommand+=self._data
        sendcommand+="\x01"
        sendcommand+="\xFD"
        self._ser.write(sendcommand)
        self._ser.flush()

    def changeband(self):
        if self.modeCWFM == "CW":
            subcommand = b"\x03"
        elif self.modeCWFM == "FM":
            subcommand = b"\x05"
        sendcommand = ""
        sendcommand += "\xFE"
        sendcommand += "\xFE"
        sendcommand += "\x00"
        sendcommand += self._receiveaddress
        sendcommand += "\x01"
        sendcommand += subcommand
        sendcommand += "\x01"
        sendcommand += "\xFD"
        self._ser.write(sendcommand)
        self._ser.flush()

    def getmode(self):
        sendcommand = ""
        sendcommand += b"\xFE"
        sendcommand += b"\xFE"
        sendcommand += self._receiveaddress
        sendcommand += b"\xE0"
        sendcommand += b"\x04"
        sendcommand += b"\xFD"
        self._ser.write(sendcommand)

    def close(self):
        self._ser.flush()
        self._ser.close()

class IC911(IC910):
    pass


class Radio(object):
    def _modesetparam(self, modeSubMain, modeCWFM):
        if(modeSubMain == "Sub" and modeCWFM == "FM"):
            self._radio._receiveaddress = b"\x60"
            self._radio._data = b"\x05"

        if(modeSubMain == "Main" and modeCWFM == "FM"):
            self._radio._receiveaddress = b"\x2E"
            self._radio._data = b"\xD0"

        if(modeSubMain == "Sub" and modeCWFM == "CW"):
            self._radio._receiveaddress = b"\x60"
            self._radio._data = b"\x03"

        if(modeSubMain == "Main" and modeCWFM == "CW"):
            self._radio._receiveaddress = b"\x60"
            self._radio._data = b"\xD0"

    def __init__(self, radiomodel, modeSubMain, modeCWFM):
        if radiomodel == "IC910":
            self._radio = IC910()
            self._radio.modeSubMain = modeSubMain
            self._radio.modeCWFM = modeCWFM
        if radiomodel == "IC911":
            self._radio = IC911()
            self._radio.modeSubMain = modeSubMain
            self._radio.modeCWFM = modeCWFM
        self._modesetparam(modeSubMain, modeCWFM)

    def connect(self, radioport, baudrate):
        self._radio.connect(radioport, baudrate)

    def changefreq(self, freqvalue):
        self._radio.changefreq(freqvalue)

    def getfreq(self):
        return self._radio.getfreq()

    def changemode(self, modeSubMain, modeCWFM):
        self._radio.modeSubMain = modeSubMain
        self._radio.modeCWFM = modeCWFM
        self._modesetparam(modeSubMain, modeCWFM)
        self._radio.changemode()

    def getmode(self):
        return self._radio.getmode()

    def close(self):
        return self._radio.close()
