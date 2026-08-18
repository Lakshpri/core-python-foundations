# ============================================================
# PYTHON LISTS
# ============================================================

# A list is used to store multiple values in one variable.
#
# Lists:
# - Are ordered
# - Allow duplicate values
# - Are mutable (can be changed)
# - Can store different data types


# ============================================================
# 1. CREATING A LIST
# ============================================================

students = ["Priya", "Rahul", "Arun", "Meena"]

print(students)


# ============================================================
# 2. LIST WITH NUMBERS
# ============================================================

marks = [85, 90, 76, 88, 95]

print(marks)


# ============================================================
# 3. LIST WITH DIFFERENT DATA TYPES
# ============================================================

data = ["Priya", 22, 85.5, True]

print(data)


# ============================================================
# 4. ACCESSING LIST ELEMENTS
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print(students[0])
print(students[1])
print(students[2])


# ============================================================
# 5. NEGATIVE INDEXING
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print(students[-1])
print(students[-2])


# ============================================================
# 6. LIST SLICING
# ============================================================

students = ["Priya", "Rahul", "Arun", "Meena", "Kiran"]

print(students[0:3])

print(students[:3])

print(students[2:])

print(students[-3:])


# ============================================================
# 7. CHANGING A LIST ELEMENT
# ============================================================

students = ["Priya", "Rahul", "Arun"]

# Change second element

students[1] = "Kiran"

print(students)


# ============================================================
# 8. APPEND
# ============================================================

students = ["Priya", "Rahul"]

# append() adds an element at the end.

students.append("Arun")

print(students)


# ============================================================
# 9. INSERT
# ============================================================

students = ["Priya", "Rahul", "Arun"]

# Insert "Meena" at index 1.

students.insert(1, "Meena")

print(students)


# ============================================================
# 10. EXTEND
# ============================================================

students = ["Priya", "Rahul"]

new_students = ["Arun", "Meena"]

students.extend(new_students)

print(students)


# ============================================================
# 11. REMOVE
# ============================================================

students = ["Priya", "Rahul", "Arun"]

students.remove("Rahul")

print(students)


# ============================================================
# 12. POP
# ============================================================

students = ["Priya", "Rahul", "Arun"]

# Removes the last element.

students.pop()

print(students)


# Remove element using index

students = ["Priya", "Rahul", "Arun"]

students.pop(1)

print(students)


# ============================================================
# 13. DEL
# ============================================================

students = ["Priya", "Rahul", "Arun"]

del students[0]

print(students)


# ============================================================
# 14. CLEAR
# ============================================================

students = ["Priya", "Rahul", "Arun"]

students.clear()

print(students)


# ============================================================
# 15. LENGTH OF LIST
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print(len(students))


# ============================================================
# 16. CHECK WHETHER ELEMENT EXISTS
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print("Priya" in students)

print("Kiran" in students)


# ============================================================
# 17. LOOP THROUGH A LIST
# ============================================================

students = ["Priya", "Rahul", "Arun"]

for student in students:

    print(student)


# ============================================================
# 18. LIST WITH NUMBERS
# ============================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    print(number)


# ============================================================
# 19. SUM OF LIST
# ============================================================

marks = [80, 90, 70, 85, 95]

total = sum(marks)

print("Total:", total)


# ============================================================
# 20. MINIMUM AND MAXIMUM
# ============================================================

marks = [80, 90, 70, 85, 95]

print("Highest:", max(marks))

print("Lowest:", min(marks))


# ============================================================
# 21. SORTING
# ============================================================

marks = [80, 50, 95, 70, 85]

marks.sort()

print(marks)


# ============================================================
# 22. REVERSE SORTING
# ============================================================

marks = [80, 50, 95, 70, 85]

marks.sort(reverse=True)

print(marks)


# ============================================================
# 23. REVERSE
# ============================================================

students = ["Priya", "Rahul", "Arun"]

students.reverse()

print(students)


# ============================================================
# 24. COUNT
# ============================================================

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))


# ============================================================
# 25. INDEX
# ============================================================

students = ["Priya", "Rahul", "Arun"]

print(students.index("Rahul"))


# ============================================================
# 26. COPYING A LIST
# ============================================================

students = ["Priya", "Rahul", "Arun"]

new_students = students.copy()

print(new_students)


# ============================================================
# 27. NESTED LIST
# ============================================================

# A list can contain another list.

students = [
    ["Priya", 22],
    ["Rahul", 23],
    ["Arun", 21]
]

print(students)


# Access nested list

print(students[0])

print(students[0][0])

print(students[0][1])


# ============================================================
# 28. REAL-WORLD EXAMPLE - SHOPPING CART
# ============================================================

cart = []

# Add products

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Shopping Cart:", cart)


# Remove a product

cart.remove("Mouse")

print("Updated Cart:", cart)


# ============================================================
# 29. REAL-WORLD EXAMPLE - STUDENT MARKS
# ============================================================

marks = [85, 90, 78, 92, 88]

print("Marks:", marks)

total = sum(marks)

highest = max(marks)

lowest = min(marks)

average = total / len(marks)

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)


# ============================================================
# IMPORTANT LIST METHODS
# ============================================================

# append()
# insert()
# extend()
# remove()
# pop()
# clear()
# sort()
# reverse()
# count()
# index()
# copy()
#
# Useful built-in functions:
#
# len()
# sum()
# min()
# max()