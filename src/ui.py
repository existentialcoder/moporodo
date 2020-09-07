# Color schemas - https://www.w3schools.com/colors/colors_monochromatic.asp
from kivy.config import Config
from kivy.app import App
from kivy.graphics import Rectangle, Color, PushMatrix, PopMatrix
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty, NumericProperty

import os
import json
import random
import kivy
kivy.require('1.10.0')

Config.set('kivy', 'window_icon', './assets/logo.png')
Config.set('kivy', 'exit_on_escape', 1)

constant_file = open(os.getcwd() + '/src/data/constants.json', 'r')
CONSTANTS = json.load(constant_file)
  
# class in which we are creating the canvas 
class PomodoroUI(Widget):
    time_str = StringProperty('00:00')
    def get_random_colors(self):
        rand_index = random.randint(0, len(CONSTANTS['COLOR_SCHEMAS']) - 1)
        colors = CONSTANTS['COLOR_SCHEMAS'][rand_index]
        return colors

    def __init__(self, **kwargs):

        super(PomodoroUI, self).__init__(**kwargs)
        self.one_pomodoro_time = int(CONSTANTS['POMODORO_UNIT'] * CONSTANTS['ONE_MINUTE'])
        self.rect_colors = CONSTANTS['COLOR_SCHEMAS'][0]
        self.app = App.get_running_app()

        with self.canvas:
            rand_colors = self.get_random_colors()
            Color(*kivy.utils.get_color_from_hex(self.rect_colors[1]))
            self.rect = Rectangle(pos=self.center, size=(
                self.width / 2., self.height / 2.))

            Color(*kivy.utils.get_color_from_hex(self.rect_colors[0]))
            self.rect2 = Rectangle(pos=self.center, size=(
                self.width / 8., self.height / 8.))

            self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.rect2.pos = (self.center_x-(self.width/3.),
                          self.center_y-(self.height/3.))
        self.rect2.size = (self.width / 1.5, self.height / 1.5)
  
# Create the App Class 
class PomodoroApp(App): 
    def build(self): 
        return PomodoroUI()
