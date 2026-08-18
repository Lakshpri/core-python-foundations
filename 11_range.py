# ============================================================
# RANGE() FUNCTION IN PYTHON
# ============================================================

# range() generates a sequence of numbers.
#
# It is commonly used with for loops.


# ============================================================
# 1. range(stop)
# ============================================================

# Starts from 0.
# Stops BEFORE 5.

for number in range(5):

    print(number)


# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# 2. range(start, stop)
# ============================================================

for number in range(1, 6):

    print(number)


# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 3. range(start, stop, step)
# ============================================================

for number in range(1, 11, 2):

    print(number)


# Output:
# 1
# 3
# 5
# 7
# 9


# ============================================================
# 4. EVEN NUMBERS
# ============================================================

for number in range(2, 11, 2):

    print(number)


# ============================================================
# 5. ODD NUMBERS
# ============================================================

for number in range(1, 11, 2):

    print(number)


# ============================================================
# 6. COUNTING BACKWARDS
# ============================================================

for number in range(10, 0, -1):

    print(number)


# ============================================================
# 7. REVERSE EVEN NUMBERS
# ============================================================

for number in range(10, 0, -2):

    print(number)


# ============================================================
# 8. RANGE WITH NEGATIVE NUMBERS
# ============================================================

for number in range(-5, 1):

    print(number)


# ============================================================
# 9. SUM USING RANGE
# ============================================================

total = 0

for number in range(1, 11):

    total = total + number

print("Sum:", total)


# ============================================================
# 10. MULTIPLICATION TABLE USING RANGE
# ============================================================

number = 7

for i in range(1, 11):

    print(number, "x", i, "=", number * i)


# ============================================================
# 11. USER INPUT + RANGE
# ============================================================

n = int(input("Enter a number: "))

for number in range(1, n + 1):

    print(number)


# ============================================================
# 12. PRINT MULTIPLES
# ============================================================

number = int(input("Enter number: "))

for i in range(1, 11):

    print(number * i)


# ============================================================
# 13. RANGE CAN BE CONVERTED TO A LIST
# ============================================================

numbers = list(range(1, 6))

print(numbers)


# ============================================================
# 14. REAL-WORLD EXAMPLE
# ============================================================

# Generate seat numbers.

for seat_number in range(1, 11):

    print("Seat Number:", seat_number)


# ============================================================
# 15. REAL-WORLD EXAMPLE - MONTHS
# ============================================================

# Month numbers are from 1 to 12.

for month in range(1, 13):

    print("Month:", month)


# ============================================================
# IMPORTANT RANGE RULE
# ============================================================

# range(start, stop, step)
#
# start -> where the sequence begins
# stop  -> where the sequence stops (NOT included)
# step  -> how much the number changes
#
# Example:
#
# range(1, 10, 2)
#
# gives:
#
# 1, 3, 5, 7, 9