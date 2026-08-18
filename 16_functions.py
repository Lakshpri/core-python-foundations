# ============================================================
# PYTHON FUNCTIONS
# ============================================================

# A function is a reusable block of code.
#
# Instead of writing the same code multiple times,
# we create a function and call it whenever required.
#
# Syntax:
#
# def function_name():
#     statements


# ============================================================
# 1. SIMPLE FUNCTION
# ============================================================

def greet():

    print("Hello!")
    print("Welcome to Python!")


# Calling the function

greet()


# ============================================================
# 2. CALLING A FUNCTION MULTIPLE TIMES
# ============================================================

def welcome():

    print("Welcome to the course!")


welcome()
welcome()
welcome()


# ============================================================
# 3. FUNCTION WITH A PARAMETER
# ============================================================

def greet_user(name):

    print("Hello", name)


greet_user("Priya")
greet_user("Rahul")


# ============================================================
# 4. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

def student_details(name, age):

    print("Name:", name)
    print("Age:", age)


student_details("Priya", 22)


# ============================================================
# 5. FUNCTION WITH RETURN
# ============================================================

def add(a, b):

    result = a + b

    return result


answer = add(10, 20)

print("Answer:", answer)


# ============================================================
# 6. RETURN MULTIPLE VALUES
# ============================================================

def calculate(a, b):

    addition = a + b
    subtraction = a - b

    return addition, subtraction


result1, result2 = calculate(20, 10)

print("Addition:", result1)
print("Subtraction:", result2)


# ============================================================
# 7. DEFAULT PARAMETER
# ============================================================

def greet(name="Student"):

    print("Hello", name)


greet("Priya")

greet()


# ============================================================
# 8. FUNCTION WITH CALCULATION
# ============================================================

def calculate_square(number):

    return number * number


print(calculate_square(5))
print(calculate_square(10))


# ============================================================
# 9. FUNCTION TO CHECK EVEN OR ODD
# ============================================================

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"


result = check_even_odd(10)

print(result)


# ============================================================
# 10. FUNCTION TO FIND LARGER NUMBER
# ============================================================

def find_larger(a, b):

    if a > b:
        return a

    else:
        return b


print(find_larger(10, 20))


# ============================================================
# 11. FUNCTION WITH LIST
# ============================================================

def calculate_total(numbers):

    total = 0

    for number in numbers:

        total = total + number

    return total


marks = [80, 90, 70, 85]

print("Total:", calculate_total(marks))


# ============================================================
# 12. FUNCTION WITH DICTIONARY
# ============================================================

def display_student(student):

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])


student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}

display_student(student)


# ============================================================
# 13. FUNCTION WITHOUT RETURN
# ============================================================

def display_message():

    print("Learning Python")


result = display_message()

print(result)

# The function does not return anything,
# so Python returns None.


# ============================================================
# 14. DOCSTRING
# ============================================================

def add_numbers(a, b):
    """
    This function adds two numbers
    and returns the result.
    """

    return a + b


print(add_numbers(10, 20))


# ============================================================
# 15. FUNCTION CALLING ANOTHER FUNCTION
# ============================================================

def add(a, b):

    return a + b


def display_result():

    result = add(10, 20)

    print("Result:", result)


display_result()


# ============================================================
# 16. REAL-WORLD EXAMPLE - SHOPPING BILL
# ============================================================

def calculate_bill(price, quantity):

    total = price * quantity

    return total


price = 500
quantity = 3

total = calculate_bill(price, quantity)

print("Total Bill:", total)


# ============================================================
# 17. REAL-WORLD EXAMPLE - STUDENT RESULT
# ============================================================

def calculate_average(marks):

    total = sum(marks)

    average = total / len(marks)

    return average


marks = [80, 90, 75, 85]

average = calculate_average(marks)

print("Average:", average)


# ============================================================
# 18. REAL-WORLD EXAMPLE - LOGIN
# ============================================================

def login(username, password):

    if username == "admin" and password == "1234":

        return True

    else:

        return False


username = input("Username: ")
password = input("Password: ")

if login(username, password):

    print("Login successful.")

else:

    print("Invalid username or password.")


# ============================================================
# FUNCTION SUMMARY
# ============================================================

# def
# parameter
# argument
# return
# default parameter
# docstring
#
# Functions help us:
#
# - Reuse code
# - Avoid repetition
# - Organize programs
# - Make programs easier to maintain