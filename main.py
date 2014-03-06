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
    spinfreqmode = ObjectProperty(None)


class MyApp(App):

    def buttonOperation_clicked(self, src):
        if self.root.buttonOperation.text == "operation":
            self.root.buttonOperation.text = "close"
        else:
            self.root.buttonOperation.text = "operation"

    def insight_outsight(self, satlon, risetime, settime):
        if satlon >= 0.0:
            self.root.labelstatus.text = "Insight"
            self.root.labelstatus.color = [0, 1, 0, 1]
        else:
            self.root.labelstatus.text = "Outsight"
            self.root.labelstatus.color = [1, 0, 0, 1]
            self.root.labelAOS.text = "AOS:"+str(risetime.strftime("%H:%M:%S"))
            self.root.labelLOS.text = "LOS:"+str(settime.strftime("%H:%M:%S"))

    def callback_operation(self, dt):
        if self.root.buttonOperation.text == "close":
            tle1 = self.root.textTLE.text.splitlines()[0]
            tle2 = self.root.textTLE.text.splitlines()[1]
            freq = self.root.textfreq.text
            orbitinfo = Orbitcalc.Orbitcalc(self.gslat, self.gslon, self.gsheight)
            orbitinfo.SatInfo('sat', tle1, tle2, freq)
            satlat, satlon, satfreq, satrisetime, satsettime, satmaxtime = orbitinfo.CalcObserve()
            print satlon
            print satfreq

            self.root.labelAZ.text = "AZ:"+"%0.3f" % satlat
            self.root.labelEL.text = "EL:"+"%0.3f" % satlon
            self.root.labelfreq.text = "Freq:"+"%0.5f" % satfreq
            self.insight_outsight(satlon, satrisetime, satsettime)

            self.ic910.changefreq("%0.5f" % satfreq)
            self.ant.moveazel(satlat, satlon)
            #self.ant.recieve()

    def spinchanged(self, src, value):
            if value == "FM":
                self.ic910.changemode("Sub", "FM")
            else:
                self.ic910.changemode("Sub", "CW")

    def build(self):
        self.root = SampleWidget()
        self.root.buttonOperation.bind(on_press=self.buttonOperation_clicked)
        Clock.schedule_interval(self.callback_operation, 1)
        self.root.spinfreqmode.bind(text=self.spinchanged)

        self.conf = config.ConfigRead().read()
        self.gslat = self.conf['lat']
        self.gslon = self.conf['lon']
        self.gsantenna = self.conf['antenna']
        self.gsheight = self.conf['height']
        self.gsradio = self.conf['radio']
        self.gsradioport = self.conf['radioport']
        self.gsradiobaudrate = self.conf['radiobaudrate']
        self.gsantennaport = self.conf['antennaport']
        self.gsantennabaudrate = self.conf['antennabaudrate']
        self.ant = antenna.Antenna(self.gsantenna, self.gsantennabaudrate)
        self.ant.connect(self.gsantennaport)
        self.ic910 = radio.Radio(self.gsradio, "Sub", "CW")
        self.ic910.connect(self.gsradioport, self.gsradiobaudrate)
        return self.root


if __name__ == '__main__':
    MyApp().run()
