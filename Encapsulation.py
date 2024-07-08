'''In Python, encapsulation can be achieved by using access modifiers, which control the visibility
of the class attributes and methods. There are three types of access modifiers in Python:'''

'''--> Public: Public members are accessible from anywhere in the program. In Python, all attributes and 
methods are public by default, and their names do not have any prefix or suffix.

--> Protected: Protected members are accessible only within the class and its subclasses. In Python, 
protected members are indicated by a single underscore (_) prefix to the attribute or method name.

--> Private: Private members are accessible only within the class. In Python, private members are 
indicated by a double underscore (__) prefix to the attribute or method name. However, the private 
members can still be accessed from outside the class by using a special syntax, which is known as 
name mangling.'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())

'''
In this example, the BankAccount class has two private attributes, __account_number and __balance, 
which cannot be accessed directly from outside the class. The class also has three methods, deposit(), 
withdraw(), and get_balance(), which provide a simple and clear interface to interact with the object. 
The deposit() and withdraw() methods modify the private attribute __balance, and the get_balance() method 
returns the current balance of the account.'''

'''What are constructors in Python?

In Python, a constructor is a special method that gets called automatically when an object is 
created from a class. It is used to initialize the attributes of the class.

In Python, the constructor method is defined with the name __init__(). It takes the self 
parameter, which refers to the instance of the class that is being created, as well as any 
other parameters that are needed to initialize the class.

Here is an example of a simple class with a constructor:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 25)
print(person1.name) # Output: John
# here, self is nothing but person1
print(person1.age) # Output: 25