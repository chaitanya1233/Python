"""
Topic   : Test 02 — Number & Digit Manipulation
Date    : December 22, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Difference Between Two Lists (A - B)
# ===========================================================

def list_diff(A, B):
    common = set(A).intersection(set(B))
    diff_a = [i for i in A if i not in common]
    diff_b = [i for i in B if i not in common]
    return diff_a + diff_b

A = [1, 2, 3, 9, 4, 5]
B = [3, 4, 6, 9]
result = list_diff(A, B)
print(f"Difference (A - B) = {result}")

# ===========================================================
# Q2: Count the Number of Digits in a Number
# ===========================================================

def count_digits(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    return len(digits)

print("Number of digits in 9876554:", count_digits(9876554))

# ===========================================================
# Q3: Product of All Digits of a Number
# Input: 234 → Output: 24
# ===========================================================

def digits_product(num):
    product = 1
    num = abs(num)
    while num != 0:
        product *= (num % 10)
        num //= 10
    return product

print(f"Product of digits of 234: {digits_product(234)}")

# ===========================================================
# Q4: Check if a Number is a Palindrome
# ===========================================================

def is_num_palindrome(num):
    s = str(num)
    return "Palindrome" if s == s[::-1] else "Not a palindrome"

print(f"1221 → {is_num_palindrome(1221)}")
print(f"112211 → {is_num_palindrome(112211)}")

# ===========================================================
# Q5: Sum Only Odd Digits of a Number
# Input: 12345 → Output: 9 (1+3+5)
# ===========================================================

def sum_odd_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        if digit % 2 != 0:
            total += digit
        num //= 10
    return total

print(f"Sum of odd digits in 12345: {sum_odd_digits(12345)}")
