'''A python function is used to define a set of code or functionality.
A function is only executed when it is called.
You can pass values using arguments inside a function.
In Python to define a function def keyword is used followed with the function name.
'''


def sumf(a, b):
    print("executing function body")
    c = a + b
    return c


a = int(input("enter first number"))
b = int(input("enter second number"))
print("result - ", sumf(a, b))
print("function ended")

'''
Here in this code a function named sumf is created.
a, b are the arguments used to pass value of input whose sum has to be calculated.
c is the variable which is used to store sum of arguments a and b.
In the last line sumf(a, b) is used to call the function which prints the output returned
by function.'''

'''In Python, *args and **kwargs are special syntax used to pass a variable number of
arguments to a function. They provide a flexible way to define functions that can accept
any number of arguments, which is especially useful in situations where the number of arguments
that a function needs to handle may vary.
'''

'''
*args is used to pass a variable number of non-keyworded arguments to a function. 
The arguments are passed as a tuple and can be accessed using the index notation. 
This means that you can pass any number of positional arguments to a function using *args.
'''


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(2, 3, 4))  # Output: 24

'''**kwargs is used to pass a variable number of keyworded arguments to a function. 
The arguments are passed as a dictionary and can be accessed using the key-value notation. 
This means that you can pass any number of keyword arguments to a function using **kwargs.'''


def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_values(a=1, b=2, c=3)

'''Benefits of using *args and **kwargs:

They provide a flexible way to define functions that can accept any number of arguments, 
which makes the code more modular and easier to maintain.

They allow you to write functions that can handle different types of arguments without having 
to define separate functions for each case.

They make it easier to work with third-party libraries that may use different argument conventions.

They can help you write cleaner and more concise code by reducing the need for repetitive 
boilerplate code.'''
