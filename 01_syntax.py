# ============================================================
# PYTHON SYNTAX
# ============================================================

# Syntax means the rules we follow when writing Python code.
# Python syntax is designed to be simple and readable.


# ------------------------------------------------------------
# 1. PRINTING SOMETHING
# ------------------------------------------------------------

# print() is used to display information on the screen.

print("Hello Python")

print("Welcome to Python Programming")


# ------------------------------------------------------------
# 2. PRINTING NUMBERS
# ------------------------------------------------------------

print(10)

print(25.5)


# ------------------------------------------------------------
# 3. PRINTING MULTIPLE VALUES
# ------------------------------------------------------------

name = "Priya"
age = 22

print(name, age)


# ------------------------------------------------------------
# 4. COMMENTS
# ------------------------------------------------------------

# This is a single-line comment.
# Python ignores comments when executing the program.

print("Comments help programmers understand code.")


# ------------------------------------------------------------
# 5. MULTI-LINE COMMENTS
# ------------------------------------------------------------

"""
This is a multi-line string.

It can be used to write
multiple lines of explanation.

It is commonly used as documentation.
"""

print("Python is easy to read.")


# ------------------------------------------------------------
# 6. INDENTATION
# ------------------------------------------------------------

# Python uses indentation (spaces) to define a block of code.

age = 22

if age >= 18:
    # This line belongs to the if block
    print("You are an adult.")

# This line is outside the if block
print("Program completed.")


# ------------------------------------------------------------
# 7. INDENTATION WITH A LOOP
# ------------------------------------------------------------

for number in range(1, 4):
    # These lines belong to the loop
    print("Number:", number)

print("Loop completed.")


# ------------------------------------------------------------
# 8. PYTHON IS CASE-SENSITIVE
# ------------------------------------------------------------

name = "Priya"

# Name and name are different variables.

Name = "Rahul"

print(name)
print(Name)


# ------------------------------------------------------------
# 9. STATEMENTS
# ------------------------------------------------------------

# A statement is an instruction given to Python.

student = "Priya"

print(student)


# ------------------------------------------------------------
# 10. PYTHON DOES NOT REQUIRE SEMICOLONS
# ------------------------------------------------------------

# In some programming languages, we use ;
# Python normally does not require it.

x = 10
y = 20

print(x + y)


# ------------------------------------------------------------
# 11. BASIC PYTHON PROGRAM
# ------------------------------------------------------------

# This is a simple program demonstrating Python syntax.

student_name = "Priya"
student_age = 22
student_course = "Computer Science"

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Course:", student_course)