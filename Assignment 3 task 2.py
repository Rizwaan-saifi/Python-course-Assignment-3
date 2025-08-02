# Task 2: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:

# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# Square root of the number
# Natural logarithm (log base e) of the number
# Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

number = float(input("Enter a number: "))  # take a number as input

# Square root of the number
square = math.sqrt(number)

# Natural logarithm (log base e) of the number
if number > 0:
    natural_log = math.log(number)
else:
    natural_log = print("undefind")

# Sine of the number (in radians)
sine = math.sin(number)

# 3.   Displays the calculated results.
print("square root of the number ",number," : ",square)
print("Natural logarithm of the number ",number," : ",natural_log)
print("Sine of the number ",number," : ",sine)
