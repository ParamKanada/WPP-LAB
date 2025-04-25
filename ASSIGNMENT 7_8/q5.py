# Shape

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width = {self.width} , height = {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius = {self.radius})"

a = int(input("Enter Width for Rectangle = \n"))
b = int(input("Enter Height for Rectangle = \n"))
rec = Rectangle(a,b)

c = int(input("Enter radius for Circle = \n"))
cir = Circle(c)

print("\nDisplay...\n")

print(f"Area of Rectangle = {rec.area()} , Perimeter of Rectangle = {rec.perimeter()}\n\n")
print(f"Area of Circle = {cir.area()} , Perimeter of Circle = {cir.perimeter()}\n")