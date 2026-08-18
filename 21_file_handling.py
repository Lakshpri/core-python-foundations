# ============================================================
# FILE HANDLING IN PYTHON
# ============================================================

# File handling allows Python programs to:
#
# 1. Create files
# 2. Write data
# 3. Read data
# 4. Append data
# 5. Delete files
#
# Common modes:
#
# "r" -> read
# "w" -> write
# "a" -> append
# "x" -> create
#
# Binary modes:
#
# "rb" -> read binary
# "wb" -> write binary


# ============================================================
# 1. WRITING TO A FILE
# ============================================================

# "w" means write mode.
#
# If the file doesn't exist,
# Python creates it.
#
# If the file already exists,
# its previous content is replaced.

file = open("student.txt", "w")

file.write("Name: Priya\n")
file.write("Age: 22\n")
file.write("Course: Python\n")

file.close()


# ============================================================
# 2. READING A FILE
# ============================================================

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()


# ============================================================
# 3. READ ONE LINE
# ============================================================

file = open("student.txt", "r")

line = file.readline()

print(line)

file.close()


# ============================================================
# 4. READ ALL LINES
# ============================================================

file = open("student.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ============================================================
# 5. LOOP THROUGH FILE
# ============================================================

file = open("student.txt", "r")

for line in file:

    print(line.strip())

file.close()


# ============================================================
# 6. APPENDING DATA
# ============================================================

# "a" means append.
#
# Existing content is preserved.

file = open("student.txt", "a")

file.write("City: Chennai\n")

file.close()


# ============================================================
# 7. WITH STATEMENT
# ============================================================

# The with statement automatically closes the file.
#
# This is the preferred way to work with files.

with open("student.txt", "r") as file:

    content = file.read()

    print(content)


# ============================================================
# 8. WRITING MULTIPLE LINES
# ============================================================

students = [
    "Priya\n",
    "Rahul\n",
    "Arun\n",
    "Meena\n"
]

with open("students.txt", "w") as file:

    file.writelines(students)


# ============================================================
# 9. CHECKING FILE CONTENT
# ============================================================

with open("students.txt", "r") as file:

    for student in file:

        print(student.strip())


# ============================================================
# 10. REAL-WORLD EXAMPLE - LOGIN LOG
# ============================================================

username = input("Enter username: ")

with open("login_log.txt", "a") as file:

    file.write("User logged in: " + username + "\n")

print("Login recorded.")


# ============================================================
# 11. REAL-WORLD EXAMPLE - NOTES
# ============================================================

note = input("Enter your note: ")

with open("notes.txt", "a") as file:

    file.write(note + "\n")

print("Note saved successfully.")


# ============================================================
# IMPORTANT
# ============================================================

# Always prefer:
#
# with open(...) as file:
#
# because Python automatically closes the file.