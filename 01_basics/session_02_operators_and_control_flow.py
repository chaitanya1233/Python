"""
Topic   : Operators, Control Flow & Loops
Session : 02
Date    : December 3, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Division Operators
# ===========================================================

print(100 / 20)
print(type(100 / 20))

# Integer (Floor) Division
print(100 // 20)
print(type(100 // 20))

# Modulus Division
print("Modulus division:", 100 % 3)
print("Modulus division:", 3 % 2)

# Power Operator
a = 5
b = 3
print(a ** b)

# ===========================================================
# SECTION 2: Assignment Operator
# ===========================================================

x = 0
x += 1
print(x)

# ===========================================================
# SECTION 3: None Data Type
# ===========================================================

# Very important for ML, AI and Data Science
winner = None
print(winner is None)        # True if None
print(winner is not None)    # False if None
print(type(winner))

winner = True
print(winner)
print(type(winner))

# ===========================================================
# SECTION 4: Control Flow — if / elif / else
# ===========================================================

# Simple if
num = int(input("Enter your number: "))
if num > 0:
    print(num)

# if-else
num = int(input("Enter yet another number: "))
if num > 0:
    print("It's Positive")
else:
    print("It's Negative")

# elif ladder — Savings example
savings = float(input("Enter how much money you have in savings: "))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("Well done")
elif savings < 1000:
    print("That's a tidy sum")
elif savings < 10000:
    print("Welcome sir!")
else:
    print("Thank you")

# ===========================================================
# SECTION 5: While Loop
# ===========================================================

# Loop continues until the breaking condition is met
count = 1
print("Starting")
while count <= 10:
    print(count)
    count += 1

# ===========================================================
# SECTION 6: For Loop
# ===========================================================

print("Print out the values in range")
for i in range(2, 10):
    print(i)
print("Done")

# ===========================================================
# SECTION 7: Break Statement
# ===========================================================

num = int(input("Enter a number to check for: "))
for i in range(0, 16):
    if i == num:
        break
    print(i)
print("Done")

# ===========================================================
# SECTION 8: Anonymous Variable ( _ )
# ===========================================================

for _ in range(0, 10):
    print('.', end=' ')
    print()

# ===========================================================
# SECTION 9: Odd and Even Numbers in a Range
# ===========================================================

# Print odd numbers from 4 to 19
start, end = 4, 19
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")

print()

# Print even numbers from 4 to 19
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")
