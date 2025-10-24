score = float(input("Enter score: "))

if not 0 <= score <= 100:
    result = "Invalid score"
elif score >= 90:
    result = "Excellent"
elif score >= 50:
    result = "Passable"
else:
    result = "Bad"

print(result)
