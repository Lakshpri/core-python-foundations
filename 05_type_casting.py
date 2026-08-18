# ============================================================
# TYPE CASTING IN PYTHON
# ============================================================

# Type casting means converting one data type into another.
#
# Common functions:
#
# int()
# float()
# str()
# bool()


# ============================================================
# 1. STRING TO INTEGER
# ============================================================

number = "100"

print(number)
print(type(number))

# Convert string to integer
number = int(number)

print(number)
print(type(number))


# ============================================================
# 2. STRING TO FLOAT
# ============================================================

price = "99.50"

print(price)
print(type(price))

price = float(price)

print(price)
print(type(price))


# ============================================================
# 3. INTEGER TO FLOAT
# ============================================================

number = 100

print(number)
print(type(number))

number = float(number)

print(number)
print(type(number))


# ============================================================
# 4. FLOAT TO INTEGER
# ============================================================

price = 99.99

print(price)

# Decimal part is removed
price = int(price)

print(price)


# ============================================================
# 5. INTEGER TO STRING
# ============================================================

age = 22

print(age)
print(type(age))

age = str(age)

print(age)
print(type(age))


# ============================================================
# 6. FLOAT TO STRING
# ============================================================

salary = 25000.50

salary = str(salary)

print(salary)
print(type(salary))


# ============================================================
# 7. BOOLEAN CONVERSION
# ============================================================

# Non-zero numbers generally become True.

print(bool(1))
print(bool(10))
print(bool(-5))

# Zero becomes False.

print(bool(0))


# ============================================================
# 8. STRING TO BOOLEAN
# ============================================================

# Important:
# Any non-empty string becomes True.

print(bool("Python"))
print(bool("Hello"))

# Empty string becomes False.

print(bool(""))


# ============================================================
# 9. INPUT + TYPE CASTING
# ============================================================

# input() gives us a string.
# If we want to perform mathematical calculations,
# we need to convert it.

age = input("Enter your age: ")

age = int(age)

print("Your age is:", age)

next_year = age + 1

print("Next year your age will be:", next_year)


# ============================================================
# 10. TAKING TWO NUMBERS
# ============================================================

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Convert both strings into integers

number1 = int(number1)
number2 = int(number2)

result = number1 + number2

print("Sum:", result)


# ============================================================
# 11. REAL-WORLD EXAMPLE
# ============================================================

print("---------- SHOPPING BILL ----------")

product_price = input("Enter product price: ")
quantity = input("Enter quantity: ")

# Convert input values to numbers

product_price = float(product_price)
quantity = int(quantity)

# Calculate total

total = product_price * quantity

print("Product Price:", product_price)
print("Quantity:", quantity)
print("Total Amount:", total)


# ============================================================
# 12. TYPE CASTING SUMMARY
# ============================================================

# int("100")       -> 100
# float("10.5")    -> 10.5
# str(100)         -> "100"
# bool(1)          -> True
# bool(0)          -> False