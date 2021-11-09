"""
#100 Days of Code Challenge
Day 6: Functions
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. \n - introduces a new line
    3. Arguments are passed into functions.
    4. The order of arguments matters unless you explicitly define them
    5. docstring are used to describe what a function does
"""


# User Defined Functions
def magic_numbers():
    trials = 3
    while not False:
        try:
            number = float(input("Enter your magic number: "))
            trials -= 1
            if number == 25:
                print("Magic Number Found! ", number)
                break
            elif trials == 0:
                print("Your time has expired."
                      "Please try again")
                break
        except:
            print("Please enter a valid number. ")


magic_numbers()


def fibanoci_series(n):
    fibon_series = ""
    number_1 = 0
    number_2 = 1
    series = 0
    while series in range(n):
        fibon_series += str(number_2) + ", "
        result = number_1 + number_2
        fibon_series += str(result) + ", "
        series += 1
        number_2 += result
        number_1 = result

    return fibon_series


fibanoci_series(2)


def sum_numbers(lower_limit, upper_limit):
    # Docstrings - Provide more information about a function
    """
    Write a function that takes in 2 numbers.
    Find out all the numbers divisible by 5 between those numbers and add them up.
    Return the sum.
    param n: Lower limit
    param m: Upper limit
    return: Sum
    """
    sum_total = 0
    for number in range(lower_limit, upper_limit):
        if number % 5 == 0:
            sum_total += number
    return sum_total


sum_numbers(4, 100)


def avg_ages(*ages):
    # *ages takes any number of variables
    for age in ages:
        print(age)


avg_ages(10, 20)
avg_ages(10, 20, 30)

# Python Standard Functions
# These are just a sample

# length functions
name = "Anthony Manne"
len(name)  # Return number of characters in the string

# absolute functions - only takes in numbers
abs(-10) # Returns magnitude of a number

# input functions
movies = input("Enter your favourite movie: ") # Returns as a string

# minimum and maximum functions
# used for both numbers and characters
grades = [12,25,63,98,10,2,56,36,99,18]
min(grades)
max(grades)

# Sum of alternate odd numbers within a range
def alternate_odd(limit):
    total_sum = 0
    odd_numbers = []
    for number in range(1, limit):
        if number % 2 != 0:
            odd_numbers.append(number)
    for item in odd_numbers:
        if odd_numbers.index(item) % 2 == 0:
            total_sum += item
    return total_sum


alternate_odd(20)

# Reverse a string
def reverse(name):
    new_name = ""
    for letter in name:
        letter = (len(name) - name.index(letter))
        new_name += name[letter - 1]
    return new_name


reverse('vinicent')