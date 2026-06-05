"""
Topic   : Data Types & Type Casting
Session : 01
Date    : December 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Number Data Types
# ===========================================================

# Integer
x = 10
print(type(x))

# Type casting - Default type of input() is String
age = input("Enter your age: ")
print(type(age))
print(age)

# Explicit type casting (int)
age1 = input("Enter your age1: ")
age2 = 24
age = int(age1) + int(age2)
print("The value of the age is:", age)
print(type(age))

# ===========================================================
# SECTION 2: Floating Point Numbers
# ===========================================================

exchange_rate = 1.83
print(type(exchange_rate))
print("The exchange rate is:", exchange_rate)

# Converting to float
int_value = 100
float_value = float(int_value)
print("The int value as a float is:", float_value)

string_value = "1.5"
float_value = float(string_value)
print("The string value as a float is:", float_value)

# ===========================================================
# SECTION 3: Complex Numbers
# ===========================================================

c1 = 1       # Real number
c2 = 2j      # Imaginary number
print("c1:", c1, "c2:", c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

# ===========================================================
# SECTION 4: Boolean Type
# ===========================================================

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))  # --> class <bool>

# Converting a string into boolean
status = bool(input("OK is it confirmed? "))
print(status)
print(type(status))

# ===========================================================
# SECTION 5: Arithmetic Operators
# ===========================================================

home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(100 / 20)
print(type(100 / 20))
