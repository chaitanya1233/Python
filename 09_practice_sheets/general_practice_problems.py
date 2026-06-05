"""
Topic   : General Practice Problems — Lists, Strings & Numbers
Date    : December 28, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Find Element in List — Return Index or "Not Found"
# ===========================================================

def find_element(lst, ele):
    for i in range(len(lst)):
        if lst[i] == ele:
            print(f"The element {lst[i]} is present at index {i}")
            return
    print("Not found")

lst = [1, 2, 3, 4, 5]
ele = int(input("Enter element to search: "))
find_element(lst, ele)

# ===========================================================
# Q2: Print All Elements After a Given Number
# ===========================================================

def print_elements_after(lst, num):
    print(lst[lst.index(num):])

lst = [10, 20, 30, 40, 50]
print_elements_after(lst, 20)

# ===========================================================
# Q3: Count How Many Times a Number Appears
# ===========================================================

def count_duplicates(lst, num):
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
    return count

lst = [1, 11, 12, 12, 1, 23, 34, 4, 4, 3, 2, 2, 1, 2, 2, 1]
num = 2
count = count_duplicates(lst, num)
print(f"The number of times {num} appears: {count}")

# ===========================================================
# Q4: Find Max and Min Without Built-in Functions
# ===========================================================

def min_max(lst):
    mini = lst[0]
    maxi = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]
        elif lst[i] < mini:
            mini = lst[i]
    return mini, maxi

lst = [1, -2, 3, 7, 5, 6]
mini, maxi = min_max(lst)
print("Minimum element:", mini)
print("Maximum element:", maxi)

# ===========================================================
# Q5: Count Vowels and Consonants in a String
# ===========================================================

def count_vowels_consonants(string):
    vowel_count = 0
    conso_count = 0
    for i in range(len(string)):
        if string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        else:
            conso_count += 1
    return vowel_count, conso_count

string = "Chaitanya"
vc, cc = count_vowels_consonants(string)
print("Vowel count:", vc)
print("Consonant count:", cc)

# ===========================================================
# Q6: Count Digits of a Number
# ===========================================================

def count_digits(num):
    count = 0
    while num != 0:
        num %= 10
        count += 1
        num //= 10
    return count

print("Digits in 12334:", count_digits(12334))

# ===========================================================
# Q7: Sum of Digits of a Number
# ===========================================================

def sum_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

print("Sum of digits of 8742:", sum_digits(8742))

# ===========================================================
# Q8: Count Even and Odd Digits in a Number
# ===========================================================

def count_even_odd_digits(num):
    even = 0
    odd = 0
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even, odd

num = 123456
even, odd = count_even_odd_digits(num)
print(f"(Even digits : Odd digits) = {even}:{odd}")
