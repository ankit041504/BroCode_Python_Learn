'''Python Generators are the most easiest way of creating iterators.
Simply speaking, a generator is a function that returns an object(iterator) that we can iterate over(one value at a time).'''

'''To create a generator you need to replace return statement from normal function with a yield statement.
The difference between yield and return statement is that , return statement stops or terminates a function entirely.
While yield statement parses the fucntion saving all its states and later continues from there on successive calls.'''


# A simple generator function
def my_gen():
    n = 1
    print('This is yield printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is yield printed second')
    yield n

    n += 1
    print('This is yield printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)



list1 = [0, 1, 2]
iter1 = list1.__iter__()

#This will convert an iterable to iterator.

print(iter1.__next__())


def my_gen2():
    n='1'
    print('This is return printed first')
    # Generator function contains yield statements
    return n

    n += 1
    print('This is return printed second')
    return n

    n += 1
    print('This is return printed at last')
    return n



# Using for loop
for item in my_gen2():
    print(item)