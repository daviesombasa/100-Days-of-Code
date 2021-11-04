"""
#100 Days of Code Challenge
Day 7: Data Structures : Lists
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
"""
# Merging list
list_1 = [1, 2, 3, 4, 'cat', 'dog']
list_2 = [5, 6, 7, 8, 'ben', 'walk']

list_1.extend(list_2)
print(list_1)

# Indexing
print(list_1[0])  # First element in list
print(list_1[-1])  # Last element in list

# Copying lists
list_3 = list_1[:]  # Makes a copy of the entire list
list_4 = list_1[1:]  # Makes a copy beginning from index one to the last element
list_5 = list_1[1:3]  # Makes a copy of items within the range

# Manipulation of lists
del (list_1[2])  # Deletes the item in tbe index specified
list_1.insert(2, 25)  # Insert a value
list_1.append(10)  # Append a value
list_1.pop(2)  # Pop a value at specified index
list_1.clear()  # Removes items in the list

# Nested Lists
person = [['barrister', 'bronny'], 25, 123, 'male']

# Enumerating Lists
for index, value in enumerate(person):
    print(index, value, sep=" = ")

grades = []  # Creates an empty list
# Populating the list

while True:
    grade = input("Enter grade")
    if grade == 'e':
        break
    else:
        grade = float(grade)
        grades.append(grade)
    print(grades)
    print(f"The sum of the grades is {sum(grades)}\n"
          f"The maximum grade is {max(grades)}\n"
          f"The minimum grade is {min(grades)}\n"
          f"The average score is {sum(grades) / len(grades)}\n")


# Calculating number of vowels in a sentence
def vowel_count():
    sentence = input("Enter your sentence: ")
    vowels = ['a', 'b', 'c', 'd', 'e']

    count = 0
    for letter in sentence:
        if letter.lower() in vowels:
            count += 1
    return count


vowel_count()
