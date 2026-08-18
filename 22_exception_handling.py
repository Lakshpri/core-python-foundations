# ============================================================
# EXCEPTION HANDLING
# ============================================================

# An exception is an error that occurs while
# a program is running.
#
# Examples:
#
# ZeroDivisionError
# ValueError
# TypeError
# FileNotFoundError
#
# We can handle exceptions using:
#
# try
# except
# else
# finally


# ============================================================
# 1. SIMPLE TRY-EXCEPT
# ============================================================

try:

    number = int(input("Enter a number: "))

    print("Number:", number)

except:

    print("Invalid input.")


# ============================================================
# 2. VALUEERROR
# ============================================================

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Please enter a valid integer.")


# ============================================================
# 3. ZERODIVISIONERROR
# ============================================================

try:

    a = 10
    b = 0

    result = a / b

    print(result)

except ZeroDivisionError:

    print("Cannot divide by zero.")


# ============================================================
# 4. MULTIPLE EXCEPTIONS
# ============================================================

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print(result)

except ValueError:

    print("Please enter a number.")

except ZeroDivisionError:

    print("Number cannot be zero.")


# ============================================================
# 5. EXCEPTION OBJECT
# ============================================================

try:

    number = int("hello")

except ValueError as error:

    print("Error:", error)


# ============================================================
# 6. ELSE
# ============================================================

# else runs only when there is NO exception.

try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid number.")

else:

    print("You entered:", number)


# ============================================================
# 7. FINALLY
# ============================================================

# finally runs whether an exception occurs or not.

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Invalid number.")

finally:

    print("Program finished.")


# ============================================================
# 8. TRY + EXCEPT + ELSE + FINALLY
# ============================================================

try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Invalid input.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Result:", result)

finally:

    print("Calculation completed.")


# ============================================================
# 9. FILE HANDLING EXCEPTION
# ============================================================

try:

    with open("unknown.txt", "r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print("File does not exist.")


# ============================================================
# 10. REAL-WORLD BANKING EXAMPLE
# ============================================================

balance = 5000

try:

    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:

        raise ValueError("Insufficient balance.")

    if amount <= 0:

        raise ValueError("Amount must be positive.")

    balance = balance - amount

    print("Withdrawal successful.")

    print("Remaining balance:", balance)

except ValueError as error:

    print("Transaction failed:", error)


# ============================================================
# IMPORTANT
# ============================================================

# try:
#     Risky code
#
# except:
#     What to do if error occurs
#
# else:
#     Runs if no error occurs
#
# finally:
#     Always runs