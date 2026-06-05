"""
Topic   : Practice Sheet 11 — List Unpacking & Search
Date    : December 23, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: List Unpacking Using * Operator
# ===========================================================

lst = [1, 2, 34, 54, 34, 45, 3, 42]
start = int(input("Enter the index from which you want to unpack: "))
print(*lst[start:])

# ===========================================================
# Q2: Search for an Element in a List
# ===========================================================

lst = [1, 2, 3, 4, 5, 6, 7]

def found_or_not(lst, ele):
    for i in range(len(lst)):
        if lst[i] == ele:
            return "Element found"
    return "Element not found"

ele = int(input("Enter the element you want to search: "))
result = found_or_not(lst, ele)
print(result)

# ===========================================================
# Q3: Count the Number of Vowels
# ===========================================================

string = input("Enter your string: ")

def count_vowels(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

print("Number of vowels:", count_vowels(string))
