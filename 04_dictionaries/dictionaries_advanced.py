"""
Topic   : Advanced Dictionaries — CRUD, Sorting, Merging & Nested
Date    : December 13, 2025
Author  : Chaitanya

Note    : Generator examples have been moved to
          06_generators_and_comprehensions/generators_advanced_practice.py
"""

# ===========================================================
# SECTION 1: Min & Max of Dictionary Values
# ===========================================================

dict1 = {'a': 12, 'b': 32, 'c': 1}

# Minimum value
min_value_key = min(dict1, key=dict1.get)
min_value = dict1[min_value_key]
print("The minimum value from the dictionary is:", min_value)

# Maximum value
max_value_key = max(dict1, key=dict1.get)
max_value = dict1[max_value_key]
print("The maximum value from the dictionary is:", max_value)

# ===========================================================
# SECTION 2: Sum of Dictionary Values
# ===========================================================

# Using a loop
dict1 = {'a': 12, 'b': 32, 'c': 1}
total = 0
for i in dict1.values():
    total = total + int(i)
print("Total is:", total)

# Using list comprehension / generator
dict1 = {'a': 12, 'b': 32, 'c': 1}
total = sum([int(i) for i in dict1.values()])
print("Total is:", total)

# ===========================================================
# SECTION 3: Unpacking a Nested Dictionary
# ===========================================================

student = {
    "name": "Chaitanya",
    "marks": {
        "maths": 85,
        "science": 90,
        "english": 78
    }
}

print(student['name'])
print(student['marks'])

# Unpacking nested dictionary
marks = student['marks']
print(marks)
print(marks.items())
print(marks.values())

math = marks['maths']
print(f"You got {math} marks in maths")

english = marks['english']
print(f"You got {english} marks in english")

science = marks['science']
print(f"You got {science} marks in science")

# ===========================================================
# SECTION 4: CRUD Operations
# ===========================================================

# Update a value
emp = {"Amit": 52000, "Neha": 68000, "Ravi": 45000}
emp['Ravi'] = 50000
print(emp.values())

# Add a new key-value pair
emp = {"Amit": 52000, "Neha": 68000, "Ravi": 45000}
emp['Chaitanya'] = 60000
print(emp.items())

# Safe fetch with .get() — no KeyError if key missing
print(emp.get("amit"))   # None (case-sensitive)

# Check if key exists
print("Neha" in emp)

# ===========================================================
# SECTION 5: Sorting Dictionaries
# ===========================================================

# Sort by values (descending)
student = {"Amit": 80, "Neha": 34, "Ravi": 44}
sorted_by_desc = dict(sorted(student.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_desc)

# Sort by keys (alphabetically / numerically)
products = {1: "Soap", 2: "Nirma", 3: "Peanuts"}
sorted_by_product_names = dict(sorted(products.items(), key=lambda item: item[0], reverse=True))
print(sorted_by_product_names)

# Sort by values, then keys for tie-breaking
dict1 = {"A": 42, "C": 12, "B": 42}
sorted_by_keys = dict(sorted(dict1.items(), key=lambda item: item[0]))
print(sorted_by_keys)

sorted_by_values = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_by_values)

# ===========================================================
# SECTION 6: Dictionary Min/Max on Prices
# ===========================================================

dict2 = {"pen": 20, "book": 40, "eraser": 5}

min_item_key = min(dict2, key=dict2.get)
min_item_price = dict2[min_item_key]
print(min_item_price)

max_item_key = max(dict2, key=dict2.get)
max_item_price = dict2[max_item_key]
print(max_item_price)

# ===========================================================
# SECTION 7: Deep Dictionary Analysis — Practice Problem
# ===========================================================

"""
Question: Employee Analysis
- Remove employees whose age is None
- Sort remaining employees by salary (descending) — use loops, not sorted()
- Return a new dict: {emp_id: {name, salary}}
- Print employee with maximum number of skills
"""

employees = {
    "emp1": {"name": "Amit",  "age": 28,   "salary": 55000, "skills": ["python", "ml"]},
    "emp2": {"name": "Neha",  "age": 24,   "salary": 48000, "skills": ["sql", "excel"]},
    "emp3": {"name": "Rahul", "age": 30,   "salary": 70000, "skills": ["python", "ds", "ml"]},
    "emp4": {"name": "Pooja", "age": None, "salary": 45000, "skills": []}
}

# Remove employees with age None
active_employees = {k: v for k, v in employees.items() if v["age"] is not None}

# Sort by salary descending (manual bubble-sort style on items)
emp_list = list(active_employees.items())
for i in range(len(emp_list)):
    for j in range(i + 1, len(emp_list)):
        if emp_list[i][1]["salary"] < emp_list[j][1]["salary"]:
            emp_list[i], emp_list[j] = emp_list[j], emp_list[i]

# Build new dictionary with only name and salary
result = {k: {"name": v["name"], "salary": v["salary"]} for k, v in emp_list}
print(result)

# Employee with maximum skills
max_skills_emp = max(active_employees, key=lambda k: len(active_employees[k]["skills"]))
print("Employee with most skills:", max_skills_emp,
      "—", active_employees[max_skills_emp]["skills"])

# ===========================================================
# SECTION 8: Grocery Billing App (Dictionary + match-case)
# ===========================================================

def add_item(item):
    item_name = input("Enter the product name: ")
    price = input("Enter the price of the product: ")
    item[item_name] = price
    print("Item added successfully.")

def update_item(item):
    item_name = input("Enter item name you want to update: ")
    price = int(input("Enter the price you want to update: "))
    item[item_name] = price
    print("The item updated successfully.")

def view_item(item):
    print("Following are items present in grocery along with their prices:")
    for key, value in item.items():
        print(f"{key}:{value}")

# Uncomment below to run the interactive grocery app:
# items = dict()
# while True:
#     choice = int(input("Enter your choice (1-Add, 2-Update, 3-View, 4-Exit): "))
#     match choice:
#         case 1: add_item(items)
#         case 2: update_item(items)
#         case 3: view_item(items)
#         case 4: break
