'''Python classes provide the functionality to bundle data and functionality together.

In python creating a new class creates a new object. Following the concept that everything
in python is an object.

Python classes could also have methods to update their states and functionalities. In general,
python functions are used as methods.

To define a class in python you just have to write the class keyword followed by the class
name (class Calculator:).'''


class Calculator:  # class defination
    def sum(a, b):  # method1 to calculate sum of two numbers
        return a + b

    def subs(a, b):  # method2 to calculate subs traction of two numbers
        return a - b

    def multi(a, b):
        return a * b

    def divi(a, b):
        return a / b


a = 10
b = 50
out1 = Calculator.sum(a, b)  # object1
print(out1)

out2 = Calculator.multi(a, b)  # object2
print(out2)

out3 = Calculator.divi(a, b)  # object3
print(out3)

out4 = Calculator.subs(a, b)  # object4
print(out4)
