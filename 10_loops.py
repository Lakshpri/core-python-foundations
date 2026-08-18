# ============================================================
# LOOPS IN PYTHON
# ============================================================

# Loops are used to repeat a block of code.
#
# Python mainly has:
#
# 1. for loop
# 2. while loop


# ============================================================
# 1. BASIC FOR LOOP
# ============================================================

for i in range(5):
    print(i)


# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# 2. FOR LOOP WITH RANGE
# ============================================================

for number in range(1, 6):
    print(number)


# ============================================================
# 3. PRINT MESSAGE MULTIPLE TIMES
# ============================================================

for i in range(5):
    print("Welcome to Python")


# ============================================================
# 4. LOOP THROUGH A STRING
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# 5. LOOP THROUGH A LIST
# ============================================================

students = ["Priya", "Rahul", "Arun", "Meena"]

for student in students:
    print(student)


# ============================================================
# 6. SUM OF NUMBERS
# ============================================================

total = 0

for number in range(1, 6):

    total = total + number

print("Total:", total)


# ============================================================
# 7. MULTIPLICATION TABLE
# ============================================================

number = 5

for i in range(1, 11):

    result = number * i

    print(number, "x", i, "=", result)


# ============================================================
# 8. WHILE LOOP
# ============================================================

number = 1

while number <= 5:

    print(number)

    number = number + 1


# ============================================================
# 9. WHILE LOOP COUNTDOWN
# ============================================================

number = 5

while number >= 1:

    print(number)

    number = number - 1

print("Start!")


# ============================================================
# 10. USER CONTROLLED WHILE LOOP
# ============================================================

number = int(input("Enter a number: "))

while number <= 10:

    print(number)

    number = number + 1


# ============================================================
# 11. BREAK
# ============================================================

# break immediately stops the loop.

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# Output:
# 1
# 2
# 3
# 4


# ============================================================
# 12. CONTINUE
# ============================================================

# continue skips the current iteration
# and moves to the next iteration.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# ============================================================
# 13. SKIP EVEN NUMBERS
# ============================================================

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 14. FIND FIRST MULTIPLE OF 7
# ============================================================

for number in range(1, 101):

    if number % 7 == 0:

        print("First multiple of 7:", number)

        break


# ============================================================
# 15. NESTED LOOPS
# ============================================================

for i in range(1, 4):

    for j in range(1, 4):

        print("i =", i, "j =", j)


# ============================================================
# 16. SIMPLE PATTERN
# ============================================================

for i in range(1, 6):

    print("*" * i)


# ============================================================
# 17. REAL-WORLD EXAMPLE
# ============================================================

# Print student attendance for 5 days.

for day in range(1, 6):

    print("Day", day, ": Student attended")


# ============================================================
# 18. REAL-WORLD ATM PIN EXAMPLE
# ============================================================

correct_pin = "1234"

attempts = 3

while attempts > 0:

    pin = input("Enter PIN: ")

    if pin == correct_pin:

        print("PIN correct. Access granted.")

        break

    else:

        attempts = attempts - 1

        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

else:

    print("Account temporarily locked.")