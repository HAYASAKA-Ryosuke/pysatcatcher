# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SampleWidget(Widget):
    labelAOS = ObjectProperty(None)
    labelLOS = ObjectProperty(None)
    labelAZ = ObjectProperty(None)
    labelEL = ObjectProperty(None)
    labelstatus = ObjectProperty(None)
    buttonOperation = ObjectProperty(None)
    def printvalue(self):
        print self.buttonOperation.text
        print self.labelAZ.text

class MyApp(App):

    def build(self):
        root = SampleWidget()
        root.printvalue()
        return root

if __name__ == '__main__':
    MyApp().run()
