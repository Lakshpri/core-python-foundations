# ============================================================
# ENCAPSULATION AND ABSTRACTION
# ============================================================


# ============================================================
# PART 1 - ENCAPSULATION
# ============================================================

# Encapsulation means:
#
# Bundling data and methods together
# inside a class.
#
# It also helps control access to data.
#
# Python commonly uses:
#
# Public
# _protected
# __private


# ============================================================
# 1. PUBLIC VARIABLE
# ============================================================

class Student:

    def __init__(self, name):

        self.name = name


student = Student("Priya")

print(student.name)


# Public data can be accessed directly.


# ============================================================
# 2. PROTECTED VARIABLE
# ============================================================

class Student:

    def __init__(self, name):

        self._name = name


student = Student("Priya")

print(student._name)


# _name indicates that it is intended
# for internal/protected use.
#
# Python does not strictly prevent access.


# ============================================================
# 3. PRIVATE VARIABLE
# ============================================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


account = BankAccount(50000)


# Direct access like this is not normally allowed:
#
# print(account.__balance)


# ============================================================
# 4. ACCESS PRIVATE DATA USING METHOD
# ============================================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def get_balance(self):

        return self.__balance


account = BankAccount(50000)

print(account.get_balance())


# ============================================================
# 5. ENCAPSULATION WITH DEPOSIT
# ============================================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

            print("Deposit successful.")

        else:

            print("Invalid amount.")


    def get_balance(self):

        return self.__balance


account = BankAccount(10000)

account.deposit(5000)

print("Balance:", account.get_balance())


# ============================================================
# 6. ENCAPSULATION WITH WITHDRAWAL
# ============================================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount


    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid amount.")

        elif amount > self.__balance:

            print("Insufficient balance.")

        else:

            self.__balance -= amount

            print("Withdrawal successful.")


    def get_balance(self):

        return self.__balance


account = BankAccount(10000)

account.deposit(5000)

account.withdraw(3000)

print("Balance:", account.get_balance())

