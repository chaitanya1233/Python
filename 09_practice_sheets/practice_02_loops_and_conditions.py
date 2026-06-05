"""
Topic   : Practice Sheet 02 — Loops & Conditions
Date    : December 3, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Student Report Card Generator
# ===========================================================

marks = []
for i in range(1, 6):
    user_input = int(input("Enter the marks of subject " + str(i) + ": "))
    marks.append(user_input)

print("Marks:", marks)

total = sum(marks)
print("The sum of subjects is:", total)

average_marks = total / 5
print("The average of the marks is:", average_marks)

if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
elif average_marks >= 70:
    print("Grade: C")
elif average_marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

if average_marks >= 36:
    print("Result: Pass")
else:
    print("Result: Fail")

# ===========================================================
# Q2: Menu-Driven Calculator
# ===========================================================

while True:
    print("------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice != 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    match choice:
        case 1:
            print("Sum:", num1 + num2)
        case 2:
            print("Subtraction:", num1 - num2)
        case 3:
            print("Multiplication:", num1 * num2)
        case 4:
            print("Division:", num1 / num2)
        case 5:
            break

# ===========================================================
# Q3: Number Analyzer (Even/Odd)
# ===========================================================

user = int(input("Enter a number: "))
if user % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")
