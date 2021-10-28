"""
#100 Days of Code Challenge
Day 2: Arithmetic Operations
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. \n - introduces a new line
"""
# Addition
boys = 10
girls = 13
total_students = boys + girls
print("Total Students: ", total_students)

boys += 1  # Same as boys = boys + 1
girls += 1  # Same as girls = girls + 1

# Subtraction
length = 100
width = 40
difference_in_distance = length - width
print("\nDifference in length: ", difference_in_distance)

# Multiplications
area = length * width
print("\nArea: ", area)

# Division
distance_ratio = length / width
print("\nDistance Ratio: ", distance_ratio)

# Modulo Division
dividend = 23
divisor = 9
remainder = dividend % divisor

# Floor division
quotient = dividend // divisor

print("\nRemainder: ", remainder)
print("Quotient: ", quotient)

# Exponents
square = 2 ** 2  # Is same as 2 x 2
cube = 2 ** 3  # Is the same as 2 x 2 x2

# Operators
# == equal to
bag = 3  # Single assignment
bag % 2 == 0  # Checks for equality by comparing and returns a True or False

# != not equal
book = 4
if book % 2 != 0:
    print("Number is odd")

# < less than  | > greater than
# does not include the comparison values
book < 10
book > 2

# <= less than or equals to  | >= greater than or equal to
# includes the comparison value
book <= 3
book >= 4

"""
Operator precedence
Determines which operators to be performed first
parenthesis > exponential > division | multiplication > addition | substraction
Operator precedence can be obtained from https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
50 + 3 * 6 / (9 - 3) ** 4

# LOGICAL OPERATORS
# Compares truth values of two comparisons
score = 100
if score >= 50 and score <= 200:  # and returns True if both values are true
    print("Score is valid")

if score >= 150 or score <= 200:  # or returns True if one values are true
    print("Score is valid")

not score < 100  # not - negates the truth value
