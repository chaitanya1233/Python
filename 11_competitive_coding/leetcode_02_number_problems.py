"""
Topic   : LeetCode-Style Problems 02 — Number Operations & Lists
Date    : December 20, 2025
Author  : Chaitanya
"""

# ===========================================================
# PROBLEM 1: Sum of Digits of a Number
# ===========================================================

def sum_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

num = 123456
print("Sum of digits:", sum_digits(num))

# ===========================================================
# PROBLEM 2: Reverse the Digits of a Number
# ===========================================================

def rev_num(num):
    while num != 0:
        digit = num % 10
        print(digit, end="")
        num //= 10
    print()

print("Reversed digits: ", end="")
rev_num(123)

# ===========================================================
# PROBLEM 3: Find Maximum and Minimum Element from a List
# ===========================================================

def min_max(lst):
    mini = float("inf")
    maxi = float("-inf")
    for i in lst:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return mini, maxi

lst = [0.231, 2, 3, 24, 5]
mini, maxi = min_max(lst)
print("Minimum element:", mini)
print("Maximum element:", maxi)

# ===========================================================
# PROBLEM 4: Sum of Positive and Negative Numbers in a List
# ===========================================================

def sum_pos_neg(lst):
    n_sum = 0
    p_sum = 0
    for i in lst:
        if i >= 0:
            p_sum += i
        else:
            n_sum += i
    return n_sum, p_sum

lst = [-1, -2, -4, 9, 53, 3, -85]
n_sum, p_sum = sum_pos_neg(lst)
print("Sum of negative numbers:", n_sum)
print("Sum of positive numbers:", p_sum)

# ===========================================================
# PROBLEM 5: Local Maxima (Mini Peak Problem)
# ===========================================================

"""
Find elements that are greater than both their neighbors.
"""

lst = [1, 3, 2, 5, 4, 6, 5]
print("Local maxima (peaks):")
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        print(lst[i])
