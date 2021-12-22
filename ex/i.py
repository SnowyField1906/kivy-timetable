import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
from kivy.lang import Builder

import math

Window.size = (450, 750)

class myGame(FloatLayout):

    def leftButton(self, *args):
        self.ids.car.direction_angle += 2

    def rightButton(self, *args):
        self.ids.car.direction_angle -= 2


class Car(Widget):
    speed = NumericProperty(20)
    direction_angle = NumericProperty(0)
    direction = ListProperty([0,1])

    def __init__(self, **kwargs):
        super(Car, self).__init__(**kwargs)
        Clock.schedule_interval(self.moveCar, 0.1)

    def moveCar(self, dt):
        self.pos = (self.x + dt * self.speed * self.direction[0], self.y + dt * self.speed * self.direction[1])


Builder.load_string('''
#:kivy 1.11.1

<FloatLayout>:
    Car: 
        id: car
        size_hint: None, None
        size: root.width * 0.15, root.height * 0.15
        pos: root.width * 0.425, root.height * 0.44
''')


class myApp(App): #name your .kv file 'my.kv'
    def build(self): # initialization method, like __init__
        game = myGame()
        return game

if __name__ == '__main__':
    myApp().run()