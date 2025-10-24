"""
CP1404/CP5632 - Practical
Random number examples
"""

import random

# Line 1
print(random.randint(5, 20))
# I saw a random integer between 5 and 20.
# Smallest number possible: 5
# Largest number possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# I saw a random odd number between 3 and 9 (like 3, 5, 7, or 9).
# Smallest number possible: 3
# Largest number possible: 9
# Line 2 could not produce a 4 because the step is 2.

# Line 3
print(random.uniform(2.5, 5.5))
# I saw a random floating-point number between 2.5 and 5.5.
# Smallest number possible: close to 2.5
# Largest number possible: close to 5.5

# Produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
