try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = int(input("Enter the denominator(not 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    denominator = int(input("Enter the denominator(not 0): "))
    fraction = numerator / denominator
    print(fraction)
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
