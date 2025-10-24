"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

print(" ".join(sorted(names)))

# list comprehension to create a list of all the names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# list comprehension to create a list of integers from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# list comprehension to create a list of only the numbers greater than 9
numbers_over_nine = [number for number in numbers if number > 9]
print(numbers_over_nine)

# use a list comprehension and join method to create a string
long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_names)
