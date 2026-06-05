"""
Topic   : Practice Sheet 05 — String & List Problems
Date    : December 8, 2025
Author  : Chaitanya

Note    : practiceSheet-5.py and practiceSheet-5(Related to session 4).py
          were identical files. Consolidated here as a single clean sheet.
"""

import random

# ===========================================================
# Q1: Sort Country Names (Hyphen Format)
# ===========================================================

countries = "india-japan-china-brazil-france"

def sorted_country(countries):
    parts = countries.split("-")
    parts = sorted(parts)
    return "-".join(parts)

sorted_countries = sorted_country(countries)
print("The sorted countries are:", sorted_countries)

# ===========================================================
# Q2: Remove Duplicate Colors
# Input : "red-blue-green-blue-red-yellow"
# Output: sorted unique colors in hyphen format
# ===========================================================

colors = "red-blue-green-blue-red-yellow"

def remove_duplicate_colors(colors):
    colors_list = colors.split("-")
    unique_sorted = sorted(set(colors_list))
    return '-'.join(unique_sorted)

unique_sorted_colors = remove_duplicate_colors(colors)
print("The sorted unique colors:", unique_sorted_colors)

# ===========================================================
# Q3: Check Palindrome Sentence (ignore spaces and case)
# ===========================================================

def palindrome(input_str):
    if input_str == "":
        print("Please enter a valid string")
        return False
    cleaned = "".join(input_str.lower().split(" "))
    return cleaned == cleaned[::-1]

input_str = "Madam madam"
output = palindrome(input_str)
print("Palindrome:" if output else "Not a palindrome:")

# ===========================================================
# Q4: Count Occurrence of a Word in a Paragraph
# ===========================================================

paragraph = """Ratan Tata was the son of Naval Tata,
               who was adopted by Ratanji Tata, son
               of Jamshedji Tata, the founder of the
               Tata Group."""

def count_word(paragraph, word):
    words = paragraph.lower().split()
    return words.count(word.lower())

count = count_word(paragraph, "tata")
print("The count of 'Tata' is:", count)

# ===========================================================
# Q5: Extract Email Username
# ===========================================================

email = "ckale5157@gmail.com"

def extract_username(email):
    return email.split("@")[0]

username = extract_username(email)
print("The username of the email is:", username)

# ===========================================================
# Q6: Reverse Words in a Sentence
# ===========================================================

def reverse_words(sentence):
    words = sentence.split(" ")
    words.reverse()
    return " ".join(words)

sentence = "Python is very powerful"
reversed_words = reverse_words(sentence)
print("The reversed words in a sentence are:", reversed_words)

# ===========================================================
# Q7: Generate Username from Full Name
# ===========================================================

def username_generator(name):
    name_parts = name.lower().split(" ")
    random_num = random.randint(1, 100)
    return "_".join(name_parts) + "_" + str(random_num)

name = input("Enter your full name: ")
username = username_generator(name)
print("The username is:", username)

# ===========================================================
# Q8: Check Vowel or Consonant
# ===========================================================

def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vowels:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

char = input("Enter a character: ")
if len(char) > 1:
    print("Enter a valid single character")
else:
    is_vowel(char)

# ===========================================================
# Q9: Compare Two Strings (Case Independent)
# ===========================================================

def is_similar(string1, string2):
    return string1.lower() == string2.lower()

string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
print("Same" if is_similar(string1, string2) else "Different")

# ===========================================================
# Q10: Remove Negative Numbers from List
# ===========================================================

lst = [3, -2, 7, -8, 9]

def remove_negatives(lst):
    return [i for i in lst if i > 0]

lst = remove_negatives(lst)
print("After removing negatives:", lst)

# ===========================================================
# Q11: Sum of Even & Odd Numbers
# ===========================================================

lst = list(range(1, 21))

def even_sum(lst):
    return sum(i for i in lst if i % 2 == 0)

def odd_sum(lst):
    return sum(i for i in lst if i % 2 != 0)

print("Sum of even numbers:", even_sum(lst))
print("Sum of odd numbers:", odd_sum(lst))

# ===========================================================
# Q12: Find Second Largest Number
# ===========================================================

def second_largest_num(lst):
    lst.sort(reverse=True)
    return lst[1]

lst = [10, 40, 20, 60, 30]
num = second_largest_num(lst)
print("The second largest number is:", num)

# ===========================================================
# Q13: Shopping Cart Price Calculator
# ===========================================================

items = [("Milk", 40), ("Bread", 30), ("Eggs", 60)]
total = sum(item[1] for item in items)
print("Total:", total)

# ===========================================================
# Q14: Word Length Mapping
# ===========================================================

fruits = ["apple", "banana", "mango"]
fruits_map = {fruit: len(fruit) for fruit in fruits}
print(fruits_map)

# ===========================================================
# Q15: Find Names Starting With a Letter
# ===========================================================

names = ["Riya", "Rohan", "Kunal", "Ritika"]
print([i for i in names if i[0] == "R"])

# ===========================================================
# Q16: Format a Receipt Using f-string
# ===========================================================

item = "Chocolate"
qty = 3
price = 45
print(f"You bought {qty} {item}(s) for rupees {qty * price}")
