# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock

class SampleWidget(Button):
    
    pass

class MyApp(App):

    def build(self):
        root = SampleWidget()

if __name__ == '__main__':
    MyApp().run()
