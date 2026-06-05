"""
Topic   : Functions — Parameters, Lambda, Filter & Comprehensions
Date    : December 17, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Function with Single Return Value
# ===========================================================

def info(name):
    return name

name = info("Arya")
print("The name is:", name)

# ===========================================================
# SECTION 2: Function with Multiple Parameters
# ===========================================================

def calc(a, b):
    mul = a * b
    add = a + b
    return mul, add

a = 10
b = 2
x, y = calc(a, b)
print("x:", x)
print("y:", y)

# ===========================================================
# SECTION 3: Recursive Function — Factorial
# ===========================================================

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

fact = factorial(5)
print(fact)

# ===========================================================
# SECTION 4: Lambda Function vs Regular Function
# ===========================================================

def info(name, age):
    print(f"Name is {name} and age is {age}")

name = "Arya"
age = 34
info(name, age)

# Lambda note: multiple return values need careful syntax
# Correct lambda for filtering:
# add = lambda name, age: (name, age)

# ===========================================================
# SECTION 5: filter() with Lambda
# ===========================================================

lst = [12, 3, 4, 23, 6, 78976, 34]

even_lst = list(filter(lambda x: x % 2 == 0, lst))
print(even_lst)

odd_lst = list(filter(lambda x: x % 2 != 0, lst))
print(odd_lst)

# ===========================================================
# SECTION 6: List Comprehension
# ===========================================================

lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i)

# Iterating over a string
name = "Arya"
for i in name:
    print(i, type(i))

# Syntax: [value | loop | condition]

# Create list from 1 to 10
lst = [i for i in range(1, 11)]
print(lst)

# Store only even numbers
even_lst = [i for i in lst if i % 2 == 0]
print(even_lst)

# Flatten a nested list
nested_lst = [[1, 2, 3, 4], [5, 6, 7, 8, 9, 10]]
flat_lst = []
for i in nested_lst:
    for j in i:
        flat_lst.append(j)
print(flat_lst)

# ===========================================================
# SECTION 7: Dictionary Comprehension
# ===========================================================

current_dict = {
    "person1": 1000,
    "person2": 3000,
    "person3": 4000,
    "person4": 4300,
    "person5": 500
}

# Filter values greater than 2000
new_dict = {k: v for k, v in current_dict.items() if v > 2000}
print(new_dict)

# ===========================================================
# SECTION 8: *args and **kwargs
# ===========================================================

# *args — variable positional arguments
def fruits(*args):
    print(f"The first fruit is {args[0]} and last fruit is {args[-1]}")

fruits("papaya", "banana", "mango", "kiwi")

# **kwargs — variable keyword arguments
def my_fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

my_fun(first_name="Papalal", mid_name="Mohanlal", last_name="Goyal")

# ===========================================================
# SECTION 9: Default Parameter
# ===========================================================

def my_function(country="Norway"):
    print("I am from " + country)

my_function("Dubai")
my_function("India")
my_function()       # Default parameter used

# ===========================================================
# SECTION 10: Passing a List to a Function
# ===========================================================

def my_function(fruits):
    for x in fruits:
        print(x)

fruits = ['Orange', 'Banana', 'Mango']
my_function(fruits)
