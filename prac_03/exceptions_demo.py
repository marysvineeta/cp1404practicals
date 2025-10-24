try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:   # prevent ZeroDivisionError by checking
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. A ValueError will occur when the user enters something that is not an integer

# 2. A ZeroDivisionError will occur when the user enters 0 as the denominator.

# 3. Yes, we can avoid the ZeroDivisionError by checking that the denominator is not zero
