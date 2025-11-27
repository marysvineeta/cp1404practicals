"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    return " ".join([s] * n)


def is_long_word(word, length=5):
    return len(word) >= length


def format_sentence(phrase):
    phrase = phrase.strip()

    # Capitalise first letter
    phrase = phrase[0].upper() + phrase[1:]

    # Ensure it ends with one full stop
    if not phrase.endswith("."):
        phrase += "."

    return phrase


def run_tests():
    """Run the tests on the functions."""

    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car("Test Car")
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car("Default Fuel Car")
    assert car.fuel == 0, "Default fuel should be 0"

    car = Car("Fuel Car", 10)
    assert car.fuel == 10, "Fuel was not set correctly when passed in"


run_tests()

# Run doctests
doctest.testmod()
