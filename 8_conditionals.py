# ============================================================
# CONDITIONAL STATEMENTS IN PYTHON
# ============================================================

# Conditional statements allow a program to make decisions.
#
# Main conditional statements:
#
# if
# if-else
# if-elif-else
# nested if


# ============================================================
# 1. SIMPLE IF
# ============================================================

age = 22

if age >= 18:
    print("You are eligible to vote.")


# ============================================================
# 2. IF CONDITION IS FALSE
# ============================================================

age = 15

if age >= 18:
    print("You are eligible to vote.")

# Nothing will be printed because condition is False.


# ============================================================
# 3. IF-ELSE
# ============================================================

age = 15

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


# ============================================================
# 4. CHECK POSITIVE OR NEGATIVE
# ============================================================

number = 10

if number >= 0:
    print("Positive number")
else:
    print("Negative number")


# ============================================================
# 5. EVEN OR ODD
# ============================================================

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ============================================================
# 6. IF-ELIF-ELSE
# ============================================================

marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")


# ============================================================
# 7. MULTIPLE CONDITIONS
# ============================================================

age = 22
has_degree = True

if age >= 18 and has_degree:
    print("Eligible for the job.")


# ============================================================
# 8. USING OR
# ============================================================

has_id = True
has_pass = False

if has_id or has_pass:
    print("Entry allowed.")
else:
    print("Entry denied.")


# ============================================================
# 9. USING NOT
# ============================================================

is_blocked = False

if not is_blocked:
    print("User can access the account.")


# ============================================================
# 10. NESTED IF
# ============================================================

age = 22
has_degree = True

if age >= 18:

    print("Age requirement satisfied.")

    if has_degree:
        print("Degree requirement satisfied.")
        print("Eligible.")

    else:
        print("Degree required.")

else:
    print("Age requirement not satisfied.")


# ============================================================
# 11. REAL-WORLD LOGIN EXAMPLE
# ============================================================

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")


# ============================================================
# 12. REAL-WORLD SHOPPING DISCOUNT
# ============================================================

amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = 20

elif amount >= 3000:
    discount = 15

elif amount >= 1000:
    discount = 10

else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Original Amount:", amount)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)


# ============================================================
# 13. STUDENT RESULT
# ============================================================

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"

print("Your Grade:", grade)