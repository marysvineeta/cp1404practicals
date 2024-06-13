"""
CP1404/CP5632 - Practical
sales bonus program
"""


sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = sales*0.1
    else:
        bonus = sales*0.15
    print("bonus is:$", bonus)
    sales = float(input("Enter sales: $"))
print("Invalid Input")
