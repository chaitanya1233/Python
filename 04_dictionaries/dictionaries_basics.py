"""
Topic   : Dictionaries — Basics, Methods & Enumeration
Date    : December 10-11, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Dictionary Introduction
# ===========================================================

dict1 = {"Brand": "Maruti", "Model": "Mustang", "Year": 1978}
print(dict1)
print(type(dict1))

# Get specific values
dict1.get("Brand")
dict1.get("year")   # Returns None — key is case-sensitive

# keys(), values(), items()
car = {"Brand": "Maruti", "Model": "Mustang", "Year": 1986}
print(car.keys())
print(type(car.keys()))
print(car.values())
print(car.items())

# ===========================================================
# SECTION 2: Adding Elements
# ===========================================================

# Way 1: via key assignment
car['Fuel_type'] = "Petrol"
print(car)

# Way 2: update() method
car = {"Brand": "Maruti", "Model": "Mustang", "Year": 1983}
car.update({"Oil": "Diesel"})
print(car)

car.update({"Price": 50000})
print(car)

car['Price'] = 300000
print(car)

# ===========================================================
# SECTION 3: Removing Elements
# ===========================================================

car = {"Brand": "Maruti", "Model": "Mustang", "Year": 1983}
car.pop("Brand")
print(car)

# ===========================================================
# SECTION 4: Iterating Over a Dictionary
# ===========================================================

car = {"Brand": "Maruti", "Model": "Mustang", "year": 1987}

for key, value in car.items():
    print(f"{key}:{value}")

# Another way
for i in car:
    print(f"{i}:{car[i]}")

# ===========================================================
# SECTION 5: Sorting by Keys and Values
# ===========================================================

dct = {'a': 5, 'b': 1, 'c': 4}

sorted_by_keys = dict(sorted(dct.items(), key=lambda item: item[0]))
print(sorted_by_keys)

sorted_by_values = dict(sorted(dct.items(), key=lambda l: l[1]))
print(sorted_by_values)

# Descending order
sorted_by_keys_desc = dict(sorted(dct.items(), key=lambda l: l[0], reverse=True))
print(sorted_by_keys_desc)

sorted_by_values_desc = dict(sorted(dct.items(), key=lambda l: l[1], reverse=True))
print(sorted_by_values_desc)

# ===========================================================
# SECTION 6: Nested Dictionary
# ===========================================================

employees = {
    "emp1": {"Name": "Chaitanya", "Age": 29, "Salary": 55000, "Skills": ["Python", "ml"]},
    "emp2": {"Name": "Arya",      "Age": 25, "Salary": 65000, "Skills": ["sql", "excel"]},
    "emp3": {"Name": "Om",        "Age": 23, "Salary": 55000, "Skills": ["python", "ds", "ml"]},
    "emp4": {"Name": "Saket",     "Age": None, "Salary": 45000, "Skills": []}
}
print(employees)

# ===========================================================
# SECTION 7: enumerate() — Index + Value
# ===========================================================

# Basic iteration (no index)
lst = ['bread', 'milk', 'butter', 'cheese']
for item in lst:
    print(item)

# Using enumerate()
for index, item in enumerate(lst):
    print(f"{index}:{item}")

# Tuple form
for item in enumerate(lst):
    print(item)

# ===========================================================
# SECTION 8: Conditional Logic with enumerate()
# ===========================================================

tasks_by_priority = ['workout', 'diet', 'gaming']

for i, task in enumerate(tasks_by_priority):
    if i == 0:
        print("*" + str.upper(task) + "!")
    else:
        print(f"*{task}")

# Takeaway: enumerate() lets you control loop flow based on index
# even when the values themselves are not what matters.
