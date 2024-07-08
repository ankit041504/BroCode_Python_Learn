# Conditional statements in python are used in a way like any other programming language.
# In general, there are three conditional statements in python if, elif, and else.
# if statement is the most widely used conditional statement.
# There could be one or more than one elif depending on the requirements. elif is used in the same way as else if is used in most programming languages.
# Usage of else is mostly optional.

#Program to check whether the number is zero, positive or negative.

my_num = int(input("enter number : "))

if my_num == 0:
    print("The number is zero")
elif my_num > 0:
    print("The number is a positive number")
else:
    print("The number is a negative number")


#Print "Excellent" if the marks obtained are greater than 90 and lesser than 100.

marks = int(input("enter number : "))
if marks > 90 and marks <100:
    print("Excellent")
else: print("ok")

# Here are 20 practice coding questions on conditional statements in Python:
#
# 1. Write a Python program to check if a number is positive, negative, or zero.
# 
# 2. Create a program that takes a user's age as input and determines if they are eligible to vote (18 or older).
#
# 3. Write a Python function that checks if a given year is a leap year.
#
# 4. Create a program that calculates the discount on a purchase based on the total amount. If the total is greater than $100, apply a 10% discount; otherwise, apply a 5% discount.
#
# 5. Write a program that takes a temperature in Celsius as input and converts it to Fahrenheit using the formula: F = (C * 9/5) + 32.
#
# 6. Build a Python program that calculates the BMI (Body Mass Index) of a person based on their weight (in kg) and height (in meters) and provides a classification (Underweight, Normal, Overweight, or Obese).
#
# 7. Create a program that determines whether a given number is even or odd.
#
# 8. Write a Python function that checks if a given string is a palindrome (reads the same forwards and backwards).
#
# 9. Develop a program that calculates the area of a triangle given its base and height.
#
# 10. Implement a Python program that simulates a basic calculator. It should take two numbers and an operator (+, -, *, /) as input and perform the corresponding calculation.
#
# 11. Write a program that takes a user's score as input and assigns a grade (A, B, C, D, or F) based on the following grading scale: A >= 90, B >= 80, C >= 70, D >= 60, F < 60.
#
# 12. Create a program that determines if a given year is a "century year" (ends in 00) and whether it's a leap year.
#
# 13. Write a Python function that finds the maximum of three numbers.
#
# 14. Build a program that checks if a given character is a vowel or a consonant.
#
# 15. Create a program that determines if a given number is a prime number.
#
# 16. Write a Python function that computes the factorial of a non-negative integer.
#
# 17. Develop a program that calculates the sum of all even numbers in a given range.
#
# 18. Implement a program that calculates the roots of a quadratic equation (ax^2 + bx + c = 0).
#
# 19. Write a Python program that checks if a given year is a "special year" (a year that is divisible by 4 but not by 100 or divisible by 400).
#
# 20. Create a program that takes two integers as input and finds their greatest common divisor (GCD) using the Euclidean algorithm.