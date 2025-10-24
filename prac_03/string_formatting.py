name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print("My guitar: " + name + ", first made in " + str(year))
print("My guitar: {}, first made in {}".format(name, year))
print(f"My {name} was first made in {year} (that's right, {year}!)")

print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about ${cost:,.0f}!")

for power in range(0, 11):
    print(f"2 ^ {power:2} is {2 ** power:4}")
