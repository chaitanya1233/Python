"""
Topic   : Function Types — Regular, Recursive, Lambda & Filter
Date    : December 16, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Function with Return Value
# ===========================================================

def my_function(x):
    y = x * 5
    return y

my_function(4)

# Multiple return values
def my_function(x):
    y = x * 5
    z = x * 7
    return x, y

print(my_function(4))

# ===========================================================
# SECTION 2: pass Keyword (placeholder)
# ===========================================================

# Use when business logic is not yet defined
def my_function(x):
    pass

my_function(4)

# ===========================================================
# SECTION 3: Recursive Function — Factorial
# ===========================================================

# n! = n * (n-1)!
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

# ===========================================================
# SECTION 4: Lambda Function
# ===========================================================

# Regular function
def add(x):
    return x + 10

print(add(20))

# Lambda equivalent
add = lambda a: a + 10
print(add(20))

# Lambda with two arguments
add = lambda a, b: a + b
print(add(2, 4))

# ===========================================================
# SECTION 5: filter() with Lambda
# ===========================================================

lst = [34, 12, 64, 55, 75, 13, 63]

# Filter even numbers
even_list = list(filter(lambda x: (x % 2 == 0), lst))
print(even_list)

# Filter odd numbers
odd_lst = list(filter(lambda x: (x % 2 != 0), lst))
print(odd_lst)
