"""
#100 Days of Code Challenge
Day 4: Loops
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. \n - introduces a new line
"""

# Generating a string of odd numbers
odd_numbers = ""
for number in range(20):
    if number % 2 != 0:
        odd_numbers += str(number) + " "
print(odd_numbers)

# Generating numbers within a certain range
# 1. Using for and range commands
for number in range(5):
    print(number)

# 1.1 Printing in reverse order
for number in range(5, 0, -1):
    print(number)

# 2. Using while loop
age = 0
while age < 5:
    print(age)
    age += 1

# 2.1 Printing in reverse order
age = 5
while age > 0:
    print(age)
    age -= 1

# 3. Using for and while loops
range_numbers = 'stop'
while range_numbers != 0:
    for number in range(range_numbers):
        print(number)
    range_numbers = input("Enter range value: ")
    if range_numbers != 'stop':
        range_numbers = int(range_numbers)

# 4. Calculating sum of numbers 1 to 1000
total_sum = 0
for sum_numbers in range(1000):
    total_sum += sum_numbers
print(total_sum)

total_sum = 0
numbers = 0
while numbers <= 1000:
    # print(numbers)
    total_sum += numbers
    numbers += 1
print(total_sum)

# 5. Implementing the Fibonacci series
# Each number is a sum of the previous two numbers
# e.g 1, 1, 2, 3, 5, 8, 13, 21...
fibon_series = ""
number_1 = 0
number_2 = 1
series = 0
while series in range(5):
    fibon_series += str(number_2) + ", "
    result = number_1 + number_2
    fibon_series += str(result) + ", "
    series += 1
    number_2 += result
    number_1 = result

print(fibon_series)

# 5.1 Using for loop to implement the Fibonacci series
fibon_series = ""
number_a = 0
number_b = 1
for series in range(50):
    fibon_series += str(number_b) + ", "
    result = number_a + number_b
    fibon_series += str(result) + ", "
    series += 1
    number_a = result
    number_b += result
    if number_a > 100:
        print("Series ended at: ", number_a)
        break

print(fibon_series)
