# ============================================================
# PYTHON DICTIONARIES
# ============================================================

# A dictionary stores data in KEY : VALUE pairs.
#
# Example:
#
# student = {
#     "name": "Priya",
#     "age": 22,
#     "course": "Python"
# }
#
# "name"   -> key
# "Priya"  -> value


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

print(student)


# ============================================================
# 2. ACCESSING VALUES
# ============================================================

print(student["name"])
print(student["age"])
print(student["course"])


# ============================================================
# 3. GET()
# ============================================================

# get() can be used to access a value.

print(student.get("name"))

print(student.get("age"))


# If the key does not exist,
# get() returns None instead of causing an error.

print(student.get("city"))


# ============================================================
# 4. ADDING A NEW KEY-VALUE PAIR
# ============================================================

student["city"] = "Chennai"

print(student)


# ============================================================
# 5. UPDATING A VALUE
# ============================================================

student["age"] = 23

print(student)


# ============================================================
# 6. REMOVE USING pop()
# ============================================================

student.pop("city")

print(student)


# ============================================================
# 7. popitem()
# ============================================================

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

# Removes the last key-value pair.

student.popitem()

print(student)


# ============================================================
# 8. del
# ============================================================

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

del student["age"]

print(student)


# ============================================================
# 9. clear()
# ============================================================

student = {
    "name": "Priya",
    "age": 22
}

student.clear()

print(student)


# ============================================================
# 10. KEYS()
# ============================================================

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

print(student.keys())


# ============================================================
# 11. VALUES()
# ============================================================

print(student.values())


# ============================================================
# 12. ITEMS()
# ============================================================

print(student.items())


# ============================================================
# 13. CHECK IF KEY EXISTS
# ============================================================

student = {
    "name": "Priya",
    "age": 22
}

print("name" in student)

print("city" in student)


# ============================================================
# 14. LOOP THROUGH KEYS
# ============================================================

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

for key in student:
    print(key)


# ============================================================
# 15. LOOP THROUGH VALUES
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# 16. LOOP THROUGH KEY AND VALUE
# ============================================================

for key, value in student.items():

    print(key, ":", value)


# ============================================================
# 17. DICTIONARY LENGTH
# ============================================================

print(len(student))


# ============================================================
# 18. NESTED DICTIONARY
# ============================================================

student = {
    "name": "Priya",
    "marks": {
        "python": 90,
        "java": 85,
        "sql": 88
    }
}

print(student)

print(student["marks"])

print(student["marks"]["python"])


# ============================================================
# 19. LIST OF DICTIONARIES
# ============================================================

students = [
    {
        "name": "Priya",
        "age": 22
    },
    {
        "name": "Rahul",
        "age": 23
    },
    {
        "name": "Arun",
        "age": 21
    }
]

print(students)

print(students[0])

print(students[0]["name"])


# ============================================================
# 20. REAL-WORLD EXAMPLE - PRODUCT
# ============================================================

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "brand": "Dell",
    "available": True
}

print("Product ID:", product["id"])
print("Product Name:", product["name"])
print("Price:", product["price"])
print("Brand:", product["brand"])
print("Available:", product["available"])


# ============================================================
# 21. REAL-WORLD EXAMPLE - EMPLOYEE
# ============================================================

employee = {
    "id": 1001,
    "name": "Priya",
    "department": "IT",
    "salary": 40000
}

for key, value in employee.items():

    print(key, ":", value)


# ============================================================
# IMPORTANT DICTIONARY METHODS
# ============================================================

# get()
# keys()
# values()
# items()
# update()
# pop()
# popitem()
# clear()
#
# Useful:
# len()