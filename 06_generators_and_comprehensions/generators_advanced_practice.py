"""
Topic   : Generators — Advanced Practice (Levels 1–8)
Date    : December–January 2025/2026
Author  : Chaitanya

Source  : Extracted from Advanced_dictionaries_Py.py
          (generator section was unrelated to dictionary topic)
"""

# ===========================================================
# LEVEL 1 — Basic Generator with yield
# ===========================================================

def count_up_to_n(n):
    for i in range(1, n + 1):
        yield i

gen = count_up_to_n(5)
print(next(gen))    # 1
print(next(gen))    # 2
for i in gen:
    print(i)        # 3, 4, 5

# ===========================================================
# LEVEL 2 — Generator as a Filter
# ===========================================================

def positive_num(data):
    for x in data:
        if x > 0:
            yield x

data = list(range(-10, 4))
positive_data = [i for i in positive_num(data)]
print(positive_data)

# Task: yield only strings
def string_data(data):
    for i in data:
        if isinstance(i, str):
            yield i

data = [10, "hi", 5.5, "python", None]
gen = string_data(data)
print(next(gen), end=",")
print(next(gen))

# Task: numbers greater than 10
def nums_filter(data):
    for i in data:
        if i > 10:
            yield i

data = [5, 12, 3, 25, 7]
gen_lst = [i for i in nums_filter(data)]
print(gen_lst)

# ===========================================================
# LEVEL 3 — Even Numbers Generator
# ===========================================================

def even_nums_upto_n(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

even_gen_lst = [i for i in even_nums_upto_n(10)]
print(even_gen_lst)

# ===========================================================
# LEVEL 4 — Generator Expression (One-Line)
# ===========================================================

# Squares of odd numbers from 1 to 10
gen = (x * x for x in range(1, 11) if x % 2 != 0)
for i in gen:
    print(i)

# ===========================================================
# LEVEL 5 — Combining isinstance + Condition
# ===========================================================

# Yield only positive integers (not floats, not strings, not None)
data = [10, -3, 4.5, "5", 8, None]

def pos_int(data):
    for i in data:
        if isinstance(i, int) and i > 0:
            yield i

gen_lst = [x for x in pos_int(data)]
print(gen_lst)

# ===========================================================
# LEVEL 6 — Flatten a Nested List with Generator
# ===========================================================

def flatten_lst(matrix):
    for i in matrix:
        for j in i:
            yield j

matrix = [[1, 2], [3, 4], [5]]
gen_lst = [x for x in flatten_lst(matrix)]
print(gen_lst)

# ===========================================================
# LEVEL 7 — Generator with State (Cumulative Sum)
# ===========================================================

def cumulative_sum(data):
    total = 0
    for i in data:
        total += i
        yield total     # yields running total

data = [1, 2, 3, 4, 5]
gen_lst = [x for x in cumulative_sum(data)]
print(gen_lst)

# ===========================================================
# LEVEL 8 — Validation Generator (Interview Level)
# ===========================================================

# Yield valid numbers: int or float, non-negative
data = [10, "20", None, 5.5, -3]

def non_negative_nums(data):
    for i in data:
        if isinstance(i, (int, float)) and i > 0:
            yield i

gen_lst = [i for i in non_negative_nums(data)]
print(gen_lst)

# Strict integer-only filter
def positive_integers_only(data):
    for i in data:
        if isinstance(i, int) and i > 0:
            yield i

gen_lst = [i for i in positive_integers_only(data)]
print(gen_lst)

# ===========================================================
# BONUS — Valid Numbers from Mixed List
# ===========================================================

"""
Task: From a mixed list, yield only valid numbers:
    - int or float only
    - Ignore strings (even numeric strings)
    - Ignore None
    - Ignore negative numbers

data = [10, "20", None, 5.5, "abc", 30, -5, "40"]
"""

def valid_numbers(data):
    for item in data:
        if isinstance(item, (int, float)) and item > 0:
            yield item

data = [10, "20", None, 5.5, "abc", 30, -5, "40"]
valid_lst = [i for i in valid_numbers(data)]

print("Min:", min(valid_lst))
print("Max:", max(valid_lst))
print("Sum:", sum(valid_lst))
