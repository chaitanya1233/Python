"""
Topic   : Practice Sheet 03 — String Operations & Methods
Date    : December 4, 2025
Author  : Chaitanya
"""

# ===========================================================
# Q1: Assign Three Variables in One Line
# ===========================================================

x, y, z = 10, 20, 30
print(x, y, z)

# ===========================================================
# Q2: Global vs Local Variable Demo
# ===========================================================

name = "I am global variable, Chaitanya"

def my_name():
    name = "I am local variable, Arya"   # local takes priority
    print(name)

my_name()

# ===========================================================
# Q3: Print Characters from Index 2 to 8
# ===========================================================

input_str = input("Enter any string: ")
print("The characters from index 2 to 8 are:", input_str[2:9])

# ===========================================================
# Q4: Reverse a String Using Slicing
# ===========================================================

name = "Chaitanya"
print("The reversed string is:", name[::-1])

# ===========================================================
# Q5: First 3 and Last 3 Characters
# ===========================================================

x = "I love Someone"
print("First 3 characters are:", x[:3])
print("Last 3 characters are:", x[-3:])

# ===========================================================
# Q6: Slice With Step Size 2
# ===========================================================

y = "I eat mango"
print("The string slice using step 2 is:", y[::2])

# ===========================================================
# Q7: Convert to UPPERCASE and Lowercase
# ===========================================================

sentence = "Hello Shivani, How are you?"
print("Uppercase is:", sentence.upper())
print("Lowercase is:", sentence.lower())

# ===========================================================
# Q8: Strip Spaces — lstrip, rstrip, strip
# ===========================================================

word = "Deon Deselva. "
print("Word before rstrip:", word)
print("Word after rstrip:", word.rstrip())

word = " Saket Gokhle"
print("Word before lstrip:", word)
print("Word after lstrip:", word.lstrip())

# ===========================================================
# Q9: Replace Word in a String
# ===========================================================

sentence = "Hello, I am learning Python."
sentence = sentence.replace("Python", "Java")
print("After replacement:", sentence)

# ===========================================================
# Q10: Split a String on "_"
# ===========================================================

x = "Chaitanya_Jagannath_Kale"
print("After splitting:", x.split("_"))
