
# ============================================================
# PART 2 - ABSTRACTION
# ============================================================

# Abstraction means hiding implementation details
# and exposing only the necessary functionality.
#
# Example:
#
# When we use an ATM:
#
# We select:
# Withdraw
#
# We don't need to know the internal banking
# implementation.


# ============================================================
# 7. ABSTRACT CLASS
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass


# Animal is an abstract class.
#
# sound() is an abstract method.
#
# The child class must implement sound().


# ============================================================
# 8. IMPLEMENTING ABSTRACT METHOD
# ============================================================

class Dog(Animal):

    def sound(self):

        print("Dog barks.")


dog = Dog()

dog.sound()


# ============================================================
# 9. ANOTHER ABSTRACT CLASS
# ============================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):

        pass


class UPI(Payment):

    def pay(self, amount):

        print(
            "Paid",
            amount,
            "using UPI."
        )


class CreditCard(Payment):

    def pay(self, amount):

        print(
            "Paid",
            amount,
            "using Credit Card."
        )


upi = UPI()

upi.pay(500)


card = CreditCard()

card.pay(1000)


# ============================================================
# 10. REAL-WORLD ABSTRACTION
# ============================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass


class Car(Vehicle):

    def start(self):

        print("Car starts using engine.")


class ElectricCar(Vehicle):

    def start(self):

        print("Electric car starts using battery.")


car = Car()

electric_car = ElectricCar()

car.start()

electric_car.start()


# ============================================================
# ENCAPSULATION VS ABSTRACTION
# ============================================================

# ENCAPSULATION
#
# Focus:
# Protecting/bundling data and methods.
#
# Example:
# __balance
#
#
# ABSTRACTION
#
# Focus:
# Hiding implementation details.
#
# Example:
# abstractmethod
#
#
# Simple way to remember:
#
# Encapsulation -> "Protect the data"
#
# Abstraction   -> "Hide the complexity"


# ============================================================
# COMPLETE REAL-WORLD EXAMPLE
# ============================================================

class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):

        pass


class BankATM(ATM):

    def __init__(self, balance):

        # Private variable
        self.__balance = balance


    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid amount.")

        elif amount > self.__balance:

            print("Insufficient balance.")

        else:

            self.__balance -= amount

            print("Please collect your cash.")


    def check_balance(self):

        print(
            "Available balance:",
            self.__balance
        )


atm = BankATM(10000)

atm.check_balance()

atm.withdraw(2000)

atm.check_balance()


# ============================================================
# FINAL OOP SUMMARY
# ============================================================

# CLASS
# -> Blueprint for objects
#
# OBJECT
# -> Instance of a class
#
# CONSTRUCTOR
# -> __init__()
#
# INHERITANCE
# -> Reuse code from another class
#
# POLYMORPHISM
# -> Same interface, different behavior
#
# ENCAPSULATION
# -> Bundle/protect data and methods
#
# ABSTRACTION
# -> Hide implementation complexity