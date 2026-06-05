"""
Topic   : Practice Sheet 04 — Lists, Comprehensions, Tuples & Sets
Date    : December 5–7, 2025
Author  : Chaitanya
"""

# ===========================================================
# PART A: Smart Attendance System
# ===========================================================

stud = dict()

def add_student():
    enr_no = int(input("Enter enrollment number of student: "))
    name = input("Enter name of the student: ")
    status = input("Is student Present or Absent? ")
    stud[enr_no] = [name, status]
    print(stud.items())

def get_student_attendance():
    enr_no = int(input("Enter enrollment number to get attendance status: "))
    if enr_no in stud:
        print("Attendance status:", stud.get(enr_no))
    else:
        print("Please enter a valid enrollment number.")

# add_student()
# get_student_attendance()

# ===========================================================
# PART B: List Basics
# ===========================================================

student = ['Arya', 'Chaitanya', 'Om']
print(student)
print(type(student))

# List constructor
l1 = list("Chaitanya")
l2 = list([1, 2, 3, 4, 5])
l3 = list(l2)
print(l1, l2, l3)

# Accessing a list
name = ["A", "B", "C", "D"]
print(name[0])
print(name[-1])
print(name[:])
print(name[::-1])

# Inserting elements
arr = [1, 2, 3, 4, 5]
arr.append(10)
print(arr)
arr.insert(0, "Om")
print(arr)

# Membership check
marks = [3, 5, 6]
if 7 in marks:
    print("Yes")
else:
    print("No")

# ===========================================================
# PART C: List Slicing — Jump Index
# ===========================================================

colors = ["Red", "Yellow", "Blue", "Orange"]
print(colors[1:3])
print(colors[1:3:1])

nums = [18, 293, 92, 843, 294, 2234, 45, 4]
print(nums[1:8])
print(nums[1:8:2])

# ===========================================================
# PART D: List Comprehension Problems
# ===========================================================

# Squares of 1 to 10
square_num = [i * i for i in range(1, 11)]
print(square_num)

# Uppercase strings
colors_list = ["red", "yellow", "blue", "pink", "orange"]
upper_colors = [i.upper() for i in colors_list]
print(upper_colors)

# Word lengths
lengths = [len(i) for i in upper_colors]
print(lengths)

# First letter of each word
first_letters = [i[0] for i in upper_colors]
print(first_letters)

# Positive numbers only
nums = [-1, 3, 4, -3, 4, -23, 23, 42, -323]
pos_num = [i for i in nums if i > 0]
print(pos_num)

# Fruits containing letter "a"
fruits = ["Mango", "Apple", "Guava", "Orange", "Kivi", "papaya", "Berry", "Aster"]
fruits_with_a = [i for i in fruits if "a" in i]
print(fruits_with_a)

# Even and odd from a number list
nums = [1, 2, 36, 56, 67, 3, 56, 4, 2, 3, 2454, 534, 23213, 234, 213, 2334, 1232]
even_nums = [i for i in nums if i % 2 == 0]
odd_nums = [i for i in nums if i % 2 != 0]
print(even_nums)
print(odd_nums)

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5]]
flattened = [i for item in nested for i in item]
print(flattened)

# Numbers from 1–50 divisible by both 3 and 5
nums_div = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
print(nums_div)

# ===========================================================
# PART E: List Methods Demonstration
# ===========================================================

# append, sort, reverse, insert, index, count, extend
ls = [1, 4, 3, 12, 999, 544, 45, 65]
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)

ls = [1, 2, 3, 4, 5]
ls.reverse()
print(ls)

ls = [10, 20, 30, 40]
ls.insert(3, 999)
print(ls)

ls = [89, 4393, 3, 4, 12, 45]
x = ls.index(12)
print("Index of 12:", x)

fruits = ["Papaya", "Apple", "Apple", "Banana", "Kivi"]
print("Apple count:", fruits.count("Apple"))

l = [1, 2, 3, 4, 5, 6]
m = [10, 20, 30, 50, 4000]
l.extend(m)
print(l)

# ===========================================================
# PART F: Tuple Practice
# ===========================================================

tup = (1, 4, 6, 16, 22)
print(tup[0])
print(tup[::-1])
print(tup[4:-5])
print(len(tup))

# Slicing creates a new object
tup1 = tup[1:4]
print(id(tup1) == id(tup))   # False

# ===========================================================
# PART G: Set Operations
# ===========================================================

a = set([1, 2, 3, 4, 5])
b = set([3, 2, 4, 6, 7, 9])
print("Intersection:", a.intersection(b))
print("Union:", a.union(b))

sym_diff = a.symmetric_difference(b)
print("Symmetric difference:", sym_diff)

a = {1, 2, 3, 4, 5}
a.clear()
print("After clear:", a)
