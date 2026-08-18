# ============================================================
# FUNCTION ARGUMENTS IN PYTHON
# ============================================================

# An argument is the actual value passed to a function.
#
# Example:
#
# def greet(name):
#     print(name)
#
# greet("Priya")
#
# "Priya" is the argument.


# ============================================================
# 1. POSITIONAL ARGUMENTS
# ============================================================

def student_details(name, age, course):

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details("Priya", 22, "Python")


# The values are assigned based on their position.


# ============================================================
# 2. ORDER MATTERS IN POSITIONAL ARGUMENTS
# ============================================================

def employee(name, role):

    print("Name:", name)
    print("Role:", role)


employee("Priya", "Developer")


# If the order changes:

employee("Developer", "Priya")

# Python will still accept it,
# but the data will be logically incorrect.


# ============================================================
# 3. KEYWORD ARGUMENTS
# ============================================================

def student(name, age, course):

    print(name)
    print(age)
    print(course)


student(
    name="Priya",
    age=22,
    course="Python"
)


# ============================================================
# 4. KEYWORD ARGUMENTS CAN CHANGE ORDER
# ============================================================

student(
    course="Python",
    name="Priya",
    age=22
)


# ============================================================
# 5. DEFAULT ARGUMENTS
# ============================================================

def greet(name="Student"):

    print("Hello", name)


greet("Priya")

greet()


# ============================================================
# 6. MULTIPLE DEFAULT ARGUMENTS
# ============================================================

def employee_details(
    name,
    role="Developer",
    location="Chennai"
):

    print("Name:", name)
    print("Role:", role)
    print("Location:", location)


employee_details("Priya")

employee_details(
    "Rahul",
    "Tester",
    "Bangalore"
)


# ============================================================
# 7. POSITIONAL + KEYWORD ARGUMENTS
# ============================================================

def student(name, age, course):

    print(name, age, course)


student(
    "Priya",
    age=22,
    course="Python"
)


# ============================================================
# IMPORTANT RULE
# ============================================================

# Positional arguments should generally come before
# keyword arguments.


# ============================================================
# 8. *args
# ============================================================

# *args allows a function to accept
# any number of positional arguments.

def add_numbers(*numbers):

    total = 0

    for number in numbers:

        total = total + number

    return total


print(add_numbers(10, 20))

print(add_numbers(10, 20, 30))

print(add_numbers(10, 20, 30, 40, 50))


# ============================================================
# 9. *args IS A TUPLE
# ============================================================

def display(*values):

    print(values)

    print(type(values))


display(10, 20, 30)


# ============================================================
# 10. **kwargs
# ============================================================

# **kwargs allows a function to accept
# any number of keyword arguments.

def display_student(**details):

    print(details)


display_student(
    name="Priya",
    age=22,
    course="Python"
)


# ============================================================
# 11. **kwargs IS A DICTIONARY
# ============================================================

def display(**details):

    print(details)

    print(type(details))


display(
    name="Priya",
    age=22
)


# ============================================================
# 12. LOOPING THROUGH **kwargs
# ============================================================

def student_details(**details):

    for key, value in details.items():

        print(key, ":", value)


student_details(
    name="Priya",
    age=22,
    course="Python",
    city="Chennai"
)


# ============================================================
# 13. *args + **kwargs
# ============================================================

def example(*args, **kwargs):

    print("Positional arguments:", args)

    print("Keyword arguments:", kwargs)


example(
    10,
    20,
    30,
    name="Priya",
    age=22
)


# ============================================================
# 14. REAL-WORLD SHOPPING EXAMPLE
# ============================================================

def calculate_total(*prices):

    total = 0

    for price in prices:

        total += price

    return total


print("Total:", calculate_total(100, 200))

print("Total:", calculate_total(100, 200, 300))

print("Total:", calculate_total(100, 200, 300, 400))


# ============================================================
# 15. REAL-WORLD USER PROFILE
# ============================================================

def create_profile(**details):

    print("---------- PROFILE ----------")

    for key, value in details.items():

        print(key, ":", value)


create_profile(
    name="Priya",
    age=22,
    city="Chennai",
    profession="Developer"
)


# ============================================================
# ARGUMENT SUMMARY
# ============================================================

# Positional arguments
# Keyword arguments
# Default arguments
# *args
# **kwargs