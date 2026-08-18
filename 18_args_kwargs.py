# ============================================================
# *args AND **kwargs
# ============================================================

# This file focuses specifically on:
#
# *args
# **kwargs
#
# These are useful when we don't know beforehand
# how many arguments a function will receive.


# ============================================================
# 1. *args
# ============================================================

def show_numbers(*numbers):

    print(numbers)


show_numbers(10, 20, 30)


# *args stores values as a TUPLE.


def show_numbers(*numbers):

    print(numbers)
    print(type(numbers))


show_numbers(10, 20, 30)


# ============================================================
# 2. LOOPING THROUGH *args
# ============================================================

def show_numbers(*numbers):

    for number in numbers:

        print(number)


show_numbers(10, 20, 30, 40, 50)


# ============================================================
# 3. SUM USING *args
# ============================================================

def calculate_sum(*numbers):

    total = 0

    for number in numbers:

        total += number

    return total


print(calculate_sum(10, 20))

print(calculate_sum(10, 20, 30))

print(calculate_sum(10, 20, 30, 40, 50))


# ============================================================
# 4. FIND MAXIMUM USING *args
# ============================================================

def find_maximum(*numbers):

    return max(numbers)


print(find_maximum(10, 50, 20, 90, 30))


# ============================================================
# 5. **kwargs
# ============================================================

def show_details(**details):

    print(details)


show_details(
    name="Priya",
    age=22,
    city="Chennai"
)


# **kwargs stores values as a DICTIONARY.


# ============================================================
# 6. LOOP THROUGH **kwargs
# ============================================================

def show_details(**details):

    for key, value in details.items():

        print(key, ":", value)


show_details(
    name="Priya",
    age=22,
    city="Chennai"
)


# ============================================================
# 7. *args AND **kwargs TOGETHER
# ============================================================

def display(*args, **kwargs):

    print("Arguments:", args)

    print("Keyword arguments:", kwargs)


display(
    10,
    20,
    30,
    name="Priya",
    age=22
)


# ============================================================
# 8. NORMAL PARAMETER + *args
# ============================================================

def greet(greeting, *names):

    for name in names:

        print(greeting, name)


greet(
    "Hello",
    "Priya",
    "Rahul",
    "Arun"
)


# ============================================================
# 9. NORMAL PARAMETER + **kwargs
# ============================================================

def employee(role, **details):

    print("Role:", role)

    for key, value in details.items():

        print(key, ":", value)


employee(
    "Developer",
    name="Priya",
    age=22,
    city="Chennai"
)


# ============================================================
# 10. REAL-WORLD BILLING SYSTEM
# ============================================================

def calculate_bill(customer_name, *prices):

    total = sum(prices)

    print("Customer:", customer_name)

    print("Total:", total)


calculate_bill(
    "Priya",
    100,
    200,
    300
)


# ============================================================
# 11. REAL-WORLD PROFILE SYSTEM
# ============================================================

def create_user(**details):

    print("---------- USER ----------")

    for key, value in details.items():

        print(key, ":", value)


create_user(
    name="Priya",
    age=22,
    email="priya@example.com",
    city="Chennai"
)


# ============================================================
# 12. IMPORTANT DIFFERENCE
# ============================================================

# *args
# -> Multiple positional arguments
# -> Stored as tuple
#
# **kwargs
# -> Multiple keyword arguments
# -> Stored as dictionary


# ============================================================
# EXAMPLE
# ============================================================

def example(*args, **kwargs):

    print("args:", args)
    print("args type:", type(args))

    print("kwargs:", kwargs)
    print("kwargs type:", type(kwargs))


example(
    10,
    20,
    30,
    name="Priya",
    age=22
)