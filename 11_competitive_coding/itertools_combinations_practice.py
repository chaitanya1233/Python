"""
Topic   : External Practice — itertools: combinations & combinations_with_replacement
Date    : December 17, 2025
Author  : Chaitanya
"""

from itertools import combinations, combinations_with_replacement

# ===========================================================
# PROBLEM 1: Leap Year Check
# ===========================================================

def is_leap(year):
    """
    Standard leap year logic:
    - Divisible by 4       → leap year candidate
    - Divisible by 100     → NOT a leap year
    - Divisible by 400     → IS a leap year (overrides 100 rule)
    """
    leap = False
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True
    return leap

print("1992 is leap:", is_leap(1992))
print("1900 is leap:", is_leap(1900))
print("2000 is leap:", is_leap(2000))

# ===========================================================
# PROBLEM 2: All Combinations of 2 from a String
# ===========================================================

s = "HACK"
s = sorted(s)
print("Combinations of 2 from 'HACK':")
for combo in combinations(s, 2):
    print("".join(combo))

# ===========================================================
# PROBLEM 3: All Combinations Up to Size k
# ===========================================================

"""
Print all possible combinations up to size 3
of a given string in lexicographic order.
"""

string = "Chaitanya"
s = sorted(string)
count = 0
for i in range(1, 4):
    for c in combinations(s, i):
        print("".join(c))
        count += 1
print("Total combinations:", count)

# ===========================================================
# PROBLEM 4: Combinations From a List of Numbers
# ===========================================================

"""
combinations = no repeated elements in each combination
(unique pairs only)
"""

lst = sorted([3, 42, 1, 4, 3, 656, 756])
print("Combinations (no repetition) of size 2:")
for combo in combinations(lst, 2):
    print(combo)

# ===========================================================
# PROBLEM 5: Combinations With Replacement
# ===========================================================

"""
combinations_with_replacement = repeated elements allowed
e.g., (A, A), (B, B) are valid
"""

# s, k = input().split()
# k = int(k)
s = "AB"
k = 2
s = sorted(s)
print(f"\nCombinations with replacement (size {k}) from '{s}':")
for combo in combinations_with_replacement(s, k):
    print("".join(combo))
