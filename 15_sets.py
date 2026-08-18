# ============================================================
# PYTHON SETS
# ============================================================

# A set is a collection of unique values.
#
# Characteristics:
#
# 1. Does not allow duplicates
# 2. Mutable
# 3. Unordered
# 4. Does not support indexing
#
# Sets are written using { }.


# ============================================================
# 1. CREATING A SET
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)


# ============================================================
# 2. DUPLICATES ARE REMOVED
# ============================================================

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# ============================================================
# 3. CHECK DATA TYPE
# ============================================================

numbers = {10, 20, 30}

print(type(numbers))


# ============================================================
# 4. ADD()
# ============================================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# ============================================================
# 5. UPDATE()
# ============================================================

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)


# ============================================================
# 6. REMOVE()
# ============================================================

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)


# ============================================================
# 7. DISCARD()
# ============================================================

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)


# discard() does not cause an error if the value
# does not exist.

numbers.discard(100)

print(numbers)


# ============================================================
# 8. POP()
# ============================================================

numbers = {10, 20, 30}

removed_value = numbers.pop()

print("Removed:", removed_value)
print(numbers)


# ============================================================
# 9. CLEAR()
# ============================================================

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# ============================================================
# 10. LENGTH
# ============================================================

numbers = {10, 20, 30, 40}

print(len(numbers))


# ============================================================
# 11. CHECK VALUE
# ============================================================

numbers = {10, 20, 30}

print(20 in numbers)

print(50 in numbers)


# ============================================================
# 12. LOOP THROUGH SET
# ============================================================

languages = {"Python", "Java", "C++"}

for language in languages:

    print(language)


# ============================================================
# 13. UNION
# ============================================================

# Union combines values from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)


# Another way:

result = set1 | set2

print(result)


# ============================================================
# 14. INTERSECTION
# ============================================================

# Intersection gives common values.

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.intersection(set2)

print(result)


# Another way:

result = set1 & set2

print(result)


# ============================================================
# 15. DIFFERENCE
# ============================================================

# Difference gives values that exist in the first set
# but not in the second set.

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.difference(set2)

print(result)


# Another way:

result = set1 - set2

print(result)


# ============================================================
# 16. SYMMETRIC DIFFERENCE
# ============================================================

# Gives values that are not common.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)

print(result)


# ============================================================
# 17. REAL-WORLD EXAMPLE - UNIQUE PHONE NUMBERS
# ============================================================

phone_numbers = {
    "9876543210",
    "9876543211",
    "9876543210",
    "9876543212"
}

print(phone_numbers)


# Duplicate number is automatically removed.


# ============================================================
# 18. REAL-WORLD EXAMPLE - STUDENT COURSES
# ============================================================

python_students = {
    "Priya",
    "Rahul",
    "Arun"
}

java_students = {
    "Rahul",
    "Arun",
    "Meena"
}

# Students learning both Python and Java

both = python_students.intersection(java_students)

print("Students learning both:", both)


# ============================================================
# IMPORTANT SET METHODS
# ============================================================

# add()
# update()
# remove()
# discard()
# pop()
# clear()
#
# union()
# intersection()
# difference()
# symmetric_difference()