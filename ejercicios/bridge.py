# Author: Jose Carlos Soto Barco
#description: a bridge is made


class DrawingAPIOne(object):
    """ Implementation-specific abstraction: concrete class one """
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {})".format(x, y, radius))

class DrawingAPITwo(object):
    """ Implementation-specific abstraction: concrete class one """
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class Circle(object):
    """ Implementation-independent abtraction: for example, there could be a rectangle class! """

    def __init__(self, x, y, radius, drawing_api):
        """ Initialize the necessary attributes """
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        """ Implementation-specific abstraction taken care of by another class: DrawinAPI"""
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        """ Implmentation-independent"""
        self.radius = percent

# Build the first circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw a circle
circle1.draw()

# Build the first circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# Draw a circle
circle2.draw()