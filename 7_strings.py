# ============================================================
# PYTHON STRINGS
# ============================================================

# A string is a sequence of characters.
# Strings are used to store text.
#
# Examples:
# "Hello"
# "Python"
# "Chennai"
# "12345"
#
# We can create strings using:
# Single quotes  -> 'Python'
# Double quotes  -> "Python"


# ============================================================
# 1. CREATING A STRING
# ============================================================

name = "Priya"

print(name)


# Single quotes can also be used

city = 'Chennai'

print(city)


# ============================================================
# 2. STRING WITH NUMBERS
# ============================================================

# This is a STRING, not an integer.

phone = "9876543210"

print(phone)

print(type(phone))


# ============================================================
# 3. STRING LENGTH
# ============================================================

# len() returns the number of characters.

name = "Python"

print(len(name))


# Output:
# 6


# ============================================================
# 4. STRING INDEXING
# ============================================================

# Every character has an index.
#
# Python uses ZERO-BASED indexing.
#
# P  Y  T  H  O  N
# 0  1  2  3  4  5

language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])


# ============================================================
# 5. NEGATIVE INDEXING
# ============================================================

# Python also supports negative indexes.
#
# P   Y   T   H   O   N
# -6 -5  -4  -3  -2  -1

language = "Python"

print(language[-1])  # N
print(language[-2])  # O
print(language[-3])  # H


# ============================================================
# 6. STRING SLICING
# ============================================================

# Slicing extracts a portion of a string.
#
# Syntax:
# string[start:end]
#
# The end index is NOT included.

language = "Python"

print(language[0:2])
print(language[0:4])
print(language[2:6])


# ============================================================
# 7. SLICING FROM THE BEGINNING
# ============================================================

name = "Programming"

print(name[:4])

# Same as:
# name[0:4]


# ============================================================
# 8. SLICING UNTIL THE END
# ============================================================

name = "Programming"

print(name[4:])


# ============================================================
# 9. NEGATIVE SLICING
# ============================================================

name = "Programming"

print(name[-5:])
print(name[:-5])


# ============================================================
# 10. STRING CONCATENATION
# ============================================================

# Concatenation means joining strings.

first_name = "Lakshmi"
last_name = "Priya"

full_name = first_name + " " + last_name

print(full_name)


# ============================================================
# 11. STRING REPETITION
# ============================================================

message = "Hello "

print(message * 3)


# ============================================================
# 12. STRING METHODS
# ============================================================

name = "python programming"

# Convert to uppercase
print(name.upper())

# Convert to lowercase
print(name.lower())

# Capitalize first character
print(name.capitalize())

# Convert every word's first character to uppercase
print(name.title())


# ============================================================
# 13. strip()
# ============================================================

# strip() removes spaces from the beginning and end.

name = "   Priya   "

print(name)

print(name.strip())


# ============================================================
# 14. replace()
# ============================================================

message = "I am learning Java"

new_message = message.replace("Java", "Python")

print(new_message)


# ============================================================
# 15. find()
# ============================================================

language = "Python Programming"

position = language.find("Programming")

print(position)


# ============================================================
# 16. count()
# ============================================================

message = "Python is easy. Python is powerful."

print(message.count("Python"))


# ============================================================
# 17. startswith()
# ============================================================

email = "priya@gmail.com"

print(email.startswith("priya"))
print(email.startswith("admin"))


# ============================================================
# 18. endswith()
# ============================================================

filename = "student.py"

print(filename.endswith(".py"))
print(filename.endswith(".txt"))


# ============================================================
# 19. in OPERATOR
# ============================================================

message = "I am learning Python"

print("Python" in message)
print("Java" in message)


# ============================================================
# 20. NOT IN
# ============================================================

message = "I am learning Python"

print("Java" not in message)
print("Python" not in message)


# ============================================================
# 21. SPLIT
# ============================================================

sentence = "Python is easy to learn"

words = sentence.split()

print(words)


# ============================================================
# 22. JOIN
# ============================================================

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# ============================================================
# 23. F-STRINGS
# ============================================================

name = "Priya"
age = 22
city = "Chennai"

message = f"My name is {name}. I am {age} years old. I live in {city}."

print(message)


# ============================================================
# 24. ESCAPE CHARACTERS
# ============================================================

# \n means new line

print("Hello\nPython")


# \t means tab

print("Name:\tPriya")
print("Age:\t22")


# ============================================================
# 25. MULTILINE STRING
# ============================================================

message = """
Welcome to Python.

We are learning:
- Strings
- Variables
- Operators
"""

print(message)


# ============================================================
# 26. REAL-WORLD EXAMPLE
# ============================================================

print("---------- USER PROFILE ----------")

name = input("Enter your name: ")
city = input("Enter your city: ")

# Remove unwanted spaces
name = name.strip()
city = city.strip()

# Convert name to title case
name = name.title()

# Convert city to title case
city = city.title()

print()
print("Name:", name)
print("City:", city)

print(f"Welcome {name} from {city}!")


# ============================================================
# IMPORTANT STRING FUNCTIONS
# ============================================================

# len()
# upper()
# lower()
# capitalize()
# title()
# strip()
# replace()
# find()
# count()
# startswith()
# endswith()
# split()
# join()