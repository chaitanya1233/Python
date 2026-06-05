"""
Topic   : Week 1 & 2 Review — Functions, Dictionaries & Numbers
Date    : December 15, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Even or Odd Checker
# ===========================================================

def is_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter any number: "))
is_even_odd(num)

# ===========================================================
# Q2: Sum of Digits of a Number
# ===========================================================

def sum_of_digits(n):
    total = 0
    while n != 0:
        last = n % 10      # extract last digit
        total += last
        n //= 10           # remove last digit
    return total

digit = int(input("Enter any number: "))
total = sum_of_digits(digit)
print("Sum of digits:", total)

# ===========================================================
# Q3: Reverse an Integer
# ===========================================================

def reverse_int(num):
    reversed_str = ""
    temp = num
    while temp != 0:
        last = temp % 10
        reversed_str += str(last)
        temp //= 10
    return int(reversed_str)

digit = 123
rev_num = reverse_int(digit)
print("The reversed number is:", rev_num)

# ===========================================================
# Q4: Sort a Dictionary by Keys and Values
# ===========================================================

data = {'a': 5, 'z': 1, 'c': 4}
print("Original:", data)

sorted_by_keys = dict(sorted(data.items(), key=lambda item: item[0]))
print("Sorted by keys:", sorted_by_keys)

sorted_by_values = dict(sorted(data.items(), key=lambda a: a[1]))
print("Sorted by values:", sorted_by_values)

# ===========================================================
# Q5: Return Minimum Value from Dictionary
# ===========================================================

data = {'a': 5, 'z': 1, 'c': 4}
min_value_key = min(data, key=data.get)
min_value = data[min_value_key]
print("Minimum value:", min_value)

# ===========================================================
# Q6: Sort Dictionary in Reversed Order
# ===========================================================

data = {'a': 5, 'z': 1, 'c': 4}
sorted_in_rev = dict(sorted(data.items(), key=lambda item: item[0], reverse=True))
print("Sorted reversed:", sorted_in_rev)

# ===========================================================
# Q7: Sum of All Values in a Dictionary
# ===========================================================

data = {'a': 5, 'z': 1, 'c': 4}
total = sum(data.values())
print("Sum of values:", total)
