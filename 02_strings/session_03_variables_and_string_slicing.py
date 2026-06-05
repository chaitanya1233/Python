"""
Topic   : Variables, Scope & String Slicing
Session : 03
Date    : December 4, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Multiple Variable Assignment
# ===========================================================

x, y, z = 5, 6, 7
print(x)
print(y)
print(z)

# ===========================================================
# SECTION 2: Global vs Local Variables
# ===========================================================

# Global variable accessed inside function
x = "awesome"
def my_function():
    print("python is " + x)
my_function()

# Local variable overrides global inside function
x = "awesome"
def my_function():
    x = "fantastic"          # local x
    print("python is " + x)
my_function()
print("python is " + x)     # global x is unchanged

# ===========================================================
# SECTION 3: Python Built-in Data Structures (Overview)
# ===========================================================

# range
x = range(6)
print(x)
print(type(x))

# dictionary
x = {"name": "ram", "age": 34}
print(type(x))

# list
lst = [1, 2, 3]
print(lst)
print(type(lst))

# tuple
tup = (1, 2, 3)
print(tup)
print(type(tup))

# set
set1 = {1, 2, 3}
print(set1)
print(type(set1))

# ===========================================================
# SECTION 4: String Slicing — Positive Indexing
# ===========================================================

x = "this is python. it is very powerful"
print(x)
print(x[2:8])

# Slicing from the beginning
print(x[:3])

x = "government polytechnic osmanpura chhatrapati sambhajinagar"
print(x[23:32])
print(x[:10])
print(x[:22])

x = "this is python.it is very powerful"
print(x[4:])

# ===========================================================
# SECTION 5: String Slicing — Negative Indexing
# ===========================================================

s = "python"
print(s[-1])
print(s[-2])
print(s[-6])
print(s[0:5:2])    # pto
print(s[:5:2])     # pto

s = "powerful"
print(s[-6:-2])
print(s[-2:-6])
print(s[-2:-6:-2])

s = "python"
print(s[::-1])         # reverse string
print(s[-2:-6:-1])     # moves backward

# Mixing positive and negative indices
print(s[1:-1])
print(s[-5:5])

# ===========================================================
# SECTION 6: String Methods
# ===========================================================

x = "this is python. it is very powerful"
print(x.upper())

x = x.upper()
print(x)
print(x.lower())

x = "  this is python  "
print(x.strip())

x = "  this is python"
print(x.lstrip())

x = "this is python  "
print(x.rstrip())

x = "hello"
print(x.replace("hello", "gello"))

x = "hello_world"
print(x.split("_"))

x = "hello world"
print(x.split(" "))

x = "blue-green-red"
print(x.split("-"))

x = "this is python. it is difficult to implement"
print(x.split("."))
