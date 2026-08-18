# ============================================================
# PYTHON VARIABLES
# ============================================================

# A variable is a name used to store a value.
#
# Example:
#
# name = "Priya"
#
# name       -> variable
# "Priya"    -> value


# ------------------------------------------------------------
# 1. CREATING A VARIABLE
# ------------------------------------------------------------

name = "Priya"

print(name)


# ------------------------------------------------------------
# 2. DIFFERENT TYPES OF VALUES
# ------------------------------------------------------------

name = "Priya"          # String
age = 22                # Integer
salary = 25000.50       # Float
is_student = True       # Boolean

print(name)
print(age)
print(salary)
print(is_student)


# ------------------------------------------------------------
# 3. MULTIPLE VARIABLES
# ------------------------------------------------------------

first_name = "Priya"
last_name = "Gopinath"

print(first_name)
print(last_name)


# ------------------------------------------------------------
# 4. CHANGING A VARIABLE VALUE
# ------------------------------------------------------------

age = 21

print(age)

# Change the value
age = 22

print(age)


# ------------------------------------------------------------
# 5. VARIABLES CAN STORE CALCULATIONS
# ------------------------------------------------------------

price = 100
quantity = 5

total = price * quantity

print("Total:", total)


# ------------------------------------------------------------
# 6. MULTIPLE ASSIGNMENT
# ------------------------------------------------------------

name, age, city = "Priya", 22, "Chennai"

print(name)
print(age)
print(city)


# ------------------------------------------------------------
# 7. SAME VALUE TO MULTIPLE VARIABLES
# ------------------------------------------------------------

x = y = z = 100

print(x)
print(y)
print(z)


# ------------------------------------------------------------
# 8. VARIABLE NAMING RULES
# ------------------------------------------------------------

# Valid variable names:

student_name = "Priya"
student_age = 22
marks1 = 90
_total = 500

print(student_name)
print(student_age)
print(marks1)
print(_total)


# ------------------------------------------------------------
# INVALID VARIABLE NAMES
# ------------------------------------------------------------

# The following are NOT valid:

# 1student = "Priya"       # Cannot start with a number
# student-name = "Priya"  # Hyphen is not allowed
# student name = "Priya"  # Space is not allowed


# ------------------------------------------------------------
# 9. PYTHON VARIABLES ARE DYNAMICALLY TYPED
# ------------------------------------------------------------

# We don't have to explicitly mention the data type.

value = 100

print(value)

# The same variable can later store another type.

value = "Python"

print(value)


# ------------------------------------------------------------
# 10. REAL-WORLD EXAMPLE
# ------------------------------------------------------------

# Student information

student_name = "Priya"
student_age = 22
student_mark = 87.5
student_is_placed = True

print("---------- STUDENT DETAILS ----------")

print("Name:", student_name)
print("Age:", student_age)
print("Mark:", student_mark)
print("Placed:", student_is_placed)


# ------------------------------------------------------------
# 11. CALCULATING USING VARIABLES
# ------------------------------------------------------------

monthly_salary = 30000
monthly_expense = 18000

monthly_savings = monthly_salary - monthly_expense

print("Monthly Salary:", monthly_salary)
print("Monthly Expense:", monthly_expense)
print("Monthly Savings:", monthly_savings)