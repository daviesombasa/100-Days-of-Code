"""
#100 Days of Code Challange
Day 1: Python Basics

"""
# Declaring variables
name = "wanderking"  # String
age = 21  # Interger
is_eating = True  # Boolean

# Checking variable type
print("Variable Types")
print("name is type", type(name))
print("age is type", type(age))
print("is_eating is type", type(is_eating))

# Division of numbers results in a float
print('\nDivision of numbers')
print(age / 12)
print(age * 10.2)

# Multiple Assignments
height, weight = 140.5, 70
print("\nMultiple Assignments")
print(height)
print(weight)

# Variable naming convention
"""
1. Should not contain any reserve key words eg import, while, for
    To check for python keywords you can use the following code
    import keyword
    keyword.kwlist
2. Can only contain _ as the only special character eg student_age
3. Use meaningful words eg student_age
4. Cannot contain spaces 
5. Cannot start with an integer eg 1_one is not a valid name
"""

# Operations on input data
"""
input() function treats all data as strings
In order to perform any arithmetic operations with it, appropriate type convertion must be performed.
"""
length = input("Enter length: ")
width = input("Enter width: ")

area = int(length) * int(width)
print("Area is = ", area)