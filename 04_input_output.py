# ============================================================
# INPUT AND OUTPUT IN PYTHON
# ============================================================

# OUTPUT:
# print() is used to display information.
#
# INPUT:
# input() is used to take information from the user.


# ============================================================
# 1. BASIC OUTPUT
# ============================================================

print("Hello Python")

print("Welcome to my program")


# ============================================================
# 2. PRINT MULTIPLE VALUES
# ============================================================

name = "Priya"
age = 22

print(name, age)


# ============================================================
# 3. PRINT WITH LABELS
# ============================================================

print("Name:", name)
print("Age:", age)


# ============================================================
# 4. BASIC INPUT
# ============================================================

# input() waits for the user to enter something.

name = input("Enter your name: ")

print("Hello", name)


# ============================================================
# 5. TAKING MULTIPLE INPUTS
# ============================================================

name = input("Enter your name: ")
city = input("Enter your city: ")
course = input("Enter your course: ")

print("---------- DETAILS ----------")

print("Name:", name)
print("City:", city)
print("Course:", course)


# ============================================================
# 6. IMPORTANT:
# input() ALWAYS RETURNS A STRING
# ============================================================

age = input("Enter your age: ")

print("Age:", age)

print("Data type:", type(age))


# ============================================================
# 7. STRING CONCATENATION
# ============================================================

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# ============================================================
# 8. F-STRINGS
# ============================================================

name = input("Enter your name: ")
city = input("Enter your city: ")

# f-string allows us to directly insert variables
# inside a string.

print(f"My name is {name} and I live in {city}.")


# ============================================================
# 9. REAL-WORLD EXAMPLE
# ============================================================

print("---------- STUDENT REGISTRATION ----------")

name = input("Enter student name: ")
course = input("Enter course: ")
college = input("Enter college name: ")

print()
print("---------- REGISTRATION DETAILS ----------")

print(f"Student Name : {name}")
print(f"Course       : {course}")
print(f"College      : {college}")