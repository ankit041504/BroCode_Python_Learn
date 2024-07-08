# Creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Creating a tuple with elements
fruits = ('apple', 'banana', 'mango')
print(fruits)  # Output: ('apple', 'banana', 'mango')

# Creating a tuple without parentheses
numbers = 1, 2, 3
print(numbers)  # Output: (1, 2, 3)


fruits = ('apple', 'banana', 'mango')

# Accessing elements by index
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'mango'

# Negative indexing
print(fruits[-1])  # Output: 'mango'


# Concatenating tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: ('a', 'b', 'c', 1, 2, 3)

# Repeating a tuple
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# Slicing a tuple
sliced_tuple = concatenated_tuple[2:5]
print(sliced_tuple)  # Output: ('c', 1, 2)


# Example 1: Multiple Return Values -- Tuples can be used to return multiple values from a function:

def get_circle_properties(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return circumference, area

circle_radius = int(input("radius ?"))
circle_circumference, circle_area = get_circle_properties(circle_radius)
print("Circumference:", circle_circumference)
print("Area:", circle_area)



# Example 2: Unpacking Tuples-- Tuples can be unpacked to assign values to multiple variables:

student = ('John', 'Doe', 20, 'Computer Science')
first_name, last_name, age, major = student # unpacking
print("First Name is:", first_name, last_name)
print("Age is :", age)
print("Major is :", major)




# Example 3: Data Validation with Tuples -- Tuples can be used to validate and process data:

user_data = ('John',  'Doe' , 'john.doe@example.com')
required_fields = ('first_name', 'last_name', 'email')

for field, value in zip(required_fields, user_data):
    if not value:
        print(f"Error: {field} is required.")
