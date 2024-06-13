"""
CP1404/CP5632 - Practical
loop program
"""

print("odd numbers between 1 to 20")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.
print("count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=" ")
print()
#b.
print("count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=" ")
print()
#c.
n = int(input("star count: "))
print("Number of stars:")
for _ in range(n):
    print("*", end="")
print()
#d.
n = int(input("star count: "))
for i in range(1, n + 1):
    print('*' * i)
