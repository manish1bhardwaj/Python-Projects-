# 7. Problem: Shape Area Calculator 
# Description: Implement a Shape class with methods to calculate the area for different 
# shapes like square, rectangle, and circle.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by the subclass")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example Usage
square = Square(4)
print(f"Area of Square: {square.area()}")

rectangle = Rectangle(4, 5)
print(f"Area of Rectangle: {rectangle.area()}")

circle = Circle(3)
print(f"Area of Circle: {circle.area():.2f}")