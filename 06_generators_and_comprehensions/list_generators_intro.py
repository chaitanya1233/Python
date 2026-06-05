"""
Topic   : List Comprehensions & Generators — Introduction
Date    : December 24, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Building a List with a Loop
# ===========================================================

lst = []
for i in range(1, 21):
    lst.append(i)
print(lst)

# ===========================================================
# SECTION 2: List Comprehension (Creating on the fly)
# ===========================================================

lst = [num for num in range(1, 11)]
print(lst)

# Capitalize each item
names = ['dada', 'mama', 'kaka']
names = [name.capitalize() for name in names]
print(names)

# ===========================================================
# SECTION 3: List Comprehension with Conditions
# ===========================================================

def is_even(num):
    return num % 2 == 0

# Keep only even numbers
lst = [num for num in range(1, 11) if is_even(num)]
print(lst)

# Alternative: inline condition
even_lst = [i for i in range(1, 11) if i % 2 == 0]
print(even_lst)

# ===========================================================
# SECTION 4: Generator Expression
# ===========================================================

# Generator expressions are lazy — they compute on demand
even_sum = sum(i for i in range(10))
print(even_sum)

# ===========================================================
# SECTION 5: Nested Comprehensions
# ===========================================================

lst = [f"{i}:{j}" for i in range(1) for j in range(3)]
print(lst)

# ===========================================================
# SECTION 6: Set Comprehension
# ===========================================================

s = {s for s in range(1, 10)}
print(s)

# ===========================================================
# SECTION 7: Generator Function with yield
# ===========================================================

# A generator function uses 'yield' instead of 'return'
# It pauses execution and resumes from where it left off

def num_generator(n):
    for i in range(n):
        yield i

gen = num_generator(10)
print(list(gen))
