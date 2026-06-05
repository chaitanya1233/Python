"""
Topic   : HackerRank Problems — Strings, Sets, Runner-Up Score
Date    : December 18–21, 2025
Author  : Chaitanya
"""

# ===========================================================
# PROBLEM 1: Runner-Up Score
# Find the second maximum value from a list.
# ===========================================================

def runner_up_score(arr):
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

# Input format (HackerRank style):
# n = int(input())
# arr = list(map(int, input().split()))
arr = [2, 3, 6, 6, 5]
print("Runner-up score:", runner_up_score(arr))

# ===========================================================
# PROBLEM 2: Nested Lists — Second Lowest Score
# ===========================================================

"""
Given a list of [name, score] pairs, find all students
with the second lowest score.
"""

def second_lowest_students(student_lst):
    # Convert to dict and sort by score
    d = dict(student_lst)
    d_sorted = dict(sorted(d.items(), key=lambda a: a[1]))
    sorted_lst = list(d_sorted.items())

    # Find second lowest score value
    if len(sorted_lst) < 2:
        return []
    second_lowest = sorted_lst[1][1]

    # Collect all students with that score
    result = [name for name, score in sorted_lst if score == second_lowest]
    return sorted(result)

students_input = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.12],
    ["Akriti", 41],
    ["Harsh", 39]
]
for name in second_lowest_students(students_input):
    print(name)

# ===========================================================
# PROBLEM 3: Capitalize Words in a Sentence
# ===========================================================

def capitalize_words(s):
    words = s.split(" ")
    return "".join(word.capitalize() for word in words)

result = capitalize_words("hello world")
print(result)

# ===========================================================
# PROBLEM 4: String Validation
# ===========================================================

# if __name__ == '__main__':
#     s = input()
#     print(s.isalnum())
#     print(s.isalpha())
#     print(s.isdigit())
#     print(s.islower())
#     print(s.isupper())

s = "Hello123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())

# ===========================================================
# PROBLEM 5: Set Operations — Add, Update, Remove, Discard
# ===========================================================

# Create a set from a list
lst = [1, 2, 3, 4]
s = set(lst)
print(s)

# Modify the set
my_set = set(['a', 'b', 'c'])
my_set.add("d")
print(my_set)

my_set.add("a")        # no effect — already exists
print(my_set)

# add a tuple element
my_set.add((2, 'A'))
print(my_set)

# update() — add multiple elements
my_set.update({1, 6}, [5, 13])
print(my_set)

# remove() raises KeyError if not found
# discard() does NOT raise error
my_set.discard(1)
print(my_set)

# map() to convert list of strings to integers
lst = ['1', '23', '4', '3', '4', '45', '4', '43']
new_lst = list(map(int, lst))
print(new_lst)

# ===========================================================
# PROBLEM 6: Mutable String (Change a Character)
# ===========================================================

name = "Chaitnaya"
lst = list(name)
lst[4] = 'C'
name = "".join(lst)
print(name)
