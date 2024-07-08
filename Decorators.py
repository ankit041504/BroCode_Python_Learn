'''Decorators in python are used to modify and extend the proporties of existing function.

In decorators functions are used as an arguments in other function and then called inside a wrapper function.

Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without 
permanently modifying it.'''

'''Some Proporties of Python Functions

A python function is an instance of object type.
A function can be stored inside a variable.
A function can be passed as an argument to a function.
A function could be returned as a return from another function.'''


# Example - Treating a fucntion as object

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))

print('***************************************************************')

'''In the above example, we have assigned the function shout to a variable. 
This will not call the function instead it takes the function object referenced by a shout 
and creates a second name pointing to original function, yell.'''



# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout1(text): 
    return text.upper() 

def whisper1(text): 
    return text.lower() 

def greet1(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet1(shout1) 
greet1(whisper1) 


print('***************************************************************')


# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10)) 

'''create_adder is a factory function that generates adder functions.
add_15 is a specific adder function created with x set to 15.
When add_15(10) is called, it adds 15 (the fixed value of x) to 10 (the argument passed to adder), resulting in 25.'''

print('***************************************************************')


# defining a decorator

def hello_decorator(func):

    # inner1 is a Wrapper function in 
    # which the argument is called
    
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")
        
    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()







