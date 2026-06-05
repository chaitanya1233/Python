"""
Topic   : Dictionaries Practice & Function Types Combined
Date    : December 11, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Min/Max Item From a Dictionary (Grocery Price)
# ===========================================================

sorted_dict = {"banana": 40, "apple": 100, "grapes": 120, "mango": 200}

# Get lowest price item for free
free_item_key = min(sorted_dict, key=sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"You will get the lowest price item {free_item_key} ({free_item_value}) for free")

# Get highest priced item for free
max_free_key = max(sorted_dict, key=sorted_dict.get)
max_free_value = sorted_dict[max_free_key]
print(f"You will get {max_free_key} ({max_free_value}) for free!")

# ===========================================================
# SECTION 2: Sort Dictionary in Descending Order
# ===========================================================

sorted_dict = {"banana": 40, "apple": 100, "grapes": 120, "mango": 200}
sorted_by_descending = dict(sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_descending)

# ===========================================================
# SECTION 3: Summing Dictionary Values (with string values)
# ===========================================================

dict1 = {
    'apple': '100',
    'grapes': '120',
    'mango': '200',
    'banana': '40'
}

# Using a loop
total = 0
for value in dict1.values():
    total = total + int(value)
print(total)

# Using a generator expression
total_sum = sum(int(value) for value in dict1.values())
print(total_sum)

# ===========================================================
# SECTION 4: Concatenating Dictionaries
# ===========================================================

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# Using update()
dict1.update(dict2)
print(dict1)

# Using | (pipe) operator
dict1 = dict1 | dict3
print(dict1)

# ===========================================================
# SECTION 5: continue Keyword
# ===========================================================

fruits = ['apple', 'cherry', 'banana']
for i in fruits:
    if i == "banana":
        continue        # Skips this iteration
    else:
        print(i)

# ===========================================================
# SECTION 6: Regular Function — No Arguments
# ===========================================================

def my_function():
    print("Hello, from my function")

my_function()

# ===========================================================
# SECTION 7: Function with Arguments
# ===========================================================

def my_function(name):
    print("Hello", name)

my_function("Ram")

# ===========================================================
# SECTION 8: *args — Arbitrary Arguments
# ===========================================================

def my_function(*args):
    print(args[0] + " " + args[2])

my_function("Tappu", "Sonu", "Goli")

# ===========================================================
# SECTION 9: **kwargs — Keyword Arguments
# ===========================================================

def my_fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

my_fun(first_name="Papalal", mid_name="Mohanlal", last_name="Goyal")
