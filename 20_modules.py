# ============================================================
# PYTHON MODULES
# ============================================================

# A module is simply a Python file containing
# reusable code.
#
# A module can contain:
#
# - Variables
# - Functions
# - Classes
#
# We can import that code into another Python file.


# ============================================================
# 1. IMPORTING OUR OWN MODULE
# ============================================================

import calculator


# Use the functions from calculator.py

print(calculator.add(10, 20))

print(calculator.subtract(20, 10))

print(calculator.multiply(5, 4))

print(calculator.divide(20, 5))


# ============================================================
# 2. IMPORTING SPECIFIC FUNCTIONS
# ============================================================

from calculator import add

print(add(100, 200))


# ============================================================
# 3. IMPORT MULTIPLE FUNCTIONS
# ============================================================

from calculator import add, subtract

print(add(10, 20))

print(subtract(20, 10))


# ============================================================
# 4. USING ALIAS
# ============================================================

import calculator as calc

print(calc.add(50, 50))


# ============================================================
# 5. BUILT-IN PYTHON MODULE
# ============================================================

# Python provides many modules.
#
# Example:
# math
#
# math provides mathematical functions.

import math

print(math.sqrt(25))

print(math.pi)


# ============================================================
# 6. RANDOM MODULE
# ============================================================

import random

number = random.randint(1, 10)

print("Random number:", number)


# ============================================================
# 7. DATETIME MODULE
# ============================================================

import datetime

today = datetime.date.today()

print("Today's date:", today)


# ============================================================
# 8. MODULE WITH A VARIABLE
# ============================================================

# Suppose calculator.py contains:
#
# company = "ABC"
#
# We could access it using:
#
# calculator.company
#
# Modules can therefore contain both
# variables and functions.


# ============================================================
# 9. WHY USE MODULES?
# ============================================================

# Imagine a large application.
#
# Instead of putting everything in one file:
#
# main.py
#
# We can organize code:
#
# calculator.py
# database.py
# authentication.py
# employee.py
#
# Then import the required code.


# ============================================================
# 10. REAL-WORLD EXAMPLE
# ============================================================

# Imagine an e-commerce application.
#
# It could have:
#
# payment.py
# product.py
# user.py
# order.py
#
# Each module handles a specific responsibility.
#
# This makes the application:
#
# - Easier to understand
# - Easier to maintain
# - Easier to reuse
# - Easier to test