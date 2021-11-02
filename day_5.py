"""
#100 Days of Code Challenge
Day 5: Strings
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. \n - introduces a new line
    3. Strings are immutable - cannot change the contents of the string
"""

# Creating strings
name = "Jacob"
name_two = 'Mary'
books = "Mary's Books"

# Idexing strings
print(name[0])  # Will print the first letter in 'Jacob'
print(name[0:2])  # Will print letters within the specified range

# Substrings
name.find('a')  # Will return index of letter 'a' is present in name

# Splitting strings
code = "Python is a cool language"
code_split = code.split()  # Splits by space - default
code_split_2 = code.split(",")  # Split by ','

# Stripping - removing spaces from strings
first_name = '   Victor  '
first_name.rstrip()  # Removes spaces at the end
first_name.lstrip()  # Removes spaces at the beginning
first_name.strip()  # Removes spaces at both ends

# String functions
book = 'The Great Hope'
book.isalnum()  # Returns true if string has alphanumeric characters
book.isupper()  # Returns true if string is uppper case
book.isdigit()  # Returns true if string has only digits
book.isalpha()  # Returns true if string has only alphabet characters
book.endswith('e')  # Returns true if string ends with specified substrings

# String concatenation - combining strings
f_name = 'Mark'
l_name = 'Finlay'
full_name = f_name + l_name

# Uppercase, Lowercase, Title case
country = "maLdiVes"
country.upper()  # Returns all upper case
country.lower()  # Returns all lower case
country.title()  # Return a string with first letter of each word capitalized

# Iterating over loops
# Finding how many times a character appears in a string
school_name = input("Enter name of your school: ")
character = input("Enter the letter to check: ")
counter = 0
for letter in school_name:
    if letter == character:
        counter += 1
print(f"{character} has appeared {counter} times")
