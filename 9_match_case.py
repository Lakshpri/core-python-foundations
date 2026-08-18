# ============================================================
# MATCH-CASE IN PYTHON
# ============================================================

# match-case is used when we want to compare
# one value against multiple possible patterns.
#
# It is similar to switch-case in languages like Java.


# ============================================================
# 1. BASIC MATCH-CASE
# ============================================================

day = 1

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid day")


# ============================================================
# 2. TAKING USER INPUT
# ============================================================

choice = int(input("Enter 1, 2 or 3: "))

match choice:

    case 1:
        print("You selected Add")

    case 2:
        print("You selected Update")

    case 3:
        print("You selected Delete")

    case _:
        print("Invalid choice")


# ============================================================
# 3. SIMPLE CALCULATOR
# ============================================================

number1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
number2 = float(input("Enter second number: "))

match operator:

    case "+":
        print("Result:", number1 + number2)

    case "-":
        print("Result:", number1 - number2)

    case "*":
        print("Result:", number1 * number2)

    case "/":

        if number2 != 0:
            print("Result:", number1 / number2)

        else:
            print("Cannot divide by zero.")

    case _:
        print("Invalid operator.")


# ============================================================
# 4. ATM MENU
# ============================================================

print()
print("---------- ATM ----------")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("Checking balance...")

    case 2:
        print("Deposit selected.")

    case 3:
        print("Withdrawal selected.")

    case 4:
        print("Thank you. Goodbye!")

    case _:
        print("Invalid option.")


# ============================================================
# 5. MATCH CASE WITH STRINGS
# ============================================================

role = input("Enter your role: ")

match role.lower():

    case "admin":
        print("You have full access.")

    case "manager":
        print("You have manager access.")

    case "employee":
        print("You have employee access.")

    case _:
        print("Unknown role.")


# ============================================================
# 6. GROUPING CASES
# ============================================================

day = input("Enter day: ").lower()

match day:

    case "saturday" | "sunday":
        print("Weekend")

    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")

    case _:
        print("Invalid day")


# ============================================================
# IMPORTANT
# ============================================================

# case _:
#
# acts like the default case.
#
# It runs when none of the previous cases match.