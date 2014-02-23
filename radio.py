# -*- coding: utf-8 -*-

import serial

class IC910:
    def connect(self, radioport):
        self._ser=serial.Serial(port=radioport,baudrate=19200)
        #self._ser=serial.serial_for_url(radioport,do_not_open=True)
        print radioport
        #self._ser=serial.Serial(port=radioport,baudrate=19200,xonxoff=True,rtscts=True)
        #self._ser=serial.serial_for_url(radioport,do_not_open=True)

    def _freqvalueparse(self,freqvalue):
        freqvalue=str(freqvalue)
        freqvalue=freqvalue.replace('.',"")
        freqvalue=(freqvalue+"000000000")[:9]
        print [freqvalue[x-1]+freqvalue[x] for x in range(len(freqvalue)-1,-1,-2)]
        return [freqvalue[x-1]+freqvalue[x] for x in range(len(freqvalue)-1,-1,-2)]


    #def changefreq(self, freqvalue):
    #    #sendcommand=[]
    #    #sendcommand.append(bytes(0xFE))
    #    #sendcommand.append(bytes(0xFE))
    #    ##あとでFMな??2E
    #    #sendcommand.append(bytes(0x00))
    #    ##sendcommand.append(self._receiveaddress)
    #    #sendcommand.append(bytes(0x60))
    #    #sendcommand.append(bytes(0x00))
    #    #sendcommand.append(bytes(0x00))
    #    #sendcommand.append(bytes(0xE0))
    #    #sendcommand.append(bytes(0x05))
    #    print freqvalue
    #    return ["{0:02d}".format(int(freqvalue[x-1]+freqvalue[x])) for x in range(len(freqvalue)-1,-1,-2)]


    def changefreq(self, freqvalue):
        #sendcommand=[]
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(bytes(0xFE))
        ##あとでFMな??2E
        #sendcommand.append(bytes(0x00))
        #sendcommand.append(self._receiveaddress)
        #sendcommand.append(bytes(0x00))
        ##437.485900 なら [0x00 0x59 0x48 0x37 0x04]
        ##data = str(freqvalue)
        ##[data.append(x) for x in freqvalue[-1:]
        #freqvalue=str(freqvalue)
        #freqvalue=freqvalue.replace('.',"")
        #freqvalue=(freqvalue+"000000000")[:9]
        sendcommand=""
        sendcommand+="\xFE"
        sendcommand+="\xFE"
        sendcommand+="\x00"
        sendcommand+="\x60"
        sendcommand+="\x00"

        #sendcommand+="\x00"
        #sendcommand+="\x10"
        #sendcommand+="\x25"
        #sendcommand+="\x38"
        #sendcommand+="\x04"

        #sendcommand.extend(self._freqvalueparse(freqvalue))
        #sendcommand+="".join(self._freqvalueparse(freqvalue))
        for i in self._freqvalueparse(freqvalue):
            sendcommand+=chr(int(i,16))
        #sendcommand.extend([freqvalue[x]+freqvalue[x-1] for x in range(len(freqvalue)-1,-1,-2)])
        #print [freqvalue[x]+freqvalue[x-1] for x in range(len(freqvalue)-1,-1,-2)]
        sendcommand+="\xFD"
        #data = str("0059483704")
        #sendcommand.append(bytes(0xFD))
        #sendcommand =[priansumble[0],priansumble[1],receiveaddress,sendeaddress,command,data,postansumble]
        print "changefreq"
        #print map(str,sendcommand)
        #print sendcommad
        print sendcommand
        #for data in sendcommand:
        #    self._ser.write(data)
        #    print '%x' % int(data)
        #self._ser.flush()
        self._ser.write(sendcommand)
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
        self._ser.write(sendcommand)

    def changemode(self):
        #sendcommand=[]
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(self._receiveaddress)
        #sendcommand.append(bytes(0xE0))
        #sendcommand.append(bytes(0x07))
        #sendcommand.append(self._data)
        #sendcommand.append(bytes(0xFD))
        sendcommand=""
        sendcommand+="\xFE"
        sendcommand+="\xFE"
        sendcommand+="\x00"
        sendcommand+="\x60"
        #sendcommand+=self._receiveaddress
        sendcommand+="\x01"
        #sendcommand+="\x05"
        sendcommand+=self._data
        sendcommand+="\x01"
        sendcommand+="\xFD"
        print "changeSubMain"
        #sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        print sendcommand
        #for data in sendcommand:
        #    self._ser.write(data)
        #    print '%x' % int(data)
        self._ser.write(sendcommand)
        #self.changeband()
        self._ser.flush()

    def changeband(self):
        #sendcommand=[]
        #if self.modeCWFM == "CW":
        #    subcommand = bytes(0x03)
        #elif self.modeCWFM == "FM":
        #    subcommand = bytes(0x05)
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(self._receiveaddress)
        #sendcommand.append(bytes(0xE0))
        #sendcommand.append(bytes(0x01))
        #sendcommand.append(subcommand)
        #sendcommand.append(bytes(0xFD))
        #freqmodecommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        if self.modeCWFM == "CW":
            subcommand = b"\x03"
        elif self.modeCWFM == "FM":
            subcommand = b"\x05"
        sendcommand=""
        sendcommand+="\xFE"
        sendcommand+="\xFE"
        sendcommand+="\x00"
        sendcommand+=self._receiveaddress
        sendcommand+="\x01"
        sendcommand+=subcommand
        sendcommand+="\x01"
        sendcommand+="\xFD"
        print "changeFMCW"
        print sendcommand
        #for data in sendcommand:
        #    self._ser.write(data)
        #    print '%x' % int(data)
        self._ser.write(sendcommand)
        self._ser.flush()
        #self._ser.sendvalue(sendcommand)
        #self.changeband()

    def getmode(self):
        #sendcommand=[]
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(bytes(0xFE))
        #sendcommand.append(self._receiveaddress)
        #sendcommand.append(bytes(0xE0))
        #sendcommand.append(bytes(0x04))
        #sendcommand.append(bytes(0xFD))
        #sendcommand.append("\r")
        #sendcommand = priansumble+receiveaddress+sendeaddress+command+subcommand+data+postansumble
        sendcommand=""
        sendcommand+=b"\xFE"
        sendcommand+=b"\xFE"
        sendcommand+=self._receiveaddress
        sendcommand+=b"\xE0"
        sendcommand+=b"\x04"
        sendcommand+=b"\xFD"
        print "getfreq"
        print sendcommand
        self._ser.write(sendcommand)
        #self._ser.sendvalue(sendcommand)
    def close(self):
        self._ser.flush()
        self._ser.close()
        #self._ser.close()

class IC911(IC910):
    pass

class Radio(object):
    def _modesetparam(self,modeSubMain,modeCWFM):
        if(modeSubMain=="Sub" and modeCWFM=="FM"):
            #self._radio._receiveaddress=bytes(0x2E)
            #self._radio._data=bytes(0xD1)
            self._radio._receiveaddress=b"\x60"
            self._radio._data=b"\x05"
            #self._radio._receiveaddress=b"\x60"
            #self._radio._data=b"\xD1"
        if(modeSubMain=="Main" and modeCWFM=="FM"):
            self._radio._receiveaddress=bytes(0x2E)
            self._radio._data=bytes(0xD0)
            print "ok"
        if(modeSubMain=="Sub" and modeCWFM=="CW"):
            #self._radio._receiveaddress=bytes(0x60)
            #self._radio._data=bytes(0xD1)
            self._radio._receiveaddress=b"\x60"
            self._radio._data=b"\x03"
            #self._radio._receiveaddress=b"\x2E"
            #self._radio._data=b"\xD1"
        if(modeSubMain=="Main" and modeCWFM=="CW"):
            self._radio._receiveaddress=bytes(0x60)
            self._radio._data=bytes(0xD0)
            print "ok"

    def __init__(self, radiomodel,modeSubMain,modeCWFM):
        if radiomodel == "IC910":
            self._radio = IC910()
            self._radio.modeSubMain=modeSubMain
            self._radio.modeCWFM=modeCWFM
        if radiomodel == "IC911":
            self._radio = IC911()
            self._radio.modeSubMain=modeSubMain
            self._radio.modeCWFM=modeCWFM


        self._modesetparam(modeSubMain,modeCWFM)

    def connect(self, radioport):
        self._radio.connect(radioport)

    def changefreq(self, freqvalue):
        self._radio.changefreq(freqvalue)

    def getfreq(self):
        return self._radio.getfreq()

    def changemode(self, modeSubMain,modeCWFM):
        self._radio.modeSubMain=modeSubMain
        self._radio.modeCWFM=modeCWFM
        self._modesetparam(modeSubMain,modeCWFM)
        self._radio.changemode()

    def getmode(self):
        return self._radio.getmode()

    def close(self):
        return self._radio.close()


#class testradio(unittest.TestCase):
#
#    def testradioIC910(self):
#        radio = Radio("IC910","Sub","CW")
#        radio.connect("/dev/ttyUSB0")
#        #print radio.getfreq()
#        #radio.getmode()
#        radio.changefreq(437.38590)
#        #print "Sub FM"
#        #radio.chengemode("Sub","FM")
#        print "Sub CW"
#        radio.changemode("Sub","FM")
#        #print "Main FM"
#        #radio.chengemode("Main","FM")
#        #print "Main CW"
#        #radio.chengemode("Main","CW")
#        radio.close()
#
#    #def testradioIC911(self):
#    #    radio = Radio("IC910","Sub","CW")
#    #    radio.connect("connect")
#    #    #print radio.getfreq()
#    #    #radio.getmode()
#    #    radio.chengefreq(437.4801)
#    #    print "Sub FM"
#    #    radio.chengemode("Sub","FM")
#    #    print "Sub CW"
#    #    radio.chengemode("Sub","CW")
#    #    print "Main FM"
#    #    radio.chengemode("Main","FM")
#    #    print "Main CW"
#    #    radio.chengemode("Main","CW")
#    #    radio.close()
#
#unittest.main()
