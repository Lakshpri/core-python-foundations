# ============================================================
# PYTHON TUPLES
# ============================================================

# A tuple is a collection used to store multiple values.
#
# Tuple characteristics:
#
# 1. Ordered
# 2. Allows duplicate values
# 3. Immutable - cannot be changed after creation
# 4. Can contain different data types
# 5. Written using parentheses ()
#
# Example:
#
# student = ("Priya", 22, "Python")


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

student = ("Priya", 22, "Python")

print(student)


# ============================================================
# 2. TUPLE WITH NUMBERS
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers)


# ============================================================
# 3. TUPLE WITH DIFFERENT DATA TYPES
# ============================================================

data = ("Priya", 22, 85.5, True)

print(data)


# ============================================================
# 4. CHECK DATA TYPE
# ============================================================

student = ("Priya", 22, "Python")

print(type(student))


# ============================================================
# 5. ACCESSING TUPLE ELEMENTS
# ============================================================

student = ("Priya", 22, "Python")

print(student[0])
print(student[1])
print(student[2])


# ============================================================
# 6. NEGATIVE INDEXING
# ============================================================

student = ("Priya", 22, "Python")

print(student[-1])
print(student[-2])
print(student[-3])


# ============================================================
# 7. TUPLE SLICING
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])

print(numbers[:3])

print(numbers[2:])

print(numbers[-3:])


# ============================================================
# 8. TUPLE LENGTH
# ============================================================

student = ("Priya", 22, "Python")

print(len(student))


# ============================================================
# 9. TUPLE ALLOWS DUPLICATES
# ============================================================

numbers = (10, 20, 10, 30, 10)

print(numbers)


# ============================================================
# 10. LOOP THROUGH A TUPLE
# ============================================================

languages = ("Python", "Java", "C++", "JavaScript")

for language in languages:
    print(language)


# ============================================================
# 11. CHECK WHETHER VALUE EXISTS
# ============================================================

languages = ("Python", "Java", "C++")

print("Python" in languages)

print("Ruby" in languages)


# ============================================================
# 12. NOT IN
# ============================================================

languages = ("Python", "Java", "C++")

print("Ruby" not in languages)


# ============================================================
# 13. COUNT()
# ============================================================

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))


# ============================================================
# 14. INDEX()
# ============================================================

languages = ("Python", "Java", "C++")

print(languages.index("Java"))


# ============================================================
# 15. TUPLE CANNOT BE MODIFIED
# ============================================================

student = ("Priya", 22, "Python")

# The following will cause an error:

# student[1] = 23


# ============================================================
# 16. WHY USE TUPLES?
# ============================================================

# Tuples are useful when data should not change.
#
# Example:
# Coordinates of a location

location = (13.0827, 80.2707)

print("Latitude:", location[0])
print("Longitude:", location[1])


# ============================================================
# 17. TUPLE UNPACKING
# ============================================================

student = ("Priya", 22, "Python")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# ============================================================
# 18. SWAPPING VARIABLES USING TUPLE UNPACKING
# ============================================================

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)


# ============================================================
# 19. NESTED TUPLE
# ============================================================

students = (
    ("Priya", 22),
    ("Rahul", 23),
    ("Arun", 21)
)

print(students)

print(students[0])

print(students[0][0])

print(students[0][1])


# ============================================================
# 20. REAL-WORLD EXAMPLE
# ============================================================

# Employee details that should not be changed

employee = (
    101,
    "Priya",
    "Java Developer",
    "Chennai"
)

print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Role:", employee[2])
print("Location:", employee[3])


# ============================================================
# IMPORTANT TUPLE METHODS
# ============================================================

# count()
# index()
#
# Useful built-in functions:
#
# len()
# min()
# max()
# sum()