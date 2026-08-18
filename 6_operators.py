# ============================================================
# PYTHON OPERATORS
# ============================================================

# Operators are symbols/keywords used to perform operations
# on values and variables.


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

# Arithmetic operators are used for mathematical operations.

a = 10
b = 3

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Floor Division
# Gives the quotient without the decimal part.

print("Floor Division:", a // b)

# Modulus
# Gives the remainder.

print("Modulus:", a % b)

# Exponent
# Means power.

print("Power:", a ** b)


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

# Comparison operators compare two values.
# The result will be True or False.

a = 10
b = 20

# Equal to
print("Equal:", a == b)

# Not equal to
print("Not Equal:", a != b)

# Greater than
print("Greater:", a > b)

# Less than
print("Less:", a < b)

# Greater than or equal to
print("Greater or Equal:", a >= b)

# Less than or equal to
print("Less or Equal:", a <= b)


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================

# Logical operators are used to combine conditions.

age = 22
has_degree = True

# AND
# Both conditions must be True.

print(age >= 18 and has_degree)


# OR
# At least one condition must be True.

print(age >= 18 or has_degree)


# NOT
# Reverses the result.

print(not has_degree)


# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================

# = assigns a value.

x = 10

print(x)


# +=
# Add and assign

x = 10
x += 5

print(x)


# -=
# Subtract and assign

x = 10
x -= 3

print(x)


# *=
# Multiply and assign

x = 10
x *= 2

print(x)


# /=
# Divide and assign

x = 10
x /= 2

print(x)


# //=
# Floor divide and assign

x = 10
x //= 3

print(x)


# %=
# Modulus and assign

x = 10
x %= 3

print(x)


# **=
# Power and assign

x = 2
x **= 3

print(x)


# ============================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================

# 'in' checks whether a value exists inside a collection.

name = "Python"

print("P" in name)
print("z" in name)


# 'not in' checks whether a value does NOT exist.

print("z" not in name)
print("P" not in name)


# ============================================================
# 6. MEMBERSHIP WITH LISTS
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print("Priya" in students)

print("Kiran" in students)


# ============================================================
# 7. IDENTITY OPERATORS
# ============================================================

# 'is' checks whether two variables refer to the same object.
#
# '==' checks whether two values are equal.
#
# They are NOT the same thing.

x = None

print(x is None)

print(x is not None)


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================

# Python follows mathematical precedence rules.

result = 10 + 5 * 2

# Multiplication happens before addition.

print(result)


# Parentheses can change the order.

result = (10 + 5) * 2

print(result)


# ============================================================
# 9. REAL-WORLD EXAMPLE - SHOPPING
# ============================================================

price = 500
quantity = 3

total = price * quantity

print("Product Price:", price)
print("Quantity:", quantity)
print("Total:", total)


# ============================================================
# 10. REAL-WORLD EXAMPLE - STUDENT RESULT
# ============================================================

marks = 85

print("Marks:", marks)

print("Passed:", marks >= 40)

print("Excellent:", marks >= 90)


# ============================================================
# 11. REAL-WORLD EXAMPLE - ELIGIBILITY
# ============================================================

age = 22
has_degree = True

eligible = age >= 18 and has_degree

print("Eligible:", eligible)


# ============================================================
# 12. OPERATOR SUMMARY
# ============================================================

# Arithmetic:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor division
# %   Modulus
# **  Power
#
# Comparison:
# ==  Equal
# !=  Not equal
# >   Greater than
# <   Less than
# >=  Greater than or equal
# <=  Less than or equal
#
# Logical:
# and
# or
# not
#
# Assignment:
# =
# +=
# -=
# *=
# /=
# //=
# %=
# **=
#
# Membership:
# in
# not in
#
# Identity:
# is
# is not