"""
#100 Days of Code Challenge
Day 3: Nested Loops
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
"""
# Implmenting a basic lift algorithm
user_floor = int(input('Enter current user floor: '))
current_lift_floor = int(input('Enter current lift floor: '))
emergency_status = False

floor_difference = user_floor - current_lift_floor
if floor_difference < 0:
    if not emergency_status:
        current_lift_floor = user_floor
        print("Move down")
else:
    if not emergency_status:
        current_lift_floor = user_floor
        print("Move up")

# Checking if a number is postive, negative or zero
number = int(input("Enter your numnber: "))
if number < 0:
    print("Number ", number, " is negative")
elif number > 0:
    print("Number ", number, " is positive")
else:
    print("Number ", number, " is zero")

# Finding the oldest child
child_1 = int(input('Enter age of child_1: '))
child_2 = int(input('Enter age of child_2: '))
child_3 = int(input('Enter age of child_3: '))

if child_1 > child_2:
    if child_1 > child_3:
        oldest_child = child_1
        print("Oldest child is: ", oldest_child, " years")
    else:
        oldest_child = child_3
        print("Oldest child is: ", oldest_child, " years")
elif child_2 > child_3:
    oldest_child = child_2
    print("Oldest child is: ", oldest_child, " years")
else:
    oldest_child = child_3
    print("Oldest child is: ", oldest_child, " years")
