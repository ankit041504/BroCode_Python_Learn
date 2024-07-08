'''Polymorphism is a concept in object-oriented programming that allows objects
of different classes to be treated as if they were of the same class. It is achieved
through the use of inheritance, overriding, and method overloading.

In Python, polymorphism is supported natively, and it allows us to write code that can work
with different types of objects in a flexible and efficient way.

Here is an example of polymorphism in Python:'''


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape): #inherit
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.radius ** 2


# Function to calculate the area of any shape without knowing its specific type
def get_area(shape):
    return shape.calculate_area()


# Creating instances of the classes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Using the get_area function to calculate the area of different shapes
print(f"Area of rectangle: {get_area(rectangle)}")
print(f"Area of circle: {get_area(circle)}")