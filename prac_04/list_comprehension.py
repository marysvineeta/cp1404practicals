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

# list comprehension that creates a list containing the initials
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string
print(" ".join(sorted(names)))

lowercase_full_names = [full_name.lower() for full_name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)


digits = ([number for number in numbers if number > 9])
print(digits)

# to create a string of the last names for those full names longer than 11 characters
last_name = ", ".join([(name[name.find(" ") + 1:]) for name in full_names if len(name) > 11])
print(last_name)