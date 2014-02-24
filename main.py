# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import Orbitcalc
import antenna
import config
import radio
import threading

class SampleWidget(Widget):
    labelAOS = ObjectProperty(None)
    labelLOS = ObjectProperty(None)
    labelAZ = ObjectProperty(None)
    labelEL = ObjectProperty(None)
    labelfreq = ObjectProperty(None)
    labelstatus = ObjectProperty(None)
    buttonOperation = ObjectProperty(None)
    textTLE = ObjectProperty(None)
    textfreq = ObjectProperty(None)

    def buttonOperation_clicked(self,src):
        if self.buttonOperation.text=="operation":
            self.buttonOperation.text="close"
            self.labelAOS.text="AOS:00:00:00"
        else:
            self.buttonOperation.text="operation"
            self.labelAOS.text="AOS:00:00:00"

class MyApp(App):
    def callback_operation(self,dt):
        if self.root.buttonOperation.text=="close":
            tle1=self.root.textTLE.text.splitlines()[0]
            tle2=self.root.textTLE.text.splitlines()[1]
            freq = self.root.textfreq.text
            orbitinfo = Orbitcalc.Orbitcalc(self.gslat,self.gslon,self.gsheight)
            orbitinfo.SatInfo('sat',tle1,tle2,freq)
            satlat,satlon,satfreq,satrisetime,satsettime,satmaxtime = orbitinfo.CalcObserve()
            print satlon
            print satfreq
            #self.labelAOS.text="AOS:"+str(satrisetime)
            self.root.labelAZ.text="AZ:"+"%0.3f" % satlat
            self.root.labelEL.text="EL:"+"%0.3f" % satlon
            self.root.labelfreq.text="Freq:"+"%0.5f" % satfreq
            if satlon>=0.0:
                self.root.labelstatus.text="Insight"
                self.root.labelstatus.color=[0,1,0,1]
            else:
                self.root.labelstatus.text="Outsight"
                self.root.labelstatus.color=[1,0,0,1]
                self.root.labelAOS.text="AOS:"+str(satrisetime.strftime("%H:%M:%S"))
                self.root.labelLOS.text="LOS:"+str(satsettime.strftime("%H:%M:%S"))
            self.ic910.changemode("Sub","CW")
            print satfreq
            self.ic910.changefreq("%0.5f" % satfreq)
            self.ant.moveazel(satlat,satlon)
            #self.ant.recieve()
            
    def build(self):
        self.root = SampleWidget()
        self.root.buttonOperation.bind(on_press=self.root.buttonOperation_clicked)
        Clock.schedule_interval(self.callback_operation,1)
        self.conf = config.ConfigRead().read()
        self.gslat=self.conf['lat']
        self.gslon=self.conf['lon']
        self.gsantenna=self.conf['antenna']
        self.gsheight=self.conf['height']
        self.gsradio=self.conf['radio']
        self.gsradioport=self.conf['radioport']
        self.gsradiobaudrate=self.conf['radiobaudrate']
        self.gsantennaport=self.conf['antennaport']
        self.gsantennabaudrate=self.conf['antennabaudrate']
        self.ant=antenna.Antenna(self.gsantenna)
        self.ant.connect(self.gsantennaport)
        self.ic910=radio.Radio(self.gsradio,"Sub","CW")
        self.ic910.connect(self.gsradioport)
        return self.root


if __name__ == '__main__':
    MyApp().run()
