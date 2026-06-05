"""
Topic   : Number & List Problems
Date    : December 22, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Unpack List from a Given Index
# ===========================================================

lst = [13, 4, 6, 8, 9]
num = int(input("Enter the number from the list: "))
if num in lst:
    start = lst.index(num)
    print(*lst[start:])
else:
    print("Number not in list")

# ===========================================================
# Q2: Search Value in List — Correct Logic
# ===========================================================

lst = [13, 4, 6, 8, 9]

def search_num(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return 'Value found'
    return 'Value not found'

num = int(input("Enter the number you want to search: "))
print(search_num(lst, num))

# ===========================================================
# Q3: Count Vowels in a String
# ===========================================================

input_string = input("Enter your string: ").lower()

def count_vowels(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

print("Vowel count:", count_vowels(input_string))

# ===========================================================
# Q4: Sum of Numbers Divisible by 5 or 7
# ===========================================================

lst = [1, 2, 5, 15, 7, 42]
total = sum(i for i in lst if i % 5 == 0 or i % 7 == 0)
print("Sum of numbers divisible by 5 or 7:", total)

# ===========================================================
# Q5: Check for Duplicate Elements in a List
# ===========================================================

def has_duplicate(lst):
    seen = set()
    for i in lst:
        if i in seen:
            return True
        seen.add(i)
    return False

print("Has duplicates:", has_duplicate([1, 2, 3, 2]))
print("Has duplicates:", has_duplicate([1, 2, 3, 4]))

# ===========================================================
# Q6: Count Digits of a Number
# ===========================================================

def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

num = 1234
print("Digit count:", count_digits(num))
