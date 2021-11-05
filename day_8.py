"""
#100 Days of Code Challenge
Day 8: Data Structures : Dictionaries
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. Has key:value parameters enclosed in a {}
"""

students = {'John': 40, 'Peter': 30, 'Mary': 50}  # Creating a dictionary
print(students)
students['John'] = 70  # Modify the value of John
students['Mark'] = 42  # Add the key, value to the dictionary
print(students['Peter'])
print(students.get('Brian'))  # Returns 'None' is the key doesn't exist


# Creating a dictionary of vowels in a sentence

def vowels():
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels_dict = {}
    sentence = input('Enter your sentence: ')
    for character in sentence:
        if character.lower() in vowels_list:
            if vowels_dict.get(character) is None:
                vowels_dict[character.lower()] = 1
            else:
                vowels_dict[character.lower()] += 1
    print(f'The vowels_dict is {vowels_dict}')

    # Accessing key, value parameters of a dict
    print(f'Keys are: {list(vowels_dict.keys())}')
    print(f'Values are: {list(vowels_dict.values())}')

    vowels_dict.
vowels()
