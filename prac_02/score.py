score = float(input("Enter the score: "))
if score < 0:
    print("Invalid score")
elif score > 100:
        print("Invalid score")
elif score > 50:
        print("Passable")
elif score > 90:
    print("Excellent")
else:
    print("Bad")