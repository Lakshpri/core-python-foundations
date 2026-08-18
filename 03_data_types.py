# ============================================================
# PYTHON DATA TYPES
# ============================================================

# A data type tells Python what kind of value we are storing.


# ============================================================
# 1. INTEGER (int)
# ============================================================

# Integer represents whole numbers.

age = 22
marks = 95
quantity = 10

print(age)
print(marks)
print(quantity)

# Check the data type using type()

print(type(age))
print(type(marks))


# ============================================================
# 2. FLOAT (float)
# ============================================================

# Float represents numbers containing decimal values.

price = 99.50
percentage = 85.75
temperature = 36.5

print(price)
print(percentage)
print(temperature)

print(type(price))


# ============================================================
# 3. STRING (str)
# ============================================================

# String represents text.
# Strings can be written using:
#
# "double quotes"
# 'single quotes'

name = "Priya"
city = 'Chennai'

print(name)
print(city)

print(type(name))


# ============================================================
# 4. BOOLEAN (bool)
# ============================================================

# Boolean has only two possible values:
#
# True
# False

is_student = True
is_employee = False

print(is_student)
print(is_employee)

print(type(is_student))


# ============================================================
# 5. NONE (NoneType)
# ============================================================

# None means that currently there is no value.

address = None

print(address)

print(type(address))


# ============================================================
# 6. CHECKING DATA TYPES
# ============================================================

name = "Priya"
age = 22
salary = 25000.50
is_placed = True
address = None

print(type(name))
print(type(age))
print(type(salary))
print(type(is_placed))
print(type(address))


# ============================================================
# 7. BASIC DATA TYPES SUMMARY
# ============================================================

# int     -> Whole numbers
# float   -> Decimal numbers
# str     -> Text
# bool    -> True / False
# None    -> No value


# ============================================================
# 8. REAL-WORLD EXAMPLE
# ============================================================

student_name = "Priya"          # str
student_age = 22                # int
student_percentage = 87.5       # float
student_passed = True           # bool
student_address = None          # NoneType

print("---------- STUDENT DETAILS ----------")

print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", student_percentage)
print("Passed:", student_passed)
print("Address:", student_address)


# ============================================================
# 9. CHECK TYPES OF REAL-WORLD DATA
# ============================================================

print(type(student_name))
print(type(student_age))
print(type(student_percentage))
print(type(student_passed))
print(type(student_address))


# ============================================================
# 10. IMPORTANT: PYTHON IS DYNAMICALLY TYPED
# ============================================================

# We don't need to specify the data type while creating
# a variable.

value = 100

print(value)
print(type(value))

# Now the same variable stores a string.

value = "Python"

print(value)
print(type(value))