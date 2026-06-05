"""
Topic   : Function-Based Problems — Logic & Algorithms
Date    : December 18, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Leap Year Checker
# ===========================================================

def is_leap_year(year):
    """
    Rules:
    - Divisible by 4       → candidate leap year
    - Divisible by 100     → NOT a leap year (exception)
    - Divisible by 400     → IS a leap year (exception to the exception)
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

is_leap_year(1990)
is_leap_year(2000)
is_leap_year(1900)

# ===========================================================
# Q2: Credit Score Category
# ===========================================================

score = int(input("Enter your credit score: "))
if score < 400 or score > 850:
    print("Invalid score")
elif 400 <= score <= 599:
    print("General")
elif 600 <= score <= 799:
    print("Deluxe")
elif 800 <= score <= 850:
    print("Premium")

# ===========================================================
# Q3: Reverse Digits of a Number
# ===========================================================

# Method 1: Using modulus and division
num = int(input("Enter a number: "))
temp = num
while temp != 0:
    digit = temp % 10
    print(digit, end="")
    temp = temp // 10
print()

# Method 2: Using string slicing (cleaner)
def reverse_num_digits(num):
    return int(str(num)[::-1])

print("Reversed number:", reverse_num_digits(1234))

# ===========================================================
# Q4: Sum of Even Numbers in a List
# ===========================================================

# Method 1: List comprehension
total = sum(i for i in range(1, 11) if i % 2 == 0)
print("Sum of even numbers (1-10):", total)

# Method 2: Loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in lst:
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

# ===========================================================
# Q5: Sum of Digits of a Number
# ===========================================================

num = int(input("Enter any number: "))
total = 0
temp = num
while temp != 0:
    digit = temp % 10
    total += digit
    temp //= 10
print(f"The total digit sum of {num} is {total}")

# Alternative — string-based approach
def add_digits_num(num):
    return sum(int(d) for d in str(num))

print("Total (string method):", add_digits_num(123))

# ===========================================================
# Q6: Sum of Digits That Are 3, 6, or 9
# ===========================================================

num = int(input("Enter the number: "))
total = 0
temp = num
while temp != 0:
    digit = temp % 10
    if digit in (3, 6, 9):
        total += digit
    temp //= 10
print(f"Sum of digits 3, 6, 9 from {num}: {total}")

# ===========================================================
# Q7: Sum of Positive and Negative Numbers in a List
# ===========================================================

def return_total(lst):
    pos_total = 0
    neg_total = 0
    for i in lst:
        if i >= 0:
            pos_total += i
        else:
            neg_total += i
    return pos_total, neg_total

lst = [0, -1, -2, 4, 5, 6, -3, 20]
p, n = return_total(lst)
print(f"Sum of positives: {p}")
print(f"Sum of negatives: {n}")

# ===========================================================
# Q8: Local Maxima (Mini Peak Problem)
# ===========================================================

"""
An element is a local maximum if it is greater
than both its immediate neighbors.
"""

lst = [1, 3, 2, 5, 4, 6, 5]
print("Local maxima (peaks):")
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        print(lst[i])

# ===========================================================
# Q9: Find Max and Min Without Built-ins
# ===========================================================

def max_min_elements(lst):
    max_ele = lst[0]
    min_ele = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_ele:
            max_ele = lst[i]
        elif lst[i] < min_ele:
            min_ele = lst[i]
    return max_ele, min_ele

lst = [-1, 2, 4, 3, 54, 344, 65, 3, 343]
max_val, min_val = max_min_elements(lst)
print(f"Maximum element: {max_val}")
print(f"Minimum element: {min_val}")
