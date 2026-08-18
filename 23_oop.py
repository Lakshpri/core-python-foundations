# ============================================================
# INTRODUCTION TO OBJECT-ORIENTED PROGRAMMING
# ============================================================

# OOP = Object-Oriented Programming
#
# OOP allows us to structure programs using:
#
# Classes
# Objects
# Attributes
# Methods
#
# Main OOP concepts:
#
# 1. Class
# 2. Object
# 3. Encapsulation
# 4. Inheritance
# 5. Polymorphism
# 6. Abstraction


# ============================================================
# 1. WHAT IS A CLASS?
# ============================================================

# A class is a blueprint/template.
#
# Example:
#
# A "Student" class can describe:
#
# name
# age
# course
#
# and actions:
#
# study()
# attend_class()
# write_exam()


class Student:

    pass


# ============================================================
# 2. CREATING AN OBJECT
# ============================================================

student1 = Student()

student2 = Student()

print(student1)

print(student2)


# student1 and student2 are objects
# created from the Student class.


# ============================================================
# 3. CLASS WITH ATTRIBUTES
# ============================================================

class Student:

    name = "Priya"
    age = 22
    course = "Python"


student1 = Student()

print(student1.name)
print(student1.age)
print(student1.course)


# ============================================================
# 4. CLASS WITH METHOD
# ============================================================

class Student:

    def greet(self):

        print("Hello! I am a student.")


student1 = Student()

student1.greet()


# ============================================================
# 5. MULTIPLE OBJECTS
# ============================================================

class Student:

    def greet(self):

        print("Hello student!")


student1 = Student()
student2 = Student()

student1.greet()
student2.greet()


# ============================================================
# 6. SELF
# ============================================================

# self represents the current object.
#
# It allows us to access the object's data.


class Student:

    def display(self):

        print("This is the current object:", self)


student1 = Student()

student1.display()


# ============================================================
# 7. REAL-WORLD EXAMPLE
# ============================================================

class Car:

    def start(self):

        print("Car started.")

    def stop(self):

        print("Car stopped.")


car1 = Car()

car1.start()

car1.stop()


# ============================================================
# 8. ANOTHER REAL-WORLD EXAMPLE
# ============================================================

class BankAccount:

    def deposit(self):

        print("Money deposited.")

    def withdraw(self):

        print("Money withdrawn.")


account = BankAccount()

account.deposit()

account.withdraw()


# ============================================================
# IMPORTANT
# ============================================================

# Class:
# Blueprint
#
# Object:
# Real instance created from the class
#
# Attribute:
# Data belonging to an object/class
#
# Method:
# Function defined inside a class