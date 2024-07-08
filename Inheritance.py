'''Inheritance in python is a way of assigning properties of one class to another.

Inheritance works on the concept of Parent and child class. Where in child class inherits
the properties of the Parent class.

Inheritance allows us to share the methods across classes. Which increases the reusability of
the code.'''


class Calculator:
    def sum1(a, b):
        return a + b

    def subs(a, b):
        return a - b

    def multi(a, b):
        return a * b

    def divi(a, b):
        return a / b


class ComplexCalculator(Calculator):
    def avg(sumo, n):
        return sumo / n


a = int(input("enter first number : "))
b = int(input("enter second number : "))

sumo = ComplexCalculator.sum1(a, b)
output = ComplexCalculator.avg(sumo, 2)
print(output)

'''Types of Inheritance in Python
--> Single Level Inheritance
--> Multi Level Inheritance
--> Multiple Inheritance
--> Hierarchical Inheritance
--> Hybrid Inheritance'''

#--> Single Level Inheritance

'''In this type of inheritance there is one parent component which is inherited by one child
component. Hence it is known as single level inheritance'''

class Parent:
    pass

class Child(Parent):
    pass


#--> Multi Level Inheritance

'''
In multilevel inheritance one parent class is inherited by one child class. Then the same 
child class is inherited by another child class.'''

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Child1):
    pass

# --> Multiple Inheritance

'''
When a child class inherits more than one parent classes it is known as Multiple Inheritacne.
'''

class Parent:
    pass

class Parent2:
    pass

class Child(Parent, Parent2):
    pass

#--> Hierarchical Inheritance

'''When One parent class is inherited between multiple child classes it is known as 
herarichal inheritance.'''

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

#--> Hybrid Inheritance

'''Inheritance which is the mixture of one or more types of inheritance is known 
as Hybrid Inheritance.'''

