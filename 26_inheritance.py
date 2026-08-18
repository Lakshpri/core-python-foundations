# ============================================================
# INHERITANCE IN PYTHON
# ============================================================

# Inheritance allows a child class to
# reuse code from a parent class.
#
# Parent class -> Base class
#
# Child class -> Derived class


# ============================================================
# 1. SIMPLE INHERITANCE
# ============================================================

class Animal:

    def eat(self):

        print("Animal is eating.")


class Dog(Animal):

    def bark(self):

        print("Dog is barking.")


dog = Dog()

dog.eat()

dog.bark()


# Dog inherited eat()
# from Animal.


# ============================================================
# 2. PARENT + CHILD METHODS
# ============================================================

class Vehicle:

    def start(self):

        print("Vehicle started.")


class Car(Vehicle):

    def drive(self):

        print("Car is driving.")


car = Car()

car.start()

car.drive()


# ============================================================
# 3. MULTILEVEL INHERITANCE
# ============================================================

class Grandparent:

    def family_name(self):

        print("Family name: Kumar")


class Parent(Grandparent):

    def parent_method(self):

        print("Parent method")


class Child(Parent):

    def child_method(self):

        print("Child method")


child = Child()

child.family_name()

child.parent_method()

child.child_method()


# ============================================================
# 4. MULTIPLE INHERITANCE
# ============================================================

class Father:

    def father_property(self):

        print("Father property")


class Mother:

    def mother_property(self):

        print("Mother property")


class Child(Father, Mother):

    def child_property(self):

        print("Child property")


child = Child()

child.father_property()

child.mother_property()

child.child_property()


# ============================================================
# 5. METHOD INHERITANCE
# ============================================================

class Employee:

    def work(self):

        print("Employee is working.")


class Developer(Employee):

    def write_code(self):

        print("Developer is writing code.")


developer = Developer()

developer.work()

developer.write_code()


# ============================================================
# 6. METHOD OVERRIDING
# ============================================================

class Animal:

    def sound(self):

        print("Animal makes a sound.")


class Dog(Animal):

    def sound(self):

        print("Dog barks.")


dog = Dog()

dog.sound()


# The child class provides its own
# implementation of sound().


# ============================================================
# 7. SUPER()
# ============================================================

class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course


student = Student(
    "Priya",
    "Python"
)


print(student.name)

print(student.course)


# super() calls the parent class method.


# ============================================================
# 8. REAL-WORLD EXAMPLE
# ============================================================

class Employee:

    def login(self):

        print("Employee logged in.")


class Developer(Employee):

    def code(self):

        print("Developer is coding.")


class Tester(Employee):

    def test(self):

        print("Tester is testing.")


developer = Developer()

developer.login()

developer.code()


tester = Tester()

tester.login()

tester.test()


# ============================================================
# INHERITANCE SUMMARY
# ============================================================

# Parent class:
# class Animal:
#
# Child class:
# class Dog(Animal):
#
# Dog gets the methods and properties
# of Animal.
#
# Types:
#
# Single inheritance
# Multilevel inheritance
# Multiple inheritance