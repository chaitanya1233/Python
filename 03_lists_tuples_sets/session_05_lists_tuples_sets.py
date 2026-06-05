"""
Topic   : Lists, Tuples & Sets
Session : 05
Date    : December 9, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: List Basics & Methods
# ===========================================================

lst = ['cherry', 'banana', 'apple', 1]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])

# append()
lst = ['cherry', 'banana', 'apple']
lst.append("Mango")
print(lst)

# clear()
lst = ['cherry', 'banana', 'apple']
lst.clear()
print(lst)

# copy()
lst = ['cherry', 'banana', 'apple']
lst2 = lst.copy()
print(lst2)
if id(lst) == id(lst2):
    print("Address are same.")
else:
    print("Address are not same.")

# count()
lst = ['cherry', 'banana', 'apple', 'cherry']
print(lst.count('cherry'))

# extend()
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst = lst1 + lst2
print(lst)
lst1.extend(lst2)
print(lst1)

# insert()
lst = ['cherry', 'cherry', 'banana']
lst.insert(1, 'Mango')
print(lst)

# pop()
lst = ['cherry', 'cherry', 'banana']
lst.pop(1)
print(lst)

# remove()
lst = ['cherry', 'cherry', 'banana']
lst.remove('cherry')
print(lst)

# reverse()
lst = ['cherry', 'cherry', 'banana']
lst.reverse()
print(lst)

# sort()
lst = ['cherry', 'cherry', 'banana']
lst.sort()
print(lst)

# sorted() with key parameter
lst = ['cherry', 'kiwi', 'banana', "apple"]
sorted_lst = sorted(lst, key=len)
print(sorted_lst)

# ===========================================================
# SECTION 2: Nested Lists
# ===========================================================

nested_lst = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print(nested_lst)

# Accessing elements
print(nested_lst[0])          # first inner list
print(nested_lst[1][2])       # specific element
print(nested_lst[-1][-1])     # last element of last list

# Modifying element
nested_lst[1][1] = 'z'
print(nested_lst)

# ===========================================================
# SECTION 3: List Comprehension
# ===========================================================

# Basic
lst = [num for num in range(0, 20)]
print(lst)

# Capitalize names using comprehension
names = ['dada', 'mama', 'kaka']
lst = [name.capitalize() for name in names]
print(lst)

# Iterating over nested list
for sublist in nested_lst:
    print(sublist)

# Flatten a nested list
flat_list = [item for sublist in nested_lst for item in sublist]
print(flat_list)

# Using two for loops
for sublist in nested_lst:
    for item in sublist:
        print(item, end=" ")

# Append a new sublist
nested_lst.append(['new', 'list'])
print(nested_lst)

# Add element inside a sublist
nested_lst[0].append(4)
print(nested_lst)

# Remove element from sublist
nested_lst[1].remove('z')
print(nested_lst)

# ===========================================================
# SECTION 4: Tuples
# ===========================================================

tup = ("apple", "cherry", "banana")
print(tup)
print(type(tup))

# Tuples are immutable — values cannot be changed after creation
# To modify, convert to list first
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Kiwi"

# Convert list back to tuple
x = tuple(y)
print(x)
print(type(x))
print(x[0])

# Joining two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tup1 = tuple1 + tuple2
print(tup1)

# A single value in parentheses is NOT a tuple
t = (3)
print(t, type(t))       # <class 'int'>

# This is a tuple
t = (3,)
print(t, type(t))       # <class 'tuple'>

# ===========================================================
# SECTION 5: Sets
# ===========================================================

# An empty {} creates a dict, not a set
s = {}
print(type(s))           # <class 'dict'>

# Sets: unordered, no duplicate values, immutable elements
s = {1, 2, 3, 2, 3, 4, 3, 2, 2, 2, 3, 4}
print(s)
print(type(s))

s1 = {"Car", True, 4, "Demo"}
print(s1)

# Create an empty set
empty_set = set()
print(type(empty_set))

# Accessing values of a set (via loop only)
x = set([1, 2, 3, 4, 5, 6, 7, 7, 87, 4])
for i in x:
    print(i)

# Check membership
items = {"A", "B", "C", "D", 5, 6, 7, 23, 234}
if 4 in items:
    print("Yes")
else:
    print("No")

# Union and Intersection
a = set([1, 2, 3, 4, 5])
b = set([3, 2, 4, 6, 7, 9])
print("Intersection:", a.intersection(b))
print("Union:", a.union(b))

# Symmetric difference
a = a.symmetric_difference(b)
print(a)

# Subset and Superset
print(a.issuperset(b))
print(b.issubset(a))

# Set operations: add, remove, pop, del, clear
a = {1, 2, 3, 4, 5}
a.add("Chaitanya")
print(a)

a = {1, 2, 3, 4, 5}
a.clear()
print(a)
