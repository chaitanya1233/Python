"""
Topic   : Dictionaries, Sorting & Lambda Functions
Session : 06
Date    : December 10, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: Dictionary Basics
# ===========================================================

dict1 = {'Brand': "Maruti", 'model': "2345", "year": 2011}
print(dict1)
print(len(dict1))
print(type(dict1))

# Access value by key
dict1.get("Brand")
dict1.keys()

car = {
    "Brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)

# ===========================================================
# SECTION 2: CRUD Operations on Dictionary
# ===========================================================

# Add element
car['color'] = "white"
print(car)

# Check length
print(len(car))

# pop() — remove a key
car.pop("Model")
print(car)

# ===========================================================
# SECTION 3: Iterating Over a Dictionary
# ===========================================================

car = {"Brand": "Ford", "Model": "Mustang", "year": 1964}

# Keys only
for x in car:
    print(x)

# Values only
for x in car:
    print(car[x])

# Keys and Values using items()
for key, value in car.items():
    print("%s = %s" % (key, value))

for key, value in car.items():
    print(f"{key}:{value}")

# ===========================================================
# SECTION 4: Copying a Dictionary
# ===========================================================

car = {"Brand": "Ford", "Model": "Mustang", "Year": "1976"}
car2 = car.copy()
print(car2)
print(id(car) == id(car2))   # False — different objects

thisdict = {"Brand": "Ford", "Model": "Mustang", "Year": "1976"}
dict1 = dict(thisdict)
print(dict1)
print(id(dict1) == id(thisdict))   # False

# ===========================================================
# SECTION 5: Nested Dictionary
# ===========================================================

our_family = {
    "child1": {
        "Name": "Ram",
        "DoB": "21-05-2008"
    },
    "child2": {
        "Name": "Sham",
        "DoB": "01-01-2008"
    }
}
print(our_family)

# ===========================================================
# SECTION 6: Dictionary Methods
# ===========================================================

# clear()
car = {"Brand": "Ford", "Model": "Mustang", "year": "1976"}
car.clear()
print(car)

# fromkeys()
x = {"key1", "key2", "key3"}   # set of keys
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# get()
car = {"Brand": "Ford", "Model": "Mustang", "Year": "1976"}
model = car.get("Model")
print(model)

# items(), keys(), values()
print(car.items())
print(car.keys())
print(car.values())

# update()
car.update({"Color": "White"})
print(car)

# ===========================================================
# SECTION 7: Sorting a Dictionary
# ===========================================================

data = {'b': 2, 'a': 5, 'c': 1}

# Sort by keys (ascending)
sort_by_keys = dict(sorted(data.items()))
print(sort_by_keys)

# Sort by values (ascending)
sort_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print(sort_by_values)

# ===========================================================
# SECTION 8: Lambda Functions
# ===========================================================

# Regular function
def add(a):
    return a + 10

print(add(20))

# Lambda equivalent
add = lambda a: a + 10
print(add(20))
