"""
Topic   : Test 01 — Lists, Dictionary Comprehension & String Reversal
Date    : December 15, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Check If a List Has at Least One Common Member (Duplicate)
# ===========================================================

def has_common_member(lst):
    orig_len = len(lst)
    unique_len = len(set(lst))
    return orig_len != unique_len

lst = [1, 12, 3, 1, 4, 5, 2]
output = has_common_member(lst)
print("Has common member:", output)

# ===========================================================
# Q2: Add 6 to Each Element Using List Comprehension
# ===========================================================

lst = [i + 6 for i in range(1, 6)]
print(lst)

# ===========================================================
# Q3: Reverse a String
# ===========================================================

def str_reverse(st):
    rev_str = ""
    for i in st[::-1]:
        rev_str += i
    return rev_str

st = input("Enter the string you want to reverse: ")
rev_str = str_reverse(st)
print("The reversed string is:", rev_str)

# Alternate (one-liner)
rev = st[::-1]
print("The reversed string (slicing) is:", rev)

# ===========================================================
# Q4: Iterate Over a Dictionary Using a Loop
# ===========================================================

car = {
    'Brand': 'Maruti',
    'Model': 'Mustang',
    'year': '1987'
}
print("The dictionary elements are:")
for key, value in car.items():
    print(f"{key}:{value}")

# ===========================================================
# Q5: Dictionary Comprehension — Filter by Value
# ===========================================================

current_dict = {
    "person1": 1000,
    "person2": 3000,
    "person3": 4000,
    "person4": 4300,
    "person5": 500
}

# Keep only key-value pairs where value > 2000
new_dict = {key: value for key, value in current_dict.items() if value > 2000}
print(new_dict)
