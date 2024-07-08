# Python string methods along with examples:

# capitalize():
# This method returns a string with the first character capitalized and the rest of the characters
# in lowercase.

string1 = "hello world"
new_string1 = string1.capitalize()
print(new_string1) # Output: "Hello world"

# upper(): This method returns a string with all characters in uppercase.

string2 = "hello world"
new_string2 = string2.upper()
print(new_string2) # Output: "HELLO WORLD"


# lower(): This method returns a string with all characters in lowercase.

string3 = "HELLO WORLD"
new_string3 = string3.lower()
print(new_string3)  # Output: "hello world"

# strip(): This method returns a string with leading and trailing whitespace removed.

string4 = "    hello world    "
new_string4 = string4.strip()
print(new_string4)  # Output: "hello world"


# split(): This method splits a string into a list of substrings based on a specified delimiter.

string5 = "apple,banana,orange"
new_list5 = string5.split(",")
print(new_list5) # Output: ["apple", "banana", "orange"]


# join(): This method joins a list of strings into a single string using a specified delimiter.


list_of_strings6 = ["apple", "banana", "orange"]
new_string6 = ";".join(list_of_strings6)
print(new_string6) # Output: "apple,banana,orange"


# replace(): This method replaces all occurrences of a specified substring with another substring.

string7 = "hello world"
new_string7 = string7.replace("world", "python")
print(new_string7)  # Output: "hello python"


# startswith(): This method returns True if a string starts with a specified substring, and False
# otherwise.

string8 = "hello world"
result8 = string8.startswith("hello")
print(result8)  # Output: True


# endswith(): This method returns True if a string ends with a specified substring, and False
# otherwise.


string9 = "hello world"
result9 = string9.endswith("hello")
print(result9) # Output: False


# find(): This method returns the index of the first occurrence of a specified substring in a
# string, or -1 if the substring is not found.


string10 = "hello world"
index10 = string10.find("world")
print(index10) # Output: 6

