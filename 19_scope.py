# ============================================================
# VARIABLE SCOPE IN PYTHON
# ============================================================

# Scope means the area of the program
# where a variable can be accessed.
#
# Main types:
#
# 1. Local scope
# 2. Global scope
# 3. Enclosing scope
# 4. Built-in scope
#
# Together they are often remembered using:
#
# LEGB
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in


# ============================================================
# 1. GLOBAL VARIABLE
# ============================================================

# Created outside a function.

college = "ABC Engineering College"


def display_college():

    # We can access the global variable
    # inside the function.

    print(college)


display_college()


# We can also access it outside the function.

print(college)


# ============================================================
# 2. LOCAL VARIABLE
# ============================================================

def student():

    # This variable exists only inside the function.

    name = "Priya"

    print(name)


student()


# The following would cause an error:
#
# print(name)
#
# because name is local to student().


# ============================================================
# 3. SAME VARIABLE NAME
# ============================================================

name = "Global Priya"


def display():

    name = "Local Priya"

    print("Inside function:", name)


display()

print("Outside function:", name)


# The local variable does not change
# the global variable.


# ============================================================
# 4. MODIFYING GLOBAL VARIABLE
# ============================================================

count = 10


def update_count():

    global count

    count = 20


update_count()

print(count)


# ============================================================
# 5. WITHOUT global
# ============================================================

value = 10


def change_value():

    # This creates a NEW local variable.

    value = 20

    print("Inside:", value)


change_value()

print("Outside:", value)


# ============================================================
# 6. WITH global
# ============================================================

value = 10


def change_value():

    global value

    value = 20


change_value()

print(value)


# ============================================================
# 7. ENCLOSING SCOPE
# ============================================================

def outer():

    message = "Hello from outer function"

    def inner():

        # inner() can access the variable
        # from outer().

        print(message)

    inner()


outer()


# ============================================================
# 8. nonlocal
# ============================================================

def outer():

    count = 10

    def inner():

        nonlocal count

        count = 20

    inner()

    print(count)


outer()


# ============================================================
# 9. BUILT-IN SCOPE
# ============================================================

# Python already provides built-in functions
# such as:
#
# print()
# len()
# sum()
# max()
# min()
#
# These belong to Python's built-in scope.

numbers = [10, 20, 30]

print(len(numbers))

print(sum(numbers))

print(max(numbers))


# ============================================================
# 10. LEGB EXAMPLE
# ============================================================

x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        x = "Local"

        print(x)

    inner()


outer()


# Python finds the LOCAL variable first.


# ============================================================
# 11. REAL-WORLD EXAMPLE
# ============================================================

company = "ABC Technologies"


def employee():

    employee_name = "Priya"

    print("Company:", company)

    print("Employee:", employee_name)


employee()


# company -> global
# employee_name -> local


# ============================================================
# SCOPE SUMMARY
# ============================================================

# Local:
# Variable created inside a function.
#
# Enclosing:
# Variable from an outer function.
#
# Global:
# Variable created outside functions.
#
# Built-in:
# Python's predefined names/functions.
#
# LEGB:
# Local
# Enclosing
# Global
# Built-in