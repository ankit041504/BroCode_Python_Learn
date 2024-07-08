'''Abstraction is a fundamental concept in object-oriented programming that allows a
developer to focus on the essential features of an object, while ignoring the details
of its implementation. In Python, abstraction is achieved by using abstract classes and abstract methods.

An abstract class is a class that cannot be instantiated, and is meant to be subclassed by
other classes. It is used to define a common interface for a group of related classes, without
specifying the implementation details.

An abstract class is declared using the abc module in Python,
and is defined by inheriting from the ABC class.'''

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50


'''In this example, the Shape class is an abstract class that defines the 
area() method as an abstract method using the @abstractmethod decorator.
This means that any subclass of Shape must implement the area() method.
The Rectangle class is a subclass of Shape that implements the area() 
method to calculate the area of a rectangle.'''