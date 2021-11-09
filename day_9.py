"""
#100 Days of Code Challenge
Day 9A: Data Structures : Tuples
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. Tuples are created using parenthesis.
    3. A one element tuple is created by adding a "," after the element
    4. Tuples are immutable and meant for short storage of parameters
    5. If elements of the tuple are mutable, then they can be changed.
"""

# Creating tuples
tup_1 = ('name', 'age', 'school')

# Accessing elements of a tuple
print(tup_1[0])  # access the first element in the tuple

# Tuple methods
tup_1.count('name')  # Returns number of occurrences of an item
tup_1.index('age')  # Returns the first index of the occurrence of the element

# Converting list to tuples
list_1 = (2, 3, 5, 6, 'home')
tup_2 = tuple(list_1)

# Changing mutable elements

tup_3 = (45, [33, 90], 100, 78)
tup_3[1][1] = 356
print(tup_3)

"""
#100 Days of Code Challenge
Day 9B: Data Structures : Sets
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. Represents unique data elements without duplication
    3. Applied in determine unions, differences, intersections
    4. They are not ordered and have no indexing
    5. Created using curly brackets {}
"""
# Creating a set
days = {'mon', 'tue', 'tue', 'mon', 'wed', 'wed', 'thur'}
print(days)  # Will print only unique elements

# Creating an empty string
names = set()
print(type(names))  # Will return type set

# Adding elements
days.add('fri')

# Modifying elements
days.pop()  # Removes a random element
days.remove('fri')  # Remove element 'fri'. raises error if false
days.discard('mon') # Remove element 'mon'. Raises no error if false
days.clear()  # Removes all elements in the set

days.union()

# Set operations
# This modules generates a random list which we convert to a set
import random

set_1 = set(random.sample(range(1, 10), 5))
set_2 = set(random.sample(range(1, 10), 5))

# Union
set_1.union(set_2)  # or set_1 | set_2

# Intersection
set_1.intersection(set_2) # or set_1 & set_2

# Set difference
set_1.difference(set_2)

# Symmetric difference
set_1.symmetric_difference(set_2)
