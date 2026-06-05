"""
Topic   : String Methods, Formatting & Boolean
Session : 04
Date    : December 8, 2025
Author  : Chaitanya
"""

# ===========================================================
# SECTION 1: String find() and Concatenation
# ===========================================================

x = "This is python and it is very powerful"
print(x.find("python"))

address = "4/116 Sunder Apartments, Suyognagar"
print(address.find("Sunder"))
print(address[6:22])

# String concatenation
x = "Hello"
y = "World"
print(x + y)
print(x + " " + y)     # with white space

# ===========================================================
# SECTION 2: String Formatting
# ===========================================================

# f-strings
x = 36
print(f"My name is Anthony and my age is {x}")

quantity = 3
item_no = 54
price = 67
print(f"I want {quantity} pieces and item number is {item_no}, its price is {price}")

# Positional arguments with .format()
my_order = "I want {} pieces and item number is {}, its price is {}"
print(my_order.format(quantity, item_no, price))

# Reordering positional arguments
my_order = "I want {2} items and its item number is {1}, its price is {0}"
print(my_order.format(price, item_no, quantity))

# ===========================================================
# SECTION 3: Escape Characters
# ===========================================================

text = "This is fun fare and it has got big \" round rigo\""
print(text)

# ===========================================================
# SECTION 4: Python Booleans
# ===========================================================

print(10 > 9)
print(10 == 10)
print(10 == 9.9999)
print(9 == 9.0)

a = 20
b = 10
if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

print(a == b)
print(a != b)

# ===========================================================
# SECTION 5: Operator Precedence (PEMDAS)
# Parenthesis | Exponent | Multiply | Divide | Add | Subtract
# ===========================================================

print(3 * 3 + 3 / 3 - 3)

# ===========================================================
# SECTION 6: Identity Operators
# ===========================================================

a = 20
b = 10
print(a is b)
print(a is not b)

# ===========================================================
# SECTION 7: Lists — Introduction
# ===========================================================

lst1 = ["Cherry", "Banana", "Apple"]
print(lst1)
print(type(lst1))
print(lst1[0])
print(lst1[2])

lst = ["Cherry", 1, 1.3]
print(lst)

# append
lst1.append("Mango")
print(lst1)

# clear the list
lst1.clear()
print(lst1)

# ===========================================================
# SECTION 8: Palindrome Check Function
# ===========================================================

def is_palindrome(input_string):
    if input_string == "":
        print("You entered a wrong input")
        return False
    string = input_string[::-1]
    if string == input_string:
        return True
    return False

input_string = input("Enter your string: ")
output = is_palindrome(input_string)
if output:
    print("Given string is palindrome")
else:
    print("The given string is not palindrome")

# ===========================================================
# SECTION 9: Sort Hyphen-Separated String
# ===========================================================

def sorted_colors(input_string):
    parts = input_string.split("-")
    sorted_parts = sorted(parts)
    return '-'.join(sorted_parts)

input_string = "red-green-blue-yellow"
sorted_str = sorted_colors(input_string)
print("The sorted string is:", sorted_str)
