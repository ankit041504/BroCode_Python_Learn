# While loop in python works on the concept of iterating a statement till the
# conditional statement is True.

# While loop is preferred over for loop if there is a condition to be checked before
# iteration occurs.

# While loop also uses less memory to iterate hence the processing speed or time complexity
# of the while loop is lesser than that of for loop.

# print any table

num = int(input("enter the numer to print table : "))
i = 1

while i <= 10:   #Condition to check before entering into loop
    prod=num*i
    print(f" {num} * {i} = ",prod)
    i = i + 1

