'''Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘ + ’ operator is overloaded by int class and str class. You might have noticed 
that the same built-in operator or function shows different behavior for objects of different classes, 
this is called Operator Overloading. '''

# Python program to show use of
# + operator for different purposes.
  
print(1 + 2)
  
# concatenate two strings
print("Coders"+"daily") 
  
# Product two numbers
print(3 * 4)
  
# Repeat the String - overloading
print("Coder"*4)



# Python program to overload
# a comparison operators

class A:
	def __init__(self, a):
		self.a = a
	def __gt__(self, other):
		if(self.a>other.a):
			return True
		else:
			return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
	print("ob1 is greater than ob2")
else:
	print("ob2 is greater than ob1")
	

'''The code creates a class A that allows instances to be compared using the 
> operator based on their a attributes. The comparison shows that ob2 (with a equal to 3) 
is greater than ob1 (with a equal to 2), resulting in the printed message "ob2 is greater than ob1".'''

