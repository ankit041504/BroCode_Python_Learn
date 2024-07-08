# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Creating a set with elements
fruits = {'apple', 'banana', 'mango'}
print(fruits)  # Output: {'banana', 'mango', 'apple'}


# Adding elements to a set
fruits.add('orange')
print(fruits)  # Output: {'banana', 'mango', 'apple', 'orange'}

# Removing elements from a set
fruits.remove('banana')
print(fruits)  # Output: {'mango', 'apple', 'orange'}

fruits.discard('apple')
print(fruits)  # Output: {'mango', 'orange'}


# Sets support various operations such as union, intersection, difference, and symmetric difference.

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}  like inner join

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2} like left join

# Symmetric difference of sets
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}  NOT of inner Join


# Set Methods:
# Sets provide several methods to perform different operations. Some commonly used methods include
# len(), clear(), copy(), issubset(), issuperset(), and pop().

fruits = {'apple', 'banana', 'mango'}

# Get the length of a set
print(len(fruits))  # Output: 3

# Clear the set
fruits.clear()
print(fruits)  # Output: set()

# Copy a set
fruits = {'apple', 'banana', 'lichi', 'mango'}
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: {'banana', 'mango', 'apple'}

# Check if a set is a subset or superset of another set
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

# Remove and return an arbitrary element from the set
element = fruits.pop()
print(element)  # Output: 'banana'
print(fruits)  # Output: {'lichi', 'apple', 'mango'}

# Question 1: Create a set named countries with the following elements: 'USA', 'Canada',
# 'Germany', 'Japan'.

# Question 2: Add the element 'France' to the countries set.

# Question 3: Remove the element 'Japan' from the countries set.

# Question 4: Create another set named european_countries with the elements: 'Germany',
# 'France', 'Italy'.

# Question 5: Find the union of the countries and european_countries sets.

# Question 6: Find the intersection of the countries and european_countries sets.

# Question 7: Check if countries is a superset of european_countries.

# Question 8: Remove an arbitrary element from the countries set using the appropriate method.

# Answers:

# Question 1:
# pythonCopy code
# countries = {'USA', 'Canada', 'Germany', 'Japan'}
#
# Question 2:
# countries.add('France')
#
# Question 3:
# countries.remove('Japan')
#
# Question 4:
# european_countries = {'Germany', 'France', 'Italy'}
#
# Question 5:
# union_set = countries.union(european_countries)
#
# Question 6:
# intersection_set = countries.intersection(european_countries)
#
# Question 7:
# countries.issuperset(european_countries)
#
# Question 8:
# countries.pop()