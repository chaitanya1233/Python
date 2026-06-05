"""
Topic   : Practice Sheet 01 — Type Casting & Arithmetic
Date    : December 2, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Add Two Numbers (String Input)
# ===========================================================

num1 = '45'
num2 = '30'
total = int(num1) + int(num2)
print('Sum of the two numbers is:', total)

# ===========================================================
# Q2: Find Data Type of User Input
# ===========================================================

user_input = input("Enter anything you want to enter: ")
print("You entered:", user_input)
print(type(user_input))

# ===========================================================
# Q3: Simple Interest Calculator (SI = P*R*T/100)
# ===========================================================

principle = float(input("Enter your principal amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time = float(input("Enter the time (years): "))
simple_interest = (principle * rate_of_interest * time) / 100
print("The simple interest is:", simple_interest)

# ===========================================================
# Q4: Temperature Converter (Celsius to Fahrenheit)
# F = (C * 9/5) + 32
# ===========================================================

celsius_temp = float(input("Enter the temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9 / 5) + 32
print("The temperature in Fahrenheit is:", fahrenheit_temp)

# ===========================================================
# Q5: Even or Odd Checker
# ===========================================================

number = int(input("Enter your number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# ===========================================================
# Q6: Arithmetic Operations Program
# ===========================================================

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus (remainder):", num1 % num2)
print("Exponent:", num1 ** num2)

# ===========================================================
# Q7: List of Strings to Integers
# ===========================================================

l1 = ["10", "20", "30", "40"]
print(type(l1))
l2 = [int(i) for i in l1]
print("The converted list:", l2)

# ===========================================================
# Q8: Swap Two Variables (Without Third Variable)
# ===========================================================

a = int(input("Enter value of a: "))
b = int(input("Enter the value of b: "))
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

# ===========================================================
# Q9: Age Converter
# ===========================================================

print("* Welcome to the Age Converter Application *")
age = float(input("Enter your age: "))
years = age
months = age * 12
days = years * 365
hours = days * 24

print("Years lived:", years)
print("Months lived:", months)
print("Days lived:", days)
print("Hours lived:", hours)
